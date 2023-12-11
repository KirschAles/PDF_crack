from pypdf import PdfReader
from argparse import ArgumentParser
from string import digits, ascii_lowercase, ascii_uppercase
from itertools import product

parser = ArgumentParser()
parser.add_argument('filename',
                    help='Path to the pdf file')
parser.add_argument('-n', '--numbers',
                    default=False,
                    const=True,
                    nargs='?',
                    help='Password uses numbers.')
parser.add_argument('-a', '--alphabet',
                    default=False,
                    const=True,
                    nargs='?',
                    help='Password uses alphabet.')
parser.add_argument('-l', '--length',
                    default=4,
                    help='Length of password.')


def main(args):
    filename = args.filename

    used_letters = ''
    if args.numbers:
        used_letters += digits
    if args.alphabet:
        used_letters += ascii_uppercase + ascii_lowercase

    reader = PdfReader(filename)
    for permutation in product(used_letters, repeat=args.length):
        permutation = ''.join(permutation)
        a = reader.decrypt(permutation)
        if a != 0:
            print('Password is: {}'.format(permutation))
            break


if __name__ == '__main__':
    main(parser.parse_args())
