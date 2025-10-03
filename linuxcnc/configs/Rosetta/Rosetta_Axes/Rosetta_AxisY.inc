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
#   Rosetta_AxisY.inc                                                 #
#                                                                     #
# Purpose:                                                            #
#   This is used to setup the Y axis for the configuration of         #
#   LinuxCNC.                                                         #
#                                                                     #
# End User Customisation:                                             #
# ********************************************************************
# Details about the fields are available in the

# ********************************************************************
# Configuration values
#                                 Home   PCB
#  Axis  Joint  Channel   Type     Seq  Plug  Comments
#  ----  -----  -------  -------  ----  ----  ------------------------
#   Y      1       03    LINEAR     2    P14
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

# ********************************************************************
#    AA    XX    XX IIIIIIII  SSSSSS      YY    YY
#   AAAA    XX  XX    II     SS    SS      YY  YY
#  AA  AA    XXXX     II      SSS           YYYY
# AAAAAAAA   XXXX     II         SSS         YY
# AA    AA  XX  XX    II     SS    SS        YY
# AA    AA XX    XX IIIIIIII  SSSSSS         YY
# ********************************************************************
[AXIS_Y]
TYPE                 = LINEAR

MAX_VELOCITY         = 1.0
MAX_ACCELERATION     = 20.0

MIN_LIMIT            = -1e99
MAX_LIMIT            = 1e99

[JOINT_1]
TYPE                 = LINEAR
UNITS                = INCH

MAX_VELOCITY         = 1.0
MAX_ACCELERATION     = 2.0

BACKLASH             = 0.0000

MIN_LIMIT            = -1e99
MAX_LIMIT            = 1e99

MIN_FERROR           = 0.5
FERROR               = 5

# ********************************************************************
# Homing
HOME                 = 0.0
HOME_SEQUENCE        = 2

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
# These parameters are only needed when using servo motors.  They are
# not relevant to joints controlled by stepper motors.

# BIAS                 = 0.0
# DEADBAND             = 0.000015

# P                    = 1000.0
# I                    = 0.0
# D                    = 0.0
# FF0                  = 1.0
# FF1                  = 0.0
# FF2                  = 0.0
# ********************************************************************
