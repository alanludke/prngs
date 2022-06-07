import csv
import time

from prng.bbs import BBS
from prng.lehmer import Lehmer
from utils.utils import generate

REPS = 100
LIST_OF_BITS = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]

_SEED = int(time.time())

_RESULTS_BBS = []
_RESULTS_LEH = []


def main():

    for s in LIST_OF_BITS:
        bbs = BBS(_SEED, s)
        rst,time = generate(bbs, REPS)
        _RESULTS_BBS.append(bbs)

        leh = Lehmer(_SEED, s)
        rst, time = generate(leh, REPS)
        _RESULTS_LEH.append(leh)

    with open('results.csv', 'w+', newline='') as csv_file:

        csv_file = open('results.csv', 'w+', newline='')
        writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        with open('bbs.txt', 'w+') as txt_file:
            writer.writerow(['Blum Blum Shub'])
            for bbs in _RESULTS_BBS:
                writer.writerow([bbs.s, bbs.time])
                txt_file.write(str(bbs.s) + "\n")
                txt_file.write(bbs.result + "\n\n")

        with open('parkMiller.txt', 'w+') as txt_file:
            writer.writerow(['Park-Miller'])
            for leh in _RESULTS_LEH:
                writer.writerow([leh.s, leh.time])
                txt_file.write(str(leh.s) + "\n")
                txt_file.write(leh.result + "\n\n")

if __name__ == '__main__':
    main()
