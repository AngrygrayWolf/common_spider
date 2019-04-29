import sys

from util import query
import argparse

Query = query.Query()
is_windows = sys.platform.startswith('win')

# Console Colors
if is_windows:
    # Windows deserves coloring too :D
    G = '\033[92m'  # green
    Y = '\033[93m'  # yellow
    B = '\033[94m'  # blue
    R = '\033[91m'  # red
    W = '\033[0m'  # white
    try:
        import win_unicode_console, colorama

        win_unicode_console.enable()
        colorama.init()
        # Now the unicode will work ^_^
    except:
        print("[!] Error: Coloring libraries not installed, no coloring will be used [Check the readme]")
        G = Y = B = R = W = G = Y = B = R = W = ''


else:
    G = '\033[92m'  # green
    Y = '\033[93m'  # yellow
    B = '\033[94m'  # blue
    R = '\033[91m'  # red
    W = '\033[0m'  # white


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
    parser = argparse.ArgumentParser(epilog='\tExample: \r\npython sys.argv[0] + "-d 8.8.8.8"')
    parser.error = parser_error
    parser._optionals.title = "OPTIONS"
    parser.add_argument('-d', '--domains', help="Domain name by IP", required=True)

    return parser.parse_args()


def interactive():
    args = parse_args()
    ip = args.domains
    banner()
    res = Query.get_domains(ip=ip)


if __name__ == '__main__':
    interactive()
