# Twitter Decahose Cleaning
This repository contains the scripts and testing files used to clean Michigan's Twitter Decahose json files.

## Master-Worker

This folder contains code relevant to the Master-Worker framework constructed to deal with files that have no linebreaks between "tweet" entities.

## Separator

This folder contains code relevant to a separator script constructed to deal with files that: 
 - have new lines between "tweet" entities
 - have randomly distributed lines that contain invalidly formatted json entities
 
 The output are two files: <input_file>_fixed and <input_file>_error_lines which contain only clean / error lines respectively.
 
 **sub1** is an example file with the above properties.
