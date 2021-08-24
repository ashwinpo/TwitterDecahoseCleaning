import io
import ijson
import glob
import argparse
import multiprocessing
from itertools import islice
import pickle


def separate(infile):
    with open(infile, mode='r', encoding="ISO-8859-1") as f:
        before_error = {
        "prefix": None,
        "type": None,
        "value": None,
        }
        good = 0
        bad = 0

        with open(infile + "_fixed", mode = 'w+') as fw:
            with open(infile + "_error_lines", mode = 'w+') as fwb:
                for line_number, line in enumerate(f):
                    # print ("Processing line", line_number + 1,"at cursor index:", cursor)
                    line_as_file = io.StringIO(line)
                    # Use a new parser for each line
                    json_parser = ijson.parse(line_as_file)
                    try:
                        for prefix, type, value in json_parser:
                            before_error.update({'prefix': prefix, 'type': type, 'value': value})

                        fw.write(line)
                        good += 1
                    except:
                        fwb.write(line)
                        bad += 1


        print(str(bad) + " errors found out of " + str(good + bad) + " lines")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()

    separate(args.filename)


#ashwinpo@cavium-thunderx-login01/nfs/locker/arcts-cavium-hadoop-stage/home/ashwinpo/
