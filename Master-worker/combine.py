import shutil
import glob
import argparse
import re

def combine(outfile):
    with open(outfile,'wb') as wfd:
        files = glob.glob('output/outfile*')
        # Sort the files properly instead of doing 0,1,10,11, etc.
        files = sorted(files, key=lambda x:float(re.findall("(\d+)",x)[0]))
        for f in files:
            print(f)
            with open(f,'rb') as fd:
                shutil.copyfileobj(fd, wfd)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()

    combine(args.filename)
