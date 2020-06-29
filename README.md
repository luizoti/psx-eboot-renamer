# psx-eboot-renamer

A python script for mass renaming psx eboots.

The script captures the ID of any correctly converted eboot, and then renames it.

Tested with eboots converted via PSX2PSP.

Database: https://psxdatacenter.com/sitenews.html

# How to use:

´usage: ebootrename.py [-h] [-n] [-id] PATH

positional arguments:
  PATH          the path of eboot files

optional arguments:
  -h, --help    show this help message and exit
  -n, --name    only name
  -id, --idend  id at the end´