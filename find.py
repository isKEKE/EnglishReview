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
        words = re.match("#### (\d+)\.\s+([A-z ]+)\n", line)
        if words is not None and ((word := words.group(2)).lower() == keyword.lower()):
            index = words.group(1)
            print("-"*50)
            print(filepath, index, word)
            print_chinese_content(filepath, index, word)
            print("-"*50)


def print_chinese_content(filepath: str, index: str, word: str) -> None:
    with open(filepath, encoding="utf-8") as fp:
        content = fp.read()
    pattern = f'''#### {index}\.\s+{word}\s+-\s```(.*?)```'''
    try:
        done = re.findall(pattern, content, re.DOTALL)[0]
        print(done.rstrip()[1:])
    except IndexError:
        ...


if __name__ == "__main__":
    parser = ArgumentParser(description="Find out whether this word exists")
    parser.add_argument("-f", type=str, help="Set the keyword to find it.")
    args = parser.parse_args()

    if args.f is None:
        raise AttributeError("Please set keyword or check the help.")
    else:
        find_word(args.f)
