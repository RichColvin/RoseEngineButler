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
#   RoseEngineButler_AxisX.inc                                        #
#                                                                     #
# Purpose:                                                            #
#   This is used to setup the X axis for the configuration of         #
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
#    AA    XX    XX IIIIIIII  SSSSSS      YY    YY
#   AAAA    XX  XX    II     SS    SS      YY  YY
#  AA  AA    XXXX     II      SSS           YYYY
# AAAAAAAA   XXXX     II         SSS        XXXX
# AA    AA  XX  XX    II     SS    SS      XX   XX
# AA    AA XX    XX IIIIIIII  SSSSSS      XX     XX
# ********************************************************************

# ********************************************************************
# Configuration values
#                                 Home   PCB
#  Axis  Joint  Channel   Type     Seq  Plug  Comments
#  ----  -----  -------  -------  ----  ----  ------------------------
#   X      0       02    LINEAR     1    P13
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

[AXIS_X]
TYPE                 = LINEAR

MAX_VELOCITY         = 1.0
MAX_ACCELERATION     = 20.0

MIN_LIMIT            = -1e99
MAX_LIMIT            = 1e99

# ********************************************************************
#       JJ  OOOOOO  IIIIIIII N     NN TTTTTTTT
#       JJ OO    OO    II    NN    NN    TT
#       JJ OO    OO    II    NNN   NN    TT
#       JJ OO    OO    II    NN NN NN    TT
# JJ    JJ OO    OO    II    NN  NNNN    TT
#  JJJJJJ   OOOOOO  IIIIIIII NN    NN    TT
# ********************************************************************
[JOINT_0]
TYPE                     = LINEAR

# This over-rides the value specified in [TRAJ]LINEAR_UNITS
UNITS 					 = INCH

# ***********************
# ENCODER_SCALE = number of pulses that corresponds to a move of one
# machine unit.  This is optionally used in PnCconf built configs.
#
# Set to 20,320 steps / in
# ENCODER_SCALE            = 20320

# ***********************

# Specifies the number of pulses that corresponds to a move of one
# machine unit as set in the [TRAJ] section. For stepper systems,
# this is the number of step pulses issued per machine unit. For a
# linear joint one machine unit will be equal to the setting of
# LINEAR_UNITS. For an angular joint one unit is equal to the setting
# in ANGULAR_UNITS. For servo systems, this is the number of feedback
# pulses per machine unit. A second number, if specified, is ignored.
#
# For a linear joint one machine unit will be equal to the setting 
# of LINEAR_UNITS. 
# 
# For an angular joint one unit is equal to the setting in 
# ANGULAR_UNITS. 
#
# See also, calculation #3, above.
#
#   * Stepper systems: this is the number of step pulses issued per
#     machine unit. 
#
#   * Servo systems: this is the number of feedback pulses per
#     machine unit. A second number, if specified, is ignored.
#
# SCALE is specified in Sample configs 
# SCALE                      = 20320
# STEP_SCALE is specified in PnCconf built configs 
STEP_SCALE                 = 2032

# ***********************
# Maximum acceleration for this joint in machine units per second
# squared.
MAX_ACCELERATION           = 30

# ********************************************************************
# STEPGEN_MAXACCEL is USED FOR STEPPER MOTORS - Acceleration limit
# for the step generator. This should be 1% to 10% larger than the
# joint MAX_ACCELERATION. This value improves the tuning of StepGen’s
# "position loop". If you have added backlash compensation to an joint
# then this should be 1.5 to 2 times greater than MAX_ACCELERATION. 
STEPGEN_MAXACCEL           = 2

# ***********************
#
# 10 rev   360 deg   1 min
# ------ x ------- x ------ = 60 deg/sec
#  1 min    1 rev    60 sec
#
# Maximum velocity for this joint in machine units per second.
MAX_VELOCITY           	   = 60

# STEPGEN_MAXVEL is USED FOR STEPPER MOTORS - Older configuration
# files have a velocity limit for the step generator as well. If
# specified, it should also be 1% to 10% larger than the joint
# MAX_VELOCITY. Subsequent testing has shown that use of
# STEPGEN_MAXVEL does not improve the tuning of StepGen’s position
# loop.
STEPGEN_MAXVEL             = 75

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
MIN_LIMIT              = -1e99

# The maximum limit for joint motion, in machine units. When this
# limit is reached, the controller aborts joint motion. For a
# rotary joint with unlimited rotation having no MAX_LIMIT for
# that joint in the [JOINT_N] section a the value 1e99 is used.
MAX_LIMIT              = 1e99

# The value in machine units by which the joint is permitted to
# deviate from commanded position at very low speeds.
MIN_FERROR               = 10

# The maximum allowable following error, in machine units.
FERROR                   = 100

# 1 Indicates the joint is used as a locking indexer.
LOCKING_INDEXER          = 1




# ********************************************************************
# Homing
HOME                 = 0.0
HOME_SEQUENCE        = 1

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
