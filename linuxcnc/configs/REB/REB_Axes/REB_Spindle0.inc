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
#                                                                     #
# LinuxCNC configuration for use with a Rose Engine                   #
#                                                                     #
# File:                                                               #
#   REB_Spindle0.inc                                                  #
#                                                                     #
# Purpose:                                                            #
#   This is used to setup the Spindle 0 axis for the configuration    #
#   of LinuxCNC.                                                      #
#                                                                     #
# End User Customisation: 											  #
#   The end user of the Rose Engine Butler system may modify this     #
#   file to accommodate their local configuration.  It is recommended #
#   that a copy of this file be saved before changes are made.		  #
#																	  #
#   Changes to this file are not supported by Colvin Tools nor		  #
#   Brainwave Embedded.												  #
#                                                                     #
# Version                                                             #
#   1.0 - 09 August 2025, R. Colvin                                   #
#                                                                     #
# Copyright (c) 2025 Colvin Tools and Brainwave Embedded. 			  #
#																	  #
# The following MIT/X Consortium License applies to the Rose Engine   #
# Butler system. Use of this system constitutes consent to the terms  #
# outlined below.													  #
#																	  #
# Permission is hereby granted, free of charge, to any person 		  #
# obtaining a copy of this software and associated documentation 	  #
# files (the "Software"), to deal in the Software without 			  #
# restriction, including without limitation the rights to use, copy,  #
# modify, merge, publish, distribute, sublicense, and/or sell copies  #
# of the Software, and to permit persons to whom the Software is 	  #
# furnished to do so, subject to the following conditions:			  #
#																	  #
# 		The above copyright notice and this permission notice shall   #
# 		be included in all copies or substantial portions of the 	  #
# 		Software.													  #
#																	  #
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, 	  #
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF  #
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND 			  #
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS #
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN  #
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN   #
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE    #
# SOFTWARE.															  #
#																	  #
# Except as contained in this notice, the name of COPYRIGHT HOLDERS	  #
# shall not be used in advertising or otherwise to promote the sale,  #
# use or other dealings in this Software without prior written		  #
# authorization from COPYRIGHT HOLDERS.								  #
#######################################################################

# ********************************************************************
#  SSSSSS  PPPPPPP  IIIIIIII N     NN DDDDDDD  LL       EEEEEEEE   0000
# SS    SS PP    PP    II    NN    NN DD    DD LL       EE        00  00
#  SSS     PP    PP    II    NNN   NN DD    DD LL       EEEEE    00    00
#     SSS  PPPPPPP     II    NN NN NN DD    DD LL       EE       00    00
# SS    SS PP          II    NN  NNNN DD    DD LL       EE        00  00
#  SSSSSS  PP       IIIIIIII NN    NN DDDDDDD  LLLLLLLL EEEEEEEE   0000
# ********************************************************************

# ********************************************************************
# Configuration values
#                                 Home 
#  Axis  Joint  Channel   Type     Seq   Comments
#  ----  -----  -------  -------  ----   ------------------------
#  Sp0     7       05      n/a     n/a 
#  Sp1     6       07      n/a     n/a

[JOINT_7]
SPINDLE              = 0
TYPE                 = ANGULAR

[SPINDLE_0]
TYPE                 = ANGULAR

MAX_VELOCITY         = 10
MAX_ACCELERATION     = 30

# ********************************************************************
# The values used below are based on these calculations.
#
# ***********************
# 1. Stepper motors use 1.8 deg / step.
#
# ***********************
# 2. DM542T set to Microsteps  = 32
#                  Steps / rev = 6,400
#
#   32 microsteps           microsteps
#   -------------  = 17.778 ----------
#      1.8 deg                degree
#
# ********************************************************************
SCALE				 = 57600
STEP_SCALE           = 57600
ENCODER_SCALE        = 6400

STEPGEN_MAXVEL       = 2
STEPGEN_MAXACCEL     = 1

# ********************************************************************
# STANDARD VALUES
#
# These parameters are best left alone

BACKLASH			 = 0.0000

MIN_FERROR           = 0.5
FERROR               = 5

# LOCKING_INDEXER     = 1

BIAS                 = 0.0
DEADBAND             = 0.000015
MAX_OUTPUT           = 10.0

P                    = 1000.0
I                    = 0.0
D                    = 0.0
FF0                  = 1.0
FF1                  = 0.0
FF2                  = 0.0
# ********************************************************************
