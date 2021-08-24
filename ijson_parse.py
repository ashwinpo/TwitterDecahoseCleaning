import io
import ijson
import glob
import argparse

def parse_json(filename):
    with open(filename, encoding="UTF-8") as json_file:
        cursor = 0
        before_error = {
        "prefix": None,
        "type": None,
        "value": None,
        }
        for line_number, line in enumerate(json_file):
            print ("Processing line", line_number + 1,"at cursor index:", cursor)
            line_as_file = io.StringIO(line)
            # Use a new parser for each line
            json_parser = ijson.parse(line_as_file)
            try:
                for prefix, type, value in json_parser:
                    before_error.update({'prefix': prefix, 'type': type, 'value': value})
            except:
                print("Error on line ", line_number)
                print("Last parse: ", before_error)
            cursor += len(line)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()

    parse_json(args.filename)


#ashwinpo@cavium-thunderx-login01/nfs/locker/arcts-cavium-hadoop-stage/home/ashwinpo/
