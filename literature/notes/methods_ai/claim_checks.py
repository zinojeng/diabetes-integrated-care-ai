#!/usr/bin/env python3
"""Reproducible grep checks for methods_ai claims. Usage: python3 -I claim_checks.py  (run from repo root)."""
import re, sys
from pathlib import Path
D = Path("literature/parsed/methods_ai")
CHK = {
 "PMC10784572 ACCESS": ["164 participants", r"81/81", r"18/8[12]", r"16/25", r"64%", r"22%", r"n = 163", r"6 months"],
 "PMC6550188 pivotal": [r"87\.2%", r"90\.7%", r"96\.1%", r"819", r"198 \(23\.8%\)", r"892"],
 "PMC10692866 voice": [r"39 participants were randomized", r"32 participants", r"82\.9%", r"50\.2%", r"32\.7%", r"15 days", r"8 weeks"],
 "PMC12059970 iNCDSS": [r"149", r"76\.4%", r"73\.6%", r"−2\.7% to 8\.0%", r"6 percentage points", r"Thirteen participants", r"68 participants in each group"],
 "PMC12547058 GPT4": [r"243", r"230", r"115", r"64% for accuracy", r"35% for specificity", r"40%", r"25% \(29 of 115\)"],
 "PMC12768499 scribe": [r"N=238", r"9\.5%", r"−17\.2% to −1\.8%", r"0\.025", r"33\.5%", r"29\.5%", r"single academic institution", r"English-only"],
 "PMC13472850 Kenya": [r"9,691", r"9,347", r"102/4,693", r"94/4,654", r"0\.77", r"0\.55 to 1\.08", r"adjusted for facility and clinical officer", r"50% relative reduction"],
 "PMC12885450 He JMIR": [r"67\.93", r"300 treatment recommendations", r"not yet been prospectively validated", r"single medical institution"],
 "PMC13430954 Guo RAG-CGM": [r"4\.37", r"0\.782", r"288", r"864", r"3, 0\.7%"],
 "PMC13022550 TMU nursing": [r"3\.45", r"1\.17", r"474-981", r"September 2024", r"October-December 2024"],
 "PMC3022040 O'Connor": [r"2,556", r"11 clinics", r"−0\.26%", r"P = \.62"],
 "PMC4752167 Tangri2016": [r"721,357", r"31 cohorts", r"23,829", r"32\.9%", r"16\.5%", r"CKD-EPI\) 2009", r"170 mg/g"],
 "PMC13403277 Walker": [r"61\.2%", r"70\.3%", r"1\.75 at 5 years", r"O/E ratio 0\.98"],
 "Grams2023_KFRE_AAM": [r"eGFR <45", r"45-59", r"CKD-EPI 2021"],
 "PMC11911190 ML-DKD SR": [r"26 studies", r"only 8 studies", r"0\.839", r"0\.830"],
 "PMC12291684 DR-pred SR": [r"All 15 included studies were recognized as high risk of bias"],
 "PMC12481961 DPN-ML SR": [r"All studies had a high risk of bias", r"0\.773"],
 "PMC11465834 Su Taiwan": [r"0\.77, 0\.60 and 0\.64", r"UKPDS-OM2, RECODe, and CHIME"],
 "PMC11931409 PROBAST+AI": [r"16 targeted signalling questions", r"18 targeted signalling questions"],
 "PMC12485036 Kim2025": [r"A total of 606 reference messages", r"No \[0\], n = 300; Yes \[1\], n = 306", r"Stanford Health Care", r"Challenging cases \(N = 39\)", r"0\.61 vs\. 0\.81", r"0\.51 vs\. 0\.90"],
 "PMC11653048 Wu2024": [r"only 1 \(4%\) randomized controlled trial", r"4 groups of pre-post trials and 219 trial participants", r"MD\] 0\.30, 95% CI 0\.04-0\.55", r"January 1, 2023"],
 "PMC12707440 Zhang2025": [r"ES\]=0\.30", r"\[PI\] −0\.85, 1\.67", r"14 RCTs", r"registered the protocol retrospectively", r"g=0\.54, SE=0\.26", r"g=0\.41"],
 "PMC9293940 Samal2022": [r"5,590 patients", r"118 of 419", r"161 of 421", r"NCT02990897", r"clicked 122 times"],
 "PMC10906435 SperlHillen2024": [r"32 Midwestern primary care clinics", r"6,420 patients", r"1\.02; 95% CI, 0\.79-1\.32", r"NCT03890588"],
 "PMC11176869 MacNeill2024": [r"68 participants", r"no intervention", r"NCT04620668"],
 "PMC7677021 Gong2020": [r"−0\.04%, 95% CI −0\.45 to 0\.36", r"187 adults"],
 "PMC11019967 TRIPOD+AI": [r"TRIPOD\+AI"],
}
miss = 0
for key, pats in CHK.items():
    f = D / (key.split()[0] + ".md")
    t = f.read_text(errors="ignore") if f.exists() else ""
    for p in pats:
        n = len(re.findall(p, t))
        flag = "OK " if n else "MISS"
        miss += (n == 0)
        print(f"{flag} {key:28s} {p!r} x{n}")
print("MISSES:", miss)
