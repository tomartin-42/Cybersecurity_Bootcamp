import extractor
import argparse
import downloader

description = 'Extract jpg, jpeg, png, gif, bmp, docx and pdf files from a url'

parser = argparse.ArgumentParser(prog='spider', description=description)
parser.add_argument('URL', metavar='URL', type=str, help='URL to scrape')
parser.add_argument('-r', help='-r download recursive files in url',
                    action='store_true')
parser.add_argument('-l', type=int, default=99, nargs='?',
                    help='Inser deep lvl. If exclude deep lvl, spider get all files')
parser.add_argument('-p', metavar='PATH', type=str, default='data/',
                    help='Indicate path where download files')
args = parser.parse_args()

def spider(args):
    if args.l == None:
        args.l = 99 
    if not args.r:
        args.l = 1
    target = extractor.Extractor(args.URL, args.l)
    down = downloader.Downloader(target.file_list, target.visit_list ,args.p)


if __name__ == '__main__':
    spider(args)