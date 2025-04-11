#! /home/cnc/linuxcnc/
# ##################################################
# Rosetta Application
#
# This restores the files provided with the system
#    2025-04-01 - R. Colvin - initial file
# ##################################################
# 
sSpaces='   '
echo -e "\e[1;33;1;44m>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<\e[0m"
# Restoring files for /home/cnc/linuxcnc/configs/Rosetta/
echo -e "\e[0;33;1;44m Restoring files\e[0m"
echo -e "$sSpaces" "\e[0;33;1;44m from /home/cnc/linuxcnc/Backup/Rosetta/\e[0m"
echo -e "$sSpaces" "\e[0;33;1;44m to /home/cnc/linuxcnc/configs/Rosetta/\e[0m"
cd /home/cnc/linuxcnc/configs/Rosetta/
sudo cp /home/cnc/linuxcnc/Backup/Rosetta/*.* .
# Restoring files for /home/cnc/linuxcnc/configs/Rosetta/Rosetta_Axes
echo -e "\e[0;33;1;44m Restoring files\e[0m"
echo -e "$sSpaces" "\e[0;33;1;44m from /home/cnc/linuxcnc/Backup/Rosetta/Rosetta_Axes/\e[0m"
echo -e "$sSpaces" "\e[0;33;1;44m to /home/cnc/linuxcnc/configs/Rosetta/Rosetta_Axes/\e[0m"
cd Rosetta_Axes
sudo cp /home/cnc/linuxcnc/Backup/Rosetta/Rosetta_Axes/*.* .
