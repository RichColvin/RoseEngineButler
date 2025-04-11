# ******************************************
# Rosetta_AxisC.inc for defining the Axis C
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

[AXIS_C]
# machine units per second sq
MAX_ACCELERATION		 = 30.0
# for unlimited rotation, set this to 1e99
MAX_LIMIT				 = 9999.0
# machine units per second
MAX_VELOCITY			 = 1.0
# for unlimited rotation, set this to -1e99
MIN_LIMIT				 = -9999.0
TYPE					 = ANGULAR
WRAPPED_ROTARY			 = 1

[JOINT_4]
# STEP_SCALE can be tuned for the specific device.  The value 
# represents the number of pulses required to move the 
# distance specified by ANGULAR_UNITS or LINEAR_UNITS in
# the [TRAJ] section.  The gearing of the stepper motor
# to the movement will set this.  (pg. 163 in the manual)
#
#			   1 rev
# LEADSCREW = ------- = 0.2 rev/deg of device movement
#			   5 deg
#
# 		       128 steps   360 deg   0.2 rev
# STEP_SCALE = --------- * ------- * -------
#   	        1.8 deg     1 rev	  1 deg
#
# STEP_SCALE = 5,120 steps/deg
#
STEP_SCALE				 = 5120

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
# ENCODER_SCALE			 = 5120

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
# INPUT_SCALE			 = 5120

# pg 160
# LOCKING_INDEXER			 = 1

# pg 158
# machine units per second sq
MAX_ACCELERATION		 = 30.0

# pg 159
# for unlimited rotation, set this to 1e99
MAX_LIMIT 				 = 9999.9

# pg 163
MAX_OUTPUT				 = 10.0

# pg 158
# machine units per second
MAX_VELOCITY 			 = 1.0

# pg 159
MIN_FERROR 				 = 0.05

# pg 159
# for unlimited rotation, set this to -1e99
MIN_LIMIT				 = -9999.9

# pg 163
# SCALE = STEP_SCALE
# SCALE					 = 5120

# pg 164
# STEPGEN_MAXACCEL should be 1%-10% < than MAX_ACCELERATION
STEPGEN_MAXACCEL		 = 37.50

# pg 164
# STEPGEN_MAXVEL should be 1%-10% < than MAX_VELOCITY
STEPGEN_MAXVEL  		 = 1.25

# pg 140, 264-265, 269
STEPLEN					 = 5000
STEPSPACE				 = 5000

# pg 158
TYPE					 = ANGULAR

# pg 158
UNITS					 = degree

# pgs 161-162
P						 = 1000.0
I						 = 0.0
D						 = 0.0
FF0						 = 0.0
FF1						 = 1.0
FF2						 = 0.0
