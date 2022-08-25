import re
import os
import json
import subprocess
# --------------------------------------------------------


def fixjson(badjson):
    s = badjson
    idx = 0
    while True:
        try:
            start = s.index('": "', idx) + 4
            end1 = s.index('",\n', idx)
            end2 = s.index('"\n', idx)
            if end1 < end2:
                end = end1
            else:
                end = end2
            content = s[start:end]
            content = content.replace('"', '\\"')
            s = s[:start] + content + s[end:]
            idx = start + len(content) + 6
        except:
            return s
# -------------------------------------


def remove(string):
    return string.replace("  ", "")


def getVerNumber(string):
    l = [int(x) for x in string.split() if x.isdigit()]
    return max(l) if l else None


def copy2clip(txt):
    cmd = 'echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)
# ---------------------------------------------------------


def discordorother(dat):
    data = json.loads(fixjson(dat))
    print("From : " + data["from"]["address"])
    print("From Name :" + data["from"]["name"])
    print("Subject : " + data["subject"])
    print("Text : " + remove(data["text"]))
    stringalo = getVerNumber(remove(data["text"]))
    print("Verification Number Has Been Copied to Clipboard ")
    copy2clip(str(stringalo))
    # ---- subprocess.run("pbcopy", universal_newlines=True,
    #             input=stringalo)
