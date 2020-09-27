#!/usr/bin/python3
import rawpy
import imageio
import time
import os

'''
Project Coral module to test processing time of RAW file to different file formats.
Test data losses with different image storage paradigms (.jpeg, .tiff, .png) as well as post-compression
Saved RAW frames will need a regex for automatic processing.
Potentially could add a delete function for original files to minimize storage
'''


class stopclock():
    def __init__(self):
        self.t = time.time()

    def lap(self, message):
        lap = time.time() - self.t
        print(f'Time to {message}: {lap:.6}')
        self.t = time.time()


if __name__ == "__main__":
    paths = ['001.ARW', '002.ARW', '003.ARW']
    files = [path.split('.')[0]+'.tiff' for path in paths]

    clock = stopclock()

    for path in paths:
        with rawpy.imread(path) as raw:
            rgb = raw.postprocess()
            imageio.imsave(f'001.tiff', rgb)

        clock.lap(f'save {path}')
