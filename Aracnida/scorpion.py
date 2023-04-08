import argparse

parser = argparse.ArgumentParser(prog='spider', description='Extract imfo from jpg, jpeg, png, gif, bmp, docx and pdf files')

parser.add_argument("file", metavar="FILE", type=str, nargs='+' ,help="Files to extract info")
args = parser.parse_args()

def scorpion(args):
    for file in args.file:
        print(file)

if __name__ == '__main__':
    scorpion(args)