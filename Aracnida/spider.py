import getfolder
import argparse

description = 'Extract jpg, jpeg, png, gif, bmp, docx and pdf files from a url'

parser = argparse.ArgumentParser(prog='spider', description=description)
parser.add_argument('-r', action='store_true',
                    help='If -r is present, download all file in url')
parser.add_argument('-l', type=int, default=5,
                    help='Inser deep lvl. If exclude deep lvl, spider get all files')
parser.add_argument('-p', type=str,
                    help='Indicate path where download files')
parser.add_argument('URL', type=str,
                    help='Url from download files')

args = parser.parse_args()


def spider(args):
    print(args)
    pass
