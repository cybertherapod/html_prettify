import sys
import getopt
from bs4 import BeautifulSoup

def help_output():
    print """
    SYNTAX: python html_prettify.py [OPT] SOURCE_FILE OUTPUT_FILE

    Options:
    -h, --help      Print this output.
    """

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "h", ["help"])
    except getopt.GetoptError:
        help_output()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            help_output()
            sys.exit()

    if len(args) < 2:
        help_output()
        sys.exit(2)
    else:
        inFile = args[0]
        outFile = args[1]

        soup = BeautifulSoup(open(inFile), "html5lib")

        workingFile = open(outFile, 'w')
        workingFile.write(soup.prettify().encode('utf-8'))
        workingFile.close()

if __name__ == "__main__":
    main(sys.argv[1:])
