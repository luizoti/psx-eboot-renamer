import os
import re
import sys
import argparse
from gamenamedb import *

partids = ['SLUS', 'SLPS', 'SLPM', 'SLKA', 'SLES', 'SIPS', 'SCUS', 'SCPS', 'SCES', 'SCED', 'SCAJ', 'LSP', 'HPS', 'ESPM', 'CPCS']

parser = argparse.ArgumentParser()
parser.add_argument("PATH", help="the path of eboot files", type=str)
args = parser.parse_args()

regex = "(?:\_)(S\w{2}S\_\d{5})"

class EbootRename(object):
    """docstring for EbootRename"""
    def __init__(self):
        self.ebootid = ''
        self.ebpaths = []
        self.listfiles()
        self.getebinfo()


    def listfiles(self):
        for file in os.listdir(args.PATH):
            if '.pbp' in file.lower() :
                file = f"{args.PATH}/{file}"
                if file not in self.ebpaths:
                    self.ebpaths.append(file)


    def getebinfo(self):
        for gameeboot in self.ebpaths:
            try:
                with open(gameeboot, "rb") as f:
                    n = 0
                    b = f.read(16)
                    for number in range(0,5000):
                        ac2 = str("".join([chr(i) if 32 <= i <= 127 else "." for i in b])) # ascii string; chained comparison
                        if not ac2.count('.') > 6:
                            if re.search(regex, ac2):
                                self.ebootid = re.findall(regex, ac2)
                                self.ebootid = self.ebootid[0].replace('_', '-')
                                for _id in partids:
                                    for i, n in eval(_id).items():
                                        if i == self.ebootid:
                                            self.rename(n)
                        n += 1
                        b = f.read(16)
            except Exception as e:
                # print(__file__, ": ", type(e).__name__, " - ", e, sep="", file=sys.stderr)
                pass
        
    def rename(self, n):
        print(self.ebootid, n)
        pass

if __name__ == '__main__':
    EbootRename()