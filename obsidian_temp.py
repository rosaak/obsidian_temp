import os
from subprocess import call
from datetime import datetime, timezone
import argparse

# Set the Vault location
VAULT = "/Users/roshan/Google Drive/KB/InBox/thoughts/"

def get_time():
    """
    :return: two date time string obj
    """
    tz = datetime.now(timezone.utc).astimezone().tzinfo
    now = datetime.now()
    x1 = now.strftime("%Y%m%d%H%M%S")
    x2 = now.strftime(f"%A %B %d {tz} %Y %H:%M:%S %p")
    return x1, x2


def make_yaml(dts, t=None, a=None, w=None, f=None, s=None):
    yml = f"""---
date : {dts}
where : {w}
activity : {a}
feelings : {f}
subject : {s}
tags : {t}
---

# Note 💭









# Links 🔗









---
- possible options 🎲
     - where : office outdoor
     - activity : reading
     - feelings : sad puke poop angry mad shitty lonely alone depressed ecstatic
     - subject : science technology philosophy
     - tags : thoughts quote sci-fi music PKM AI art 
- some cheat sheets 🔗
     - [markdown](https://guides.github.com/features/mastering-markdown/)
     - [mermaidjs](https://jojozhuang.github.io/tutorial/mermaid-cheat-sheet/)
     - [emoji](https://github.com/ikatyang/emoji-cheat-sheet)
"""
    return yml


def aparse():
    desc = """
    This script makes quick note template and save it to the Obsidian vault and opens it up on vim
    It can be later modified in the Obsidian
    """
    usage = """
    example 1: python3 obsidian_temp.py -tags idea -where work -activity reading -subject science -feelings awesome
    example 2: python3 obsidian_temp.py -t idea -w work -a reading -s science -f awesome
    example 3: python3 obsidian_temp.py -t quote -w home -s nonfiction biography -f cool"""

    parser = argparse.ArgumentParser(usage=usage, description=desc,  conflict_handler='resolve',
                                     formatter_class=argparse.RawTextHelpFormatter,)
    parser.add_argument('-t', help='tags', nargs='+', action='store', dest='t', required=False)
    parser.add_argument('-w', help='where', nargs='+', action='store', dest='w', required=False)
    parser.add_argument('-a', help='activity', nargs='+', action='store', dest='a', required=False)
    parser.add_argument('-s', help='subject', nargs='+', action='store', dest='s', required=False)
    parser.add_argument('-f', help='feelings', nargs='+', action='store', dest='f', required=False)
    args = parser.parse_args()
    return args


def process_arg(obj):
    if obj is not None:
        return ' '.join(obj)
    else:
        return obj


def main(vault_loc):
    arg = aparse()
    fn, ifn = get_time()
    T, A, W, S, F = process_arg(arg.t), process_arg(arg.a), process_arg(arg.w), process_arg(arg.s), process_arg(arg.f)
    _ = make_yaml(dts=ifn, t=T, a=A, w=W, s=S, f=F)
    # print(_)
    nfn = os.path.join(vault_loc, f"rp_{fn}.md")
    with open(nfn, "w") as ifh:
       [ifh.writelines(i) for i in _]
    # Open $EDITOR with the new file
    EDITOR = os.environ.get('EDITOR','nvim')
    call([EDITOR, nfn])


main(VAULT)
