#!/usr/bin/env python
from itertools import groupby
from operator import itemgetter
import sys

def read_mapper_output(file, separator='\t'):
    for line in file:
        yield line.rstrip().split(separator, 1)

def main(separator='\t'):
    data = read_mapper_output(sys.stdin, separator=separator)
    word_counts = []
    for current_word, group in groupby(data, itemgetter(0)):
        try:
            total_count = sum(int(count) for current_word, count in group)
            word_counts.append((current_word, total_count))
        except ValueError:
            pass

    top_3 = sorted(word_counts, key=lambda x: x[1], reverse=True)[:3]
    for word, count in top_3:
        print("%s%s%d" % (word, separator, count))

if __name__ == "__main__":
    main()
