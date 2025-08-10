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
#   Rosetta_Spindle0.inc                                              #
#                                                                     #
# Purpose:                                                            #
#   This is used to setup the Spindle 0 axis for the configuration    #
#   of LinuxCNC.                                                      #
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
#   1.0 - 08 August 2025, R. Colvin                                   #
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
# ********************************************************************

# ********************************************************************
#       JJ  OOOOOO  IIIIIIII N     NN TTTTTTTT
#       JJ OO    OO    II    NN    NN    TT
#       JJ OO    OO    II    NNN   NN    TT
#       JJ OO    OO    II    NN NN NN    TT
# JJ    JJ OO    OO    II    NN  NNNN    TT
#  JJJJJJ   OOOOOO  IIIIIIII NN    NN    TT
# ********************************************************************
[JOINT_7]
SPINDLE                  = 0
TYPE                     = ANGULAR

# ********************************************************************
#  SSSSSS  PPPPPPP  IIIIIIII N     NN DDDDDDD  LL       EEEEEEEE
# SS    SS PP    PP    II    NN    NN DD    DD LL       EE
#  SSS     PP    PP    II    NNN   NN DD    DD LL       EEEEE
#     SSS  PPPPPPP     II    NN NN NN DD    DD LL       EE
# SS    SS PP          II    NN  NNNN DD    DD LL       EE
#  SSSSSS  PP       IIIIIIII NN    NN DDDDDDD  LLLLLLLL EEEEEEEE 
# ********************************************************************
[SPINDLE_0]
TYPE                     = ANGULAR

# ********************************************************************
# STEP_SCALE = number of pulses that corresponds to a move of one 
# machine unit as set in the [TRAJ] section. 
#
#   For the MDF Rose Engine,
#
#	         9 motor rev
#   	    ------------- x 6,400 = 57,600
#           1 spindle rev
#
SCALE				     = 57600
STEP_SCALE               = 57600

# ***********************
# ENCODER_SCALE = number of pulses that corresponds to a move of one
# machine unit.
#
# Set to 6400 steps / rev
ENCODER_SCALE            = 6400

# ********************************************************************
# Sets the step size for spindle speed increment / decrement commands.
# INCREMENT                = 0.1

# The maximum spindle speed (in rpm) for the specified spindle.
# The rosette phaser / multiplier needs to be able to run up to 10x the
# spindle speed.
MAX_VELOCITY           	 = 10
# MAX_FORWARD_VELOCITY     = 10
# MAX_REVERSE_VELOCITY     = 10

# Hardware StepGen requires values in rps (revolution per second)
# As it should be 10%+ higher than MAX_VELOCITY, it is set to 20
STEPGEN_MAXVEL           = 2

# Maximum acceleration for this joint in machine units per second
# squared.
MAX_ACCELERATION         = 30

# Hardware StepGen requires values in rps (revolution per second)
# As it should be 10%+ higher than MAX_ACCELERATION, it is set to 1
STEPGEN_MAXACCEL         = 1

# ********************************************************************
# Backlash in machine units.
BACKLASH				 = 0.0000

# The value in machine units by which the joint is permitted to
# deviate from commanded position at very low speeds.
MIN_FERROR               = 0.5

# The maximum allowable following error, in machine units.
FERROR                   = 5

# 1 Indicates the joint is used as a locking indexer.
LOCKING_INDEXER          = 1

# ********************************************************************
# STEPPER MOTOR SETTINGS
#
# These parameters are relevant to joints controlled by stepper
# motors; they may not be needed when using servo motors

# ***********************
# For the Stepper Online DM542T Drivers
# These are 5 μs = 5,000 ns
DIRHOLD                  = 5000
DIRSETUP                 = 5000
# These are 2.5 μs = 2,500 ns
STEPLEN                  = 2500
STEPSPACE                = 2500
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
