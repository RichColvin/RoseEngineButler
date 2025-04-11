# ******************************************
# Rosetta_Sp0.inc for defining the Spindle 0
# for use with LinuxCNC on a Rose Engine
# ******************************************
#   Ver 1.0 - 11 April 2025, R. Colvin

# ******************************************
# [AXIS_<letter>]
# Details about the fields are available in the 
#   LinuxCNC 2.9.4 System Manual, 
#   §4.4.2.12, starting on pg. 157

# [JOINT_<number>]
# Details about the fields are available in the 
#   LinuxCNC 2.9.4 System Manual, 
#   §4.4.2.13, starting on pg. 158

# [SPINDLE_<number>]
# Details about the fields are available in the 
#   LinuxCNC 2.9.4 System Manual, 
#   §4.4.2.14, starting on pg. 164

# ******************************************
#                                 Home
#  Axis  Joint  Channel   Type     Seq
#  ----  -----  -------  -------  ----
#   Sp     7       05	   n/a     n/a

[SPINDLE_0]
# The values represent the number of pulses required to move the 
# distance specified by ANGULAR_UNITS or LINEAR_UNITS in
# the [TRAJ] section.  The gearing of the stepper motor
# to the movement will set this.  (pg. 163 in the manual)
#
# Values based on 
# 1. stepper motors with 1.8 deg / step.
#
# 2. DM542T set to microsteps = 128
#
# 	128 pulses   1 step    360 deg			pulses
# 	---------- * ------- * ------- = 25,600 ------
#      step      1.8 deg  	1 rev 			 rev
#
# 3. Spindle gear:Spindle motor gear ratio is 108:12 = 9
#

# pg 161
BIAS					 = 0.0

# pg 161
DEADBAND				 = 0.000015

# pg 140, 264-265, 269
DIRHOLD   				 = 10000
DIRSETUP  				 = 10000

# pg 163, 164
#
# 				  128 pulses
# ENCODER_SCALE = ----------
#     		        1.8 deg
#
# ENCODER_SCALE = 71.111 pulses / deg
ENCODER_SCALE			 = 71.111

# pg 164
INCREMENT				 = 0.1

# INPUT_SCALE = ENCODER_SCALE
# pg 163
INPUT_SCALE				 = 71.111

# pg 160
LOCKING_INDEXER			 = 1

# pg 158
# MAX_ACCELERATION = 30 deg / sec2
MAX_ACCELERATION		 = 30

# rpm, pg 158
#
# 						  20 Sp rev	  9 motor rev
# MAX_FORWARD_VELOCITY = ---------- * -----------  
#							1 min		1 Sp rev
#
# MAX_FORWARD_VELOCITY = 180 rpm
MAX_FORWARD_VELOCITY	 = 180

# MAX_LIMIT				 = 1e99

# pg 159, 163
MAX_OUTPUT				 = 10.0

# MAX_REVERSE_VELOCITY = MAX_FORWARD_VELOCITY
# MAX_REVERSE_VELOCITY	 = 180

# pg 158
# MAX_VELOCITY = MAX_FORWARD_VELOCITY
# MAX_VELOCITY			 = 180

# rpm, pg. 164
MIN_FORWARD_VELOCITY	 = 0.0

# MIN_LIMIT				 = -1e99
# rpm, pg 158
MIN_REVERSE_VELOCITY	 = 0.0

# SCALE = ENCODER_SCALE
# pg 163
SCALE					 = 71.111

# 1%-10% higher than MAX_ACCELERATION
# pg 164
STEPGEN_MAXACCEL		 = 33

# 1%-10% higher than MAX_VELOCITY
# pg 164
STEPGEN_MAXVEL  		 = 0.25

# pg 140, 264-265, 269
STEPLEN   				 = 5000
STEPSPACE 				 = 5000

# pg 163
#
# 			   128 pulses   360 deg   9 motor rev
# STEP_SCALE = ---------- * ------- * -----------
#     		    1.8 deg		 1 rev     1 Sp rev
#
# STEP_SCALE = 230400 pulses / deg
# STEP_SCALE				 = 1536000
STEP_SCALE				 = 230400

# pgs 161-162
P						 = 1000.0
I						 = 0.0
D						 = 0.0
FF0						 = 1.0
FF1						 = 0.0
FF2						 = 0.0
