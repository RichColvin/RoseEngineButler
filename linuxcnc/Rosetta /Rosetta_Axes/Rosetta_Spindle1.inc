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
#                                                                     #
# LinuxCNC configuration for use with a Rose Engine                   #
#                                                                     #
# File:                                                               #
#   Rosetta_Spindle1.inc                                              #
#                                                                     #
# Purpose:                                                            #
#   This is used to setup the Spindle 1 axis (Rosette Phaser/         #
#   Multiplier) for the configuration of LinuxCNC.                    #
#                                                                     #
# End User Customisation:                                             #
#   The end user of the Rosetta system may modify this file to        #
#   accommodate their local configuration.  It is recommended that    #
#   a copy of this file be saved before changes are made.             #
#                                                                     #
#   Changes to this file are not supported by Colvin Tools nor        #
#   Brainwave Embedded.                                               #
#                                                                     #
# Version                                                             #
#   1.0 - 03 August 2025, R. Colvin                                   #
#                                                                     #
# Copyright (c) 2025 Colvin Tools and Brainwave Embedded.             #
#                                                                     #
# The following MIT/X Consortium License applies to the Rosetta       #
# system. Use of this system constitutes consent to the terms         #
# outlined below.                                                     #
#                                                                     #
# Permission is hereby granted, free of charge, to any person         #
# obtaining a copy of this software and associated documentation      #
# files (the "Software"), to deal in the Software without             #
# restriction, including without limitation the rights to use, copy,  #
# modify, merge, publish, distribute, sublicense, and/or sell copies  #
# of the Software, and to permit persons to whom the Software is      #
# furnished to do so, subject to the following conditions:            #
#                                                                     #
#       The above copyright notice and this permission notice shall   #
#       be included in all copies or substantial portions of the      #
#       Software.                                                     #
#                                                                     #
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,     #
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF  #
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND               #
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS #
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN  #
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN   #
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE    #
# SOFTWARE.                                                           #
#                                                                     #
# Except as contained in this notice, the name of COPYRIGHT HOLDERS   #
# shall not be used in advertising or otherwise to promote the sale,  #
# use or other dealings in this Software without prior written        #
# authorization from COPYRIGHT HOLDERS.                               #
#######################################################################

# ********************************************************************
# Details about the fields are available in the
#   LinuxCNC 2.9.4 System Manual, 
#   https://linuxcnc.org/docs/stable/html/

# ********************************************************************
# Configuration values
#                                 Home 
#  Axis  Joint  Channel   Type     Seq   Comments
#  ----  -----  -------  -------  ----   ------------------------
#  Sp0     7       05      n/a     n/a 
#  Sp1     6       07      n/a     n/a

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
# 3. Spindle gear
#
#    For the MDF Rose Engine, the spindle motor gear ratio is 
#    108:12 = 9
#
#    For the Lindow Rose Engine, the spindle motor gear ratio
#    is
#
#    17.778 microsteps    9 motor rev        microsteps
#    ----------------- x ------------- = 160 -----------
#         1 degree        1 spindle rev      spindle deg
#
# ********************************************************************

# ********************************************************************
#
#       JJ  OOOOOO  IIIIIIII N     NN TTTTTTTT
#       JJ OO    OO    II    NN    NN    TT
#       JJ OO    OO    II    NNN   NN    TT
#       JJ OO    OO    II    NN NN NN    TT
# JJ    JJ OO    OO    II    NN  NNNN    TT
#  JJJJJJ   OOOOOO  IIIIIIII NN    NN    TT
#
# ********************************************************************
[JOINT_6]
SPINDLE                  = 1
TYPE                     = ANGULAR

# ********************************************************************
#
#  SSSSSS  PPPPPPP  IIIIIIII N     NN DDDDDDD  LL       EEEEEEEE
# SS    SS PP    PP    II    NN    NN DD    DD LL       EE
#  SSS     PP    PP    II    NNN   NN DD    DD LL       EEEEE
#     SSS  PPPPPPP     II    NN NN NN DD    DD LL       EE
# SS    SS PP          II    NN  NNNN DD    DD LL       EE
#  SSSSSS  PP       IIIIIIII NN    NN DDDDDDD  LLLLLLLL EEEEEEEE 
#
# ********************************************************************
[SPINDLE_1]
TYPE                     = ANGULAR

# The maximum spindle speed (in rpm) for the specified spindle.
MAX_FORWARD_VELOCITY     = 10
MIN_FORWARD_VELOCITY     = 0.0

MAX_REVERSE_VELOCITY     = 10
MIN_REVERSE_VELOCITY     = 0.0

# Sets the step size for spindle speed increment / decrement commands.
INCREMENT                = 0.1

# ********************************************************************
# For the Stepper Online DM542T Drivers
# These are 5 μs = 5,000 ns
DIRHOLD                  = 5000
DIRSETUP                 = 5000
# These are 2.5 μs = 2,500 ns
STEPLEN                  = 2500
STEPSPACE                = 2500

# ***********************
# ENCODER_SCALE = number of pulses that corresponds to a move of one
# machine unit.
#
# See also, calculation #3, above.
ENCODER_SCALE            = 160

# ***********************
# STEP_SCALE = number of pulses that corresponds to a move of one 
# machine unit as set in the [TRAJ] section. 
#
# See also, calculation #3, above.
#
# For a linear joint one machine unit will be equal to the setting 
# of LINEAR_UNITS. 
# 
# For an angular joint one unit is equal to the setting in 
# ANGULAR_UNITS. 
#
# For stepper systems, this is the number of step pulses issued per
# machine unit. 
#
# For servo systems, this is the number of feedback pulses per machine
# unit. A second number, if specified, is ignored.
#
SCALE				  = 160
STEP_SCALE            = 160

# ***********************
# Maximum acceleration for this joint in machine units per second
# squared.
MAX_ACCELERATION         = 30

# 10%+ higher than MAX_VELOCITY (in the [SPINDLE_x] section, below)
STEPGEN_MAXACCEL         = 37.5

# ***********************
#
# 10 rev   360 deg   1 min
# ------ x ------- x ------ = 60 deg/sec
#  1 min    1 rev    60 sec
#
# Maximum velocity for this joint in machine units per second.
MAX_VELOCITY           	 = 60

# 10%+ higher than MAX_VELOCITY (in the [SPINDLE_x] section, below)
STEPGEN_MAXVEL           = 75

# ********************************************************************
# Backlash in machine units. Backlash compensation value can be used 
# to make up for small deficiencies in the hardware used to drive an 
# joint. If backlash is added to an joint and you are using steppers 
# the STEPGEN_MAXACCEL must be increased to 1.5 to 2 times the 
# MAX_ACCELERATION for the joint. Excessive backlash compensation
# can cause an joint to jerk as it changes direction.
BACKLASH				 = 0.0000

#  The minimum limit for joint motion, in machine units. When this
# limit is reached, the controller aborts joint motion. For a
# rotary joint with unlimited rotation having no MIN_LIMIT for
# that joint in the [JOINT_N] section a the value -1e99 is used.
# Not used for spindles
# MIN_LIMIT              = -1e99

# The maximum limit for joint motion, in machine units. When this
# limit is reached, the controller aborts joint motion. For a
# rotary joint with unlimited rotation having no MAX_LIMIT for
# that joint in the [JOINT_N] section a the value 1e99 is used.
# Not used for spindles
# MAX_LIMIT              = 1e99

# The value in machine units by which the joint is permitted to
# deviate from commanded position at very low speeds.
MIN_FERROR               = 0.5

# The maximum allowable following error, in machine units.
FERROR                   = 5

# 1 Indicates the joint is used as a locking indexer.
LOCKING_INDEXER          = 1

# ********************************************************************
# SERVO MOTOR SETTINGS
#
# These parameters are not relevant to joints controlled by stepper
# motors; they are only needed when using servo motors

BIAS                     = 0.0

DEADBAND                 = 0.000015

# The maximum value for the output of the PID compensation that is 
# written to the motor amplifier, in volts. The computed output value 
# is clamped to this limit. The limit is applied before scaling to raw
# output units. The value is applied symmetrically to both the plus
# and the minus side.
MAX_OUTPUT               = 10.0

P                        = 1000.0
I                        = 0.0
D                        = 0.0
FF0                      = 1.0
FF1                      = 0.0
FF2                      = 0.0
