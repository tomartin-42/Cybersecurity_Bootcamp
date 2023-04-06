import extractor
import argparse

description = 'Extract jpg, jpeg, png, gif, bmp, docx and pdf files from a url'

parser = argparse.ArgumentParser(prog='spider', description=description)
parser.add_argument('-r', metavar='URL', required=True, type=str,
                    help='-r download all file in url')
parser.add_argument('-l', type=int, default=99, nargs='?',
                    help='Inser deep lvl. If exclude deep lvl, spider get all files')
parser.add_argument('-p', metavar='PATH', type=str, default='./data/',
                    help='Indicate path where download files')
args = parser.parse_args()

def spider(args):
    if args.l == None:
        args.l = 5
    #print("arg.l ", args.l, "\narg.r ", args.r, "\narg.p ", args.p)
    target = extractor.Extractor(args.r, args.l)
    print("We have found ", len(target.get_list_file()), " files")
    print("visit list ", target.get_visit_list())
    print()
    print("url to visit ", target.get_url_to_visit())
    print()
    print(target.get_list_file())
    

if __name__ == '__main__':
    spider(args)