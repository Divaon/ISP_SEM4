#!/usr/bin/python3 
import argparse
import Parser.Serializer as Serializer
import os.path

def Check():
    if filetag!='JSON' and filetag!='TOML' and filetag!='PICLE':
        print("Unsuported file format")
        exit()
    elif newformat!='JSON' and newformat!='TOML' and newformat!='PICLE':
        print("Unsuported convert format")
        exit()
    return

parser=argparse.ArgumentParser(description='Hihi')
parser.add_argument('--f', type=str)
parser.add_argument('--c', type=str)
args=vars(parser.parse_args())
filepath=args['f']
filetags=filepath.split('.')
filetag=filetags[-1]
filetag=filetag.upper()
newformat=args['c']
newformat=newformat.upper()
filetags=filetags[:-1]
filetags.append('.'+newformat.lower())
filepath2= ''.join(filetags)
Check()
if not os.path.exists(filepath):
    print("File not founded")
    exit()
if not os.path.exists(filepath2):
    print("File2 not founded")
    if filetag!='PICLE':
        myFile = open(filepath2, "w")
    else:
        myFile = open(filepath2, "wb")
    myFile.close
if filetag==newformat:
    print("File format equal new format")
    exit()
converfromfile=Serializer.CreateDesirializator()
converttofile=Serializer.CreateSirializator( )
obj=converfromfile.deserialize(filetag, filepath)
converttofile.serialize(obj, newformat, filepath2)



