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
#   REB_AxisU.inc                                                     #
#                                                                     #
# Purpose:                                                            #
#   This is used to setup the U axis for the configuration of         #
#   LinuxCNC.                                                         #
#                                                                     #
# End User Customisation: 											  #
#   The end user of the Rose Engine Butler system may modify this     #
#   file to accommodate their local configuration.  It is recommended #
#   that a copy of this file be saved before changes are made.		  #
#                                                                     #
#   Changes to this file are not supported by Colvin Tools nor        #
#   Brainwave Embedded.                                               #
#                                                                     #
# Version                                                             #
#   1.0 - 09 October 2025, R. Colvin                                  #
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
#    AA    XX    XX IIIIIIII  SSSSSS      UU    UU
#   AAAA    XX  XX    II     SS    SS     UU    UU
#  AA  AA    XXXX     II      SSS         UU    UU
# AAAAAAAA   XXXX     II         SSS      UU    UU
# AA    AA  XX  XX    II     SS    SS     UU    UU
# AA    AA XX    XX IIIIIIII  SSSSSS       UUUUUU
# ********************************************************************

# ********************************************************************
# Configuration values
#                                 Home   PCB
#  Axis  Joint  Channel   Type     Seq  Plug  Comments
#  ----  -----  -------  -------  ----  ----  ------------------------
#   U      4       04    LINEAR     5    P15
# ********************************************************************

# ********************************************************************
[AXIS_U]
TYPE                 = LINEAR

# 1"/min = 0.083"/sec
MAX_VELOCITY         = 0.1
MAX_ACCELERATION     = 20.0

MIN_LIMIT            = -1e99
MAX_LIMIT            = 1e99

# ********************************************************************
[JOINT_4]
TYPE                 = LINEAR
UNITS 				 = INCH

MAX_VELOCITY         = 0.1
MAX_ACCELERATION     = 20.0

# ********************************************************************
# STEPPER MOTOR SETTINGS
#
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
# ***********************
# 3. Leadscrew
#
#    For the this device, a leadscrew with a 
#       * single start
#       * 2mm pitch
#    Thusly, 1 rev = 2 mm movement
#
#                6,400 steps   1 rev         steps
#   STEP_SCALE = ----------- * ----- = 3,200 -----
#                   1 rev      2 mm           mm
#
#                3,200 steps   25.4 mm          steps
#   STEP_SCALE = ----------- * ------- = 81,280 -----
#                   1 mm       1 inch           inch
# ********************************************************************

# SCALE                = 81280
STEP_SCALE           = 81280
ENCODER_SCALE        = 81280

STEPGEN_MAXACCEL     = 0.5
STEPGEN_MAXVEL       = 1.25

# ********************************************************************
# STANDARD VALUES
#
# These parameters are best left alone

BACKLASH			 = 0.0000

MIN_LIMIT            = -1e99
MAX_LIMIT            = 1e99

MIN_FERROR           = 0.05
FERROR               = 0.5

HOME                 = 0.0
HOME_SEQUENCE        = 5

# LOCKING_INDEXER	   = 1

BIAS                 = 0.0
DEADBAND             = 0.00005
MAX_OUTPUT           = 10.0
OUTPUT_SCALE		 = 1.000
OUTPUT_OFFSET		 = 0.000

P                    = 100.0
I                    = 0.0
D                    = 0.0
FF0                  = 1.0
FF1                  = 1.0
FF2                  = 0.0

# For the StepperOnline DM542T Digital Stepper Drive 
# These are 5 μs = 5,000 ns
DIRHOLD              = 5000
DIRSETUP             = 5000
# These are 2.5 μs = 2,500 ns
STEPLEN              = 2500
STEPSPACE            = 2500
# ********************************************************************
