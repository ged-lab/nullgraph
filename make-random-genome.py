#! /usr/bin/env python
import random
import argparse
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--length', type=int, default=100000,
                        help="Simulated genome length")
    parser.add_argument('-s', '--seed', type=int, default=1,
                        help="Random number seed")
    parser.add_argument('--name', type=str, help='sequence name',
                        default='genome')
    args = parser.parse_args()

    LENGTH = args.length

    random.seed(args.seed)

    print >>sys.stderr, 'Using random seed:', args.seed

    x = ["A"] + ["G"] + ["C"] + ["T"]
    x = x*(args.length / 4)

    random.shuffle(x)

    print '>%s\n%s' % (args.name, "".join(x))

if __name__ == '__main__':
    main()
