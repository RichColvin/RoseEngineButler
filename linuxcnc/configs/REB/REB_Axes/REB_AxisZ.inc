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
#   REB_AxisZ.inc                                                     #
#                                                                     #
# Purpose:                                                            #
#   This is used to setup the Z axis for the configuration of         #
#   LinuxCNC.                                                         #
#                                                                     #
# End User Customisation: 											  #
#   The end user of the Rose Engine Butler system may modify this     #
#   file to accommodate their local configuration.  It is recommended #
#   that a copy of this file be saved before changes are made.		  #
#																	  #
#   Changes to this file are not supported by Colvin Tools nor		  #
#   Brainwave Embedded.												  #
#																	  #
# Version                                                             #
#   1.0 - 08 August 2025, R. Colvin                                   #
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
#    AA    XX    XX IIIIIIII  SSSSSS      ZZZZZZZZ
#   AAAA    XX  XX    II     SS    SS          ZZ
#  AA  AA    XXXX     II      SSS             ZZ
# AAAAAAAA   XXXX     II         SSS        ZZ
# AA    AA  XX  XX    II     SS    SS      ZZ
# AA    AA XX    XX IIIIIIII  SSSSSS      ZZZZZZZZ
# ********************************************************************

# ********************************************************************
# Configuration values
#                                 Home   PCB
#  Axis  Joint  Channel   Type     Seq  Plug  Comments
#  ----  -----  -------  -------  ----  ----  ------------------------
#   Z      2       00    LINEAR     3    P11
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
# ***********************
# 3. Leadscrew
#
#    For the this device, a leadscrew with a 4-start, 2mm pitch
#    is being used = 8mm / rev
#
#                6,400 step   1 rev   25.4 mm          steps
#   STEP_SCALE = ---------- * ----- * ------- = 20,320 -----
#                  1 rev      8 mm     1 inch           inch
# ********************************************************************

[AXIS_Z]
# *******************
TYPE                 = LINEAR

MAX_VELOCITY         = 1.0
MAX_ACCELERATION     = 20.0

MIN_LIMIT            = -1e99
MAX_LIMIT            = 1e99

[JOINT_2]
TYPE                 = LINEAR
UNITS 				 = INCH

MAX_ACCELERATION     = 30
MAX_VELOCITY         = 60

BACKLASH			 = 0.0000

MIN_LIMIT            = -1e99
MAX_LIMIT            = 1e99

MIN_FERROR           = 10
FERROR               = 100

HOME                 = 0.0
HOME_SEQUENCE        = 1

# LOCKING_INDEXER	   = 1

# ********************************************************************
# STEPPER MOTOR SETTINGS
#
# These parameters are only needed when using stepper motors.  They
# are not relevant to joints controlled by servo motors.

SCALE                = 20320
STEP_SCALE           = 20320
ENCODER_SCALE        = 20320

STEPGEN_MAXACCEL     = 3.0
STEPGEN_MAXVEL       = 1.5

# For the DM542T, these are 5 μs = 5,000 ns
DIRHOLD              = 5000
DIRSETUP             = 5000
# For the DM542T, these are 2.5 μs = 2,500 ns
STEPLEN              = 2500
STEPSPACE            = 2500
# ********************************************************************

# ********************************************************************
# UU    UU N     NN UU    UU  SSSSSS  EEEEEEEE DDDDDDD
# UU    UU NN    NN UU    UU SS    SS EE       DD    DD
# UU    UU NNN   NN UU    UU  SSS     EEEEE    DD    DD    
# UU    UU NN NN NN UU    UU     SSS  EE       DD    DD
# UU    UU NN  NNNN UU    UU SS    SS EE       DD    DD
#  UUUUUU  NN    NN  UUUUUU   SSSSSS  EEEEEEEE DDDDDDD
# ********************************************************************

# ********************************************************************
# SERVO MOTOR SETTINGS
#
# These parameters are not relevant to joints controlled by stepper
# motors; they are only needed when using servo motors

# BIAS                     = 0.0

# DEADBAND                 = 0.000015

# The maximum value for the output of the PID compensation that is 
# written to the motor amplifier, in volts. The computed output value 
# is clamped to this limit. The limit is applied before scaling to raw
# output units. The value is applied symmetrically to both the plus
# and the minus side.
# MAX_OUTPUT               = 10.0

# P                        = 1000.0
# I                        = 0.0
# D                        = 0.0
# FF0                      = 1.0
# FF1                      = 0.0
# FF2                      = 0.0
# ********************************************************************
