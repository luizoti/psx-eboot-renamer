import os
import re
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("PATH", help="the path of eboot files", type=str)
args = parser.parse_args()


class EbootRename(object):
    """docstring for EbootRename"""
    def __init__(self):
        self.ebootid = ''
        self.ebpaths = []
        self.listfiles()
        self.getid()


    def listfiles(self):
        for file in os.listdir(args.PATH):
            if '.pbp' in file.lower() :
                file = args.PATH + file
                if file not in self.ebpaths:
                    self.ebpaths.append(file)


    def getid(self):
        for gameeboot in self.ebpaths:
            try:
                with open(gameeboot, "rb") as f:
                    n = 0
                    b = f.read(16)

                    for x in range(0,5000):
                        ac2 = str("".join([chr(i) if 32 <= i <= 127 else "." for i in b])) # ascii string; chained comparison

                        if not '................' in ac2:
                            if re.search("\_S\w{2}S\_\d{5}", ac2):
                                self.ebootid = re.findall("\_S\w{2}S\_\d{5}", ac2)
                                self.showname()

                        n += 1
                        b = f.read(16)
            except Exception as e:
                print(__file__, ": ", type(e).__name__, " - ", e, sep="", file=sys.stderr)
                pass
        
    def showname(self):
        print(self.ebootid)
        pass

if __name__ == '__main__':
    EbootRename()
