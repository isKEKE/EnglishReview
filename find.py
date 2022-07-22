# _*_ coding: utf-8 _*_
import glob
import os
import re
from typing import Generator
from argparse import ArgumentParser

# 查找文件
FIND_FILES_NAME = "联想单词-*.md"
# 当前目录
CURRENT_DIR_PATH = os.path.dirname(__file__)

def ergodic_word() -> Generator:
    '''ergodic file'''
    for filename in glob.glob(FIND_FILES_NAME):
        filepath = os.path.join(CURRENT_DIR_PATH, filename)
        for line in open(filepath, encoding="utf-8"):
            yield (filepath, line)


def find_word(keyword: str) -> None:
    '''find keyword'''
    for filepath, line in ergodic_word():
        word = re.match("#### \d+\.\s+([A-z ]+)\n", line)
        if word is not None and ((word := word.group(1)).lower() == keyword.lower()):
            print(filepath, word)


if __name__ == "__main__":
    parser = ArgumentParser(description="Find out whether this word exists")
    parser.add_argument("-f", type=str, help="Set the keyword to find it.")
    args = parser.parse_args()

    if args.f is None:
        raise AttributeError("Please set keyword or check the help.")
    else:
        find_word(args.f)