# PSX-Eboot-Renamer

Simple script to rename PSX eboots.

The purpose of this script is to automate the process of renaming large amounts of eboots.

In my tests I did not notice any problems, if you notice, let me know, or correct yourself.

When converting PSX games using PSX2PSP, it generates folder structures like:

SLUS01272/EBOOT.PBP
SCUS94508/EBOOT.PBP
SLES03134/EBOOT.PBP
SLPS01986/EBOOT.PBP

The name of the eboot folder is based on the game code and this code varies by region.
SLPS01986/EBOOT.PBP

The script only rename .pbp files inside folders with the game code, basically it only renames it when it encounters this /SLPSXXXXX/EBOOT.PBP structure.

If the eboot has 2 or more disks, this will be described according to the code described in the folder, for example if a Parasite Eve eboot is identified, and the eboot was created with SLUS from CD2, the name will look like this:

SCPS-45204 PARASITE EVE - [ 2 DISC ]

All multi-disc games have a dedicated SLUS for each CD and each of them is described separately by [ 1 DISC ], [ 2 DISC ], [ 3 DISC ], [ 4 DISC ] end etc.

Run the script in the following two ways, it deletes the folder of each game automatically after you rename the .pbp file.

./ebootrename.sh /folder/with/eboots

OR

~/folder_with_eboots$ /path/to/script/ebootrename.sh .

The list with game names and game codes has been taken from psxdatacenter.

https://psxdatacenter.com/sitenews.html
