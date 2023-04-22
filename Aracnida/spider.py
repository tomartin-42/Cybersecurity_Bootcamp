import extractor
import argparse
import downloader

description = 'Extract jpg, jpeg, png, gif, bmp, docx and pdf files from a url'

parser = argparse.ArgumentParser(prog='spider', description=description)
parser.add_argument('-r', metavar='URL', required=True, type=str,
                    help='-r download recursive files in url')
parser.add_argument('-l', type=int, default=5, nargs='?',
                    help='Inser deep lvl. If exclude deep lvl, spider get all files')
parser.add_argument('-p', metavar='PATH', type=str, default='data/',
                    help='Indicate path where download files')
args = parser.parse_args()

def spider(args):
    if args.l == None:
        args.l = 5
    if args.r:
        args.l = 1
    target = extractor.Extractor(args.r, args.l)
    down = downloader.Downloader(target.file_list, target.visit_list ,args.p)


if __name__ == '__main__':
    spider(args)