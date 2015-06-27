"""
Usage:  ropt [OPTIONS] <url> [REQ-INPUT]

Options:
    -X --request    Specify HTTP request method to use [default: GET]
    --get           Use the HTTP GET request method
    --head          Use the HTTP HEAD request method
    --post          Use the HTTP POST request method
    --put           Use the HTTP PUT request method
    --delete        Use the HTTP DELETE request method
    --trace         Use the HTTP TRACE request method
    --options       Use the HTTP OPTIONS request method
    --connect       Use the HTTP CONNECT request method
"""
from docopt import docopt

def main(args):
    print(args)

if __name__ == '__main__':
    arguments = docopt(__doc__, version='ropt 0.1.0')
    main(arguments)


