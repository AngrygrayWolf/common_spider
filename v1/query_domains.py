import os
import sys
sys.path.append(os.path.abspath('../'))

from util.util import get_file_domain

from v1.query_main import get_all

from util.query import Query
from util.color import R, W, Y, G


from util import query
import argparse





def banner():
    print("""%s
                                ____                                      
                 / ___|___  _ __ ___  _ __ ___   ___  _ __  
                | |   / _ \| '_ ` _ \| '_ ` _ \ / _ \| '_ \ 
                | |__| (_) | | | | | | | | | | | (_) | | | |
                 \____\___/|_| |_| |_|_| |_| |_|\___/|_| |_|%s%s
                 
                # Coded By AngryGrayWolf
    
    """ % (R, W, Y))


def parser_error(errmsg):
    banner()
    print("Usage: python " + sys.argv[0] + " [Options] use -h for help")
    print(R + "Error: " + errmsg + W)
    sys.exit()


def parse_args():
    # todo: 需要更改参数的设置，更加语义化
    parser = argparse.ArgumentParser(epilog='\tExample: \r\npython ' + sys.argv[0] + " -d 8.8.8.8")
    parser.error = parser_error
    # parser._optionals.title = "OPTIONS"
    parser.add_argument('-d', '--domains', help="Domain name by IP")
    parser.add_argument('--all', action='store_true', help="Get all information by domain")
    parser.add_argument('-i', '--input', help="input files", required=False)


    return parser.parse_args()


def interactive():
    args = parse_args()
    domains = args.domains
    banner()
    if args.input:
        test = get_file_domain('../input/test')
        if args.all:
            for one in test:
                get_all(one[0], one[1].replace('\n', ''))
    elif domains:
        res = Query().get_sub_domains(domains=[domains])
        if res is not None:
            for subdomain in res[domains]:
                print(G + subdomain + W)


if __name__ == '__main__':
    interactive()
