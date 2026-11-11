#!/usr/bin/env python
import sys

def read_input(file):
    for line in file:
        yield line.split()

def main(separator='\t'):
    data = read_input(sys.stdin)
    for words in data:
        for word in words:
            clean_word = word.strip(".,").lower()
            if clean_word:
                print("%s%s%d" % (clean_word, separator, 1))

if __name__ == "__main__":
    main()
