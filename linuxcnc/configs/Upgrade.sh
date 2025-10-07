#! /home/cnc/linuxcnc/
#######################################################################
#                    RRRRRR    EEEEEEEE  BBBBBBB 					  #
#                    RR   RR   EE        BB    BB 			   	      #
#                    RR   RR   EE        BB    BB					  #
#                    RRRRRR    EEEEEE    BBBBBBB 					  #
#                    RR   RR   EE        BB    BB					  #
#                    RR    RR  EE        BB    BB					  #
#                    RR    RR  EEEEEEEE  BBBBBBB					  #
#                                                                     #
# Rose Engine Butler                                                  #
#######################################################################
#
# LinuxCNC configuration for use with a Rose Engine
#
# File:
#   Upgrade.sh
#
# Purpose:
#   This updates the files pulled from GitHub.
#
# End User Customisation:
#   THE END USER OF THE ROSE ENGINE BUTLER SYSTEM SHOULD NOT MODIFY
#   THIS FILE.
#
#   Changes to this file are not supported by Colvin Tools nor
#   Brainwave Embedded.
#
# Version
#   1.0 - 05 Oct 2025, R. Colvin
#
# Copyright (c) 2025 Colvin Tools and Brainwave Embedded. 
#
# The following MIT/X Consortium License applies to the Rose Engine
# Butler system.  Use of this system constitutes consent to the terms 
# outlined below.
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
# Copying files 
#   from /home/cnc/Rosetta_LinuxCNC/linuxcnc/configs
#   to /home/cnc/linuxcnc/configs
echo -e "\e[0;33;1;44m Copying files\e[0m"
echo -e "$sSpaces" "\e[0;33;1;44m from /home/cnc/Rosetta_LinuxCNC/linuxcnc/configs\e[0m"
echo -e "$sSpaces" "\e[0;33;1;44m to /home/cnc/linuxcnc/configs\e[0m"
cd /home/cnc/linuxcnc/configs
sudo cp -R /home/cnc/Rosetta_LinuxCNC/linuxcnc/configs/*.* .

sudo cp -R /home/cnc/Rosetta_LinuxCNC/linuxcnc/configs/REB .
sudo cp -R /home/cnc/Rosetta_LinuxCNC/linuxcnc/configs/REB_Images .
sudo cp -R /home/cnc/Rosetta_LinuxCNC/linuxcnc/configs/REB_MesaCard .
sudo cp -R /home/cnc/Rosetta_LinuxCNC/linuxcnc/configs/REB_Setup .

sudo chmod 777 -R /home/cnc/Rosetta_LinuxCNC/linuxcnc/configs/REB
sudo chmod 777 -R /home/cnc/Rosetta_LinuxCNC/linuxcnc/configs/REB_Images
sudo chmod 777 -R /home/cnc/Rosetta_LinuxCNC/linuxcnc/configs/REB_MesaCard
sudo chmod 777 -R /home/cnc/Rosetta_LinuxCNC/linuxcnc/configs/REB_Setup
