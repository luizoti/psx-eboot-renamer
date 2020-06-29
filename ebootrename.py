import os
import re
import sys
import argparse
from gamenamedb import *

partids = ['SLUS',
            'SLPS',
             'SLPM',
              'SLKA',
               'SLES',
                'SIPS',
                 'SCUS',
                  'SCPS',
                   'SCES',
                    'SCED',
                     'SCAJ',
                      'LSP',
                       'HPS',
                        'ESPM',
                         'CPCS']

parser = argparse.ArgumentParser()
parser.add_argument("PATH", help="the path of eboot files", type=str)
parser.add_argument("-n", "--name", help="only name", action="store_true")
parser.add_argument("-id", "--idend", help="id at the end", action="store_true")
args = parser.parse_args()

regex = "(?:\_)((?:S|L|H|E|C).+?(?:S|M|A|D|J|P|M)\_\d{5})"

class EbootRename(object):
    """docstring for EbootRename"""
    def __init__(self):
        self.ebootid = ''
        self.ebpaths = []
        self.listfiles()
        self.getebinfo()


    def listfiles(self):
        for file in os.listdir(args.PATH):
            if '.pbp' in file.lower():
                file = os.path.join(args.PATH, file)
                if file not in self.ebpaths:
                    self.ebpaths.append(file)


    def getebinfo(self):
        for gameeboot in self.ebpaths:
            self.ebfilepath = gameeboot
            try:
                with open(gameeboot, "rb") as ebfile:
                    for number in range(0,50000):
                        ac2 = str("".join([chr(i) if 32 <= i <= 127 else "." for i in ebfile.read(16)])) # ascii string; chained comparison
                        if not ac2.count('.') > 6:
                            if re.search(regex, ac2):
                                self.ebootid = re.findall(regex, ac2)
                                self.ebootid = self.ebootid[0].replace('_', '-')
                                for _id in partids:
                                    for gid, name in eval(_id).items():
                                        self.gid = gid
                                        self.name = name
                                        if self.gid == self.ebootid:
                                            self.rename()
            except Exception as e:
                pass
        
    def rename(self):
        gameid = self.ebootid
        gamename = self.name

        if not args.name or args.idend:
            dest_name = f'[{gameid}] {gamename}'
            pass

        if args.name:
            dest_name = f'{self.name}'
        if args.idend:
            dest_name = f'{self.name} [{gameid}]'
            pass
            
        if not self.ebfilepath == os.path.join(args.PATH, dest_name + '.PBP'):
            print("OLD NAME: " + self.ebfilepath)
            print("NEW NAME: " + os.path.join(args.PATH, dest_name + '.PBP'))
            print("")
            os.rename(self.ebfilepath, os.path.join(args.PATH, dest_name + '.PBP'))
            pass
        pass

if __name__ == '__main__':
    EbootRename()