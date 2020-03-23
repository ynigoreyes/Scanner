from Scanner import Scanner
from pathlib import Path

import sys

def main():
    fileArg = sys.argv[1]
    path = Path('.')
    filePath = path / fileArg

    with open(filePath) as f:
        content = f.read()
        try:
            tokens = Scanner.scan(content)
            print(tokens)
        except:
            print('error')

if __name__ == '__main__':
    main()