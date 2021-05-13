import argparse

parser=argparse.ArgumentParser(description='Hihi')
parser.add_argument('--fileconvert', type=str)
parser.add_argument('--convertto', type=str)
args=vars(parser.parse_args())

if args['convertto']:
    print(args['convertto'])
if args['fileconvert']:
    print(args['fileconvert'])