#! /home/cnc/linuxcnc/
#######################################################################
#                                                                     #
#   RRRRRR     OOOOOO   SSSSSS  EEEEEEEE TTTTTTTT TTTTTTTT   AAAA     #
#   RR   RR   OO    OO SS    SS EE          TT       TT     AA  AA    #
#   RR    RR  OO    OO SS       EE          TT       TT    AA    AA   #
#   RR   RR   OO    OO  SS      EE          TT       TT    AA    AA   #
#   RRRRRR    OO    OO   SSSS   EEEEEE      TT       TT    AA    AA   #
#   RR   RR   OO    OO      SS  EE          TT       TT    AAAAAAAA   #
#   RR    RR  OO    OO       SS EE          TT       TT    AA    AA   #
#   RR    RR  OO    OO SS    SS EE          TT       TT    AA    AA   #
#   RR    RR   OOOOOO   SSSSSS  EEEEEEEE    TT       TT    AA    AA   #
#                                                                     #
#######################################################################
#
# LinuxCNC configuration for use with a Rose Engine
#
# File:
#   Backup.sh
#
# Purpose:
#   This backs up the files provided with the system
#
# End User Customisation:
#   THE END USER OF THE ROSETTA SYSTEM SHOULD NOT MODIFY THIS FILE.
#
#   Changes to this file are not supported by Colvin Tools nor
#   Brainwave Embedded.
#
# Version
#   1.0 - dd mmm 2025, R. Colvin
#
# Copyright (c) 2025 Colvin Tools and Brainwave Embedded. 
#
# The following MIT/X Consortium License applies to the Rosetta system.
# Use of this system constitutes consent to the terms outlined below.
#
# Permission is hereby granted, free of charge, to any person obtaining 
# a copy of this software and associated documentation files (the 
# "Software"), to deal in the Software without restriction, including 
# without limitation the rights to use, copy, modify, merge, publish, 
# distribute, sublicense, and/or sell copies of the Software, and to 
# permit persons to whom the Software is furnished to do so, subject to 
# the following conditions:
#
# The above copyright notice and this permission notice shall be 
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, 
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF 
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY 
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, 
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE 
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# Except as contained in this notice, the name of COPYRIGHT HOLDERS
# shall not be used in advertising or otherwise to promote the sale, 
# use or other dealings in this Software without prior written 
# authorization from COPYRIGHT HOLDERS.
#
# ********************************************************************
sSpaces='   '
echo -e "\e[1;33;1;44m>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<\e[0m"
# Backing up files 
#   from /home/cnc/linuxcnc/configs/Rosetta/
#   to /home/cnc/linuxcnc/Backup/Rosetta/
echo -e "\e[0;33;1;44m Backing up files\e[0m"
echo -e "$sSpaces" "\e[0;33;1;44m from /home/cnc/linuxcnc/configs/Rosetta/\e[0m"
echo -e "$sSpaces" "\e[0;33;1;44m to /home/cnc/linuxcnc/Backup/Rosetta/\e[0m"
cd /home/cnc/linuxcnc/Backup/Rosetta/
sudo cp /home/cnc/linuxcnc/configs/Rosetta/*.* .
# Restoring files from /home/cnc/linuxcnc/configs/Rosetta/Rosetta_Axes
# to /home/cnc/linuxcnc/Backup/Rosetta/Rosetta_Axes/
echo -e "\e[0;33;1;44m Backing up files\e[0m"
echo -e "$sSpaces" "\e[0;33;1;44m /home/cnc/linuxcnc/configs/Rosetta/Rosetta_Axes/\e[0m"
echo -e "$sSpaces" "\e[0;33;1;44m to /home/cnc/linuxcnc/Backup/Rosetta/Rosetta_Axes/\e[0m"
cd Rosetta_Axes
sudo cp /home/cnc/linuxcnc/configs/Rosetta/Rosetta_Axes/*.* .
