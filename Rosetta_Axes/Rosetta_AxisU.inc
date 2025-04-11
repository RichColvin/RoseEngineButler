# ******************************************
# Rosetta_AxisU.inc for defining the Axis U
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

# ******************************************
#                                 Home
#  Axis  Joint  Channel   Type     Seq
#  ----  -----  -------  -------  ----
#   U      4       04	 LINEAR     5

[AXIS_U]
MAX_ACCELERATION		 = 30.0
MAX_LIMIT				 = 9999.9
MAX_VELOCITY			 = 1.0
MIN_LIMIT				 = -9999.9
TYPE					 = LINEAR

[JOINT_4]
# STEP_SCALE can be tuned for the specific device.  The value 
# represents the number of pulses required to move the 
# distance specified by ANGULAR_UNITS or LINEAR_UNITS in
# the [TRAJ] section.  The gearing of the stepper motor
# to the movement will set this.  (pg. 163 in the manual)
#
#			  1 rev   25.4 mm
# LEADSCREW = ----- * ------- = 12.7 rev/in
#			  2 mm     1 inch
# 		       128 steps   360 deg   12.7 rev
# STEP_SCALE = --------- * ------- * --------
#   	        1.8 deg      rev	   inch
# STEP_SCALE = 325,120 steps/inch
#
STEP_SCALE				 = 325120

# pg 158
BACKLASH				 = 0.0000

# pg 161
BIAS					 = 0.0

# pg 161
DEADBAND				 = 0.0

# pg 140, 264-265, 269
DIRHOLD					 = 10000
DIRSETUP				 = 10000

# ENCODER_SCALE = STEP_SCALE
# pg 163, 164
# ENCODER_SCALE			 = 325120

# pg 159
FERROR 					 = 0.5

# pg 160
HOME					 = 0.0

# pg 160
HOME_OFFSET 			 = 0.0

# pg 160
HOME_SEQUENCE 			 = 5

# pg 163
# INPUT_SCALE = STEP_SCALE
# INPUT_SCALE			 = 325120

# pg 160
# LOCKING_INDEXER			 = 1

# pg 158
# machine units per second sq
MAX_ACCELERATION		 = 30.0

# pg 159
MAX_LIMIT 				 = 9999.9

# pg 163
MAX_OUTPUT				 = 0.0

# pg 158
# machine units per second
MAX_VELOCITY 			 = 0.25

# pg 159
MIN_FERROR 				 = 0.05

# pg 159
MIN_LIMIT				 = -9999.9

# pg 163
# SCALE = STEP_SCALE
# SCALE					 = 325120

# pg 164
# STEPGEN_MAXACCEL should be 1%-10% < than MAX_ACCELERATION
STEPGEN_MAXACCEL		 = 33.0

# pg 164
# STEPGEN_MAXVEL should be 1%-10% < than MAX_VELOCITY
STEPGEN_MAXVEL  		 = 0.275

# pg 140, 264-265, 269
STEPLEN					 = 5000
STEPSPACE				 = 5000

# pg 158
TYPE					 = LINEAR

# pg 158
UNITS					 = inch

# pgs 161-162
P						 = 1000.0
I						 = 0.0
D						 = 0.0
FF0						 = 0.0
FF1						 = 1.0
FF2						 = 0.0
