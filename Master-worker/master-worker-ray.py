import re
import argparse
import multiprocessing
import ray

def master(infile):
    # Take fileinput
    # Split based on length and num_workers
    l = 10000 # chunk length
    num_workers=3
    with open(infile, mode='r') as f:
        count = 0
        first_char = f.read(1)
        while first_char != '':
            #workers = []
            chunk = first_char + f.read(l)
            outfile = "output/outfile" + str(count)
            count+=1
            #workers.append(multiprocessing.Process(target=worker, args=(chunk, outfile, )))
            worker.remote(chunk, outfile)

            first_char = f.read(1)

    print("Done!")

@ray.remote
def worker(chunk, outfile):
    #created = re.compile("{\"created_at\":\"[^\"]*\",\"id")
    #delete = re.compile("{\"delete")
    if len(chunk) == 0:
        return
    created = re.search("}{\"created_at\":\"[^\"]*\",\"id", chunk)
    deleted = re.search("}{\"delete", chunk)
    start = 0
    if deleted is not None:
        if created is None:
            start = deleted.start()
        else:
            if created.start() < deleted.start():
                start = created.start()
            else:
                start = deleted.start()
    else:
        if created is None:
            with open(outfile, mode='w+') as fw:
                fw.write(chunk)
            return
        start = created.start()

    print(start)
    with open(outfile, mode='w+') as fw:
        # Account for closed brace at start of regex
        if start > 0:
            start = start+1
        fw.write(chunk[0:start])
        fw.write('\n')
        count = 0
        for c in chunk[start:]:
            fw.write(c)
            if c == '{':
              count+=1
            elif c == '}':
              count-=1
              if count == 0:
                fw.write('\n')



if __name__ == '__main__':
    ray.init()
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    outfile = args.filename + '.fixed'
    master(args.filename)
