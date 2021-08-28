# Twitter Decahose Cleaning
This repository contains the scripts and testing files used to clean Michigan's Twitter Decahose json files.

## Master-Worker

This folder contains code relevant to the Master-Worker framework constructed to deal with files that have no linebreaks between "tweet" entities.


Usage master-worker-ray.py <input_filename>

**master-worker.py** simply leverages multiprocessing and we were able to achieve decent performance with it.The script reads in chunks of characters and searches for strings denoting the start of a new "tweet" entity. Each worker cleans it's chunks and writes to an output file in **output** dir.

Usage: master-worker.py <input_filename>


**combine.py** takes the **output** dir and combines it back into a single file while maintaining the ordering of the initial file.

Usage: combine.py <final_output_filename>

**master-worker-ray.py** leverages the [ray module](https://ray.io/). We were not able to get the module on Cavium, so the script was not used in production. It has been tested locally, though, and works the same as **master-worker.py**

## Separator

This folder contains code relevant to a separator script constructed to deal with files that: 
 - have new lines between "tweet" entities
 - have randomly distributed lines that contain invalidly formatted json entities
 
 The output are two files: <input_file>_fixed and <input_file>_error_lines which contain only clean / error lines respectively.
 
 **separator/sub1** is an example file with the above properties.
 
 ## Parsing
Running ijson_parse.py is a lightweight parser that checks each line for correct json format. I usually check the head & tail of a file, and then run this parser for a few minutes to sufficiently check a file.

Usage: ijson_parse.py <input_filename>
