#!/usr/bin/python3
import rawpy
# import imageio
import cv2
import time
import os
import tarfile
from tqdm import tqdm

'''
Project Coral module to test processing time of RAW file to different file formats.
Test data losses with different image storage paradigms (.jpeg, .tiff, .png) as well as post-compression
Saved RAW frames will need a regex for automatic processing according to format.
Potentially could add a delete function for original RAW files to minimize storage.
'''


class stopclock():
    def __init__(self):
        self.t = time.time()

    def lap(self, message):
        lap = time.time() - self.t
        print(f'Time to {message}: {lap:.6}')
        self.t = time.time()


def compress(tf, files):
    tar = tarfile.open(tf, mode='w:gz')
    progress = tqdm(files)
    for file in files:
        tar.add(file)
    tar.close()


if __name__ == "__main__":
    suffix = '.png'

    paths = ['001.ARW', '002.ARW', '003.ARW']
    files = [path.split('.')[0]+suffix for path in paths]

    zfile = 'images.zip'

    clock = stopclock()

    for path, file in zip(paths, files):
        with rawpy.imread(path) as raw:
            rgb = raw.postprocess()  # numpy rgb array
            image = cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR)
            cv2.imwrite(file, image)

        clock.lap(
            f'save {path} ({(os.path.getsize(path)/1e6):.3}MB) -> ({(os.path.getsize(file)/1e6):.3}MB)')

    compress(zfile, files)
    clock.lap(f'compress {files}')
