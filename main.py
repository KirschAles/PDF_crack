from pypdf import PdfReader
import sys


def main():
    filename = sys.argv[1]
    reader = PdfReader(filename)
    for num in range(10000):
        a = reader.decrypt('{0:04d}'.format(num))
        if a != 0:
            print('Password is: {0:04d}'.format(num))


if __name__ == '__main__':
    main()
