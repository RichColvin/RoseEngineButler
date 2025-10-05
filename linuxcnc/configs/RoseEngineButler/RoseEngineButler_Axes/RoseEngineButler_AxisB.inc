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
#   RoseEngineButler_AxisB.inc                                        #
#                                                                     #
# Purpose:                                                            #
#   This is used to setup the B axis for the configuration of         #
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
#																	  #
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
#    AA    XX    XX IIIIIIII  SSSSSS      BBBBBBB
#   AAAA    XX  XX    II     SS    SS     BB    BB
#  AA  AA    XXXX     II      SSS         BBBBBBB
# AAAAAAAA   XXXX     II         SSS      BB    BB
# AA    AA  XX  XX    II     SS    SS     BB    BB
# AA    AA XX    XX IIIIIIII  SSSSSS      BBBBBBB
# ********************************************************************

# ********************************************************************
# Configuration values
#                                 Home   PCB
#  Axis  Joint  Channel   Type     Seq  Plug  Comments
#  ----  -----  -------  -------  ----  ----  ------------------------
#   B      3       06    ANGULAR    4    P17
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
# ********************************************************************

[AXIS_B]
TYPE                 = ANGULAR

MAX_VELOCITY         = 1.0
MAX_ACCELERATION     = 20.0

MIN_LIMIT            = -1e99
MAX_LIMIT            = 1e99

[JOINT_3]

# ***********************
# ENCODER_SCALE = number of pulses that corresponds to a move of one
# machine unit.
#
# Set to 6400 steps / rev
# ENCODER_SCALE            = 6400

# ***********************
# STEP_SCALE = number of pulses that corresponds to a move of one 
# machine unit as set in the [TRAJ] section. 
#
# See also, calculation #2, above.
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
# ***** Commented out new settign
SCALE				     = 17.778
# STEP_SCALE               = 17.778

# ***** From old settings
STEP_SCALE               = 1280

# ***********************
# Maximum acceleration for this joint in machine units per second
# squared.
MAX_ACCELERATION         = 30

# Hardware StepGen requires values in rps (revolution per second)
# As it should be 10%+ higher than MAX_ACCELERATION, it is set to 1
STEPGEN_MAXACCEL         = 31

# ***********************
#
# 10 rev   360 deg   1 min
# ------ x ------- x ------ = 60 deg/sec
#  1 min    1 rev    60 sec
#
# Maximum velocity for this joint in machine units per second.
MAX_VELOCITY           	 = 60

# Hardware StepGen requires values in rps (revolution per second)
# As it should be 10%+ higher than MAX_VELOCITY, it is set to 2
STEPGEN_MAXVEL           = 2

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




# pg 160
HOME                     = 0.0

# pg 160
HOME_OFFSET              = 0.0

# pg 160
HOME_SEQUENCE            = 4

# pg 158
UNITS                    = degree




# ********************************************************************
# Homing
HOME                 = 0.0
HOME_SEQUENCE        = 4

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
