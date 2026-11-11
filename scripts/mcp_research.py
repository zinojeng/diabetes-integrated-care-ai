#!/usr/bin/env python3
"""Thin local MCP client; requires `mcp` Python package. Never prints config/env."""
import argparse, asyncio, json, os, pathlib
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

ROOT = pathlib.Path(__file__).resolve().parents[1]

async def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('server', choices=['research_hub', 'paper-search', 'scihub', 'llamaparse'])
    ap.add_argument('tool', nargs='?')
    ap.add_argument('--arguments', default='{}')
    ap.add_argument('--timeout', type=int, default=35)
    a = ap.parse_args()
    config = json.loads((pathlib.Path.home()/'.claude.json').read_text())
    item = config.get('mcpServers', {}).get(a.server)
    if not item:
        raise SystemExit('MCP server not configured: '+a.server)
    env = {**os.environ, **item.get('env', {})}
    # Reuse an existing interpreter rather than asking uv to mutate its cache.
    if a.server == 'paper-search':
        cached = pathlib.Path.home()/'paper-search-mcp/.venv/bin/python'
        if cached.exists():
            item = {**item, 'command': str(cached), 'args': ['-m', 'paper_search_mcp.server']}
    if a.server == 'llamaparse':
        env.pop('LLAMA_CLOUD_API_KEY', None)
        env['LLAMA_CLOUD_API_KEY_FILE'] = str(ROOT/'.local/llamaparse.key')
    params = StdioServerParameters(command=item['command'], args=item.get('args', []), env=env, cwd=str(ROOT))
    async with asyncio.timeout(a.timeout):
        async with stdio_client(params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                result = await session.call_tool(a.tool, json.loads(a.arguments)) if a.tool else await session.list_tools()
                print(result.model_dump_json(indent=2))
                failed = bool(getattr(result, 'isError', getattr(result, 'is_error', False)))
    if failed: raise SystemExit(1)

if __name__ == '__main__':
    try: asyncio.run(main())
    except TimeoutError: raise SystemExit('MCP timeout; completion not verified.')
    except Exception as e: raise SystemExit('MCP failed: '+type(e).__name__+'; no verified result.')
