#######################################################################
#                    RRRRRR    EEEEEEEE  BBBBBBB                      #
#                    RR   RR   EE        BB    BB                     #
#                    RR   RR   EE        BB    BB                     #
#                    RRRRRR    EEEEEE    BBBBBBB                      #
#                    RR   RR   EE        BB    BB                     #
#                    RR    RR  EE        BB    BB                     #
#                    RR    RR  EEEEEEEE  BBBBBBB                      #
#                                                                     #
#                         Rose Engine Butler                          #
#######################################################################
#
# LinuxCNC configuration for use with a Rose Engine
#
# File:
#   hitcounter.py
#
# Purpose:  This is used to handle buttons used in panels developed
#   for Rose Engine Butler's use on LinuxCNC.
#
# End User Customisation:
#   THE END USER OF THE ROSE ENGINE BUTLER SYSTEM SHOULD NOT MODIFY
#   THIS FILE.
#
#   Changes to this file are not supported by Colvin Tools nor
#   Brainwave Embedded.
#
# Version
#   1.0 - 26 December 2025, R. Colvin
#
# Copyright (c) 2025 Colvin Tools and Brainwave Embedded.
#
# The following MIT/X Consortium License applies to the Rose Engine
# Butler system. Use of this system constitutes consent to the terms
# outlined below.
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
#       The above copyright notice and this permission notice shall be
#       included in all copies or substantial portions of the
#       Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# Except as contained in this notice, the name of COPYRIGHT HOLDERS
# shall not be used in advertising or otherwise to promote the sale,
# use or other dealings in this Software without prior written
# authorization from COPYRIGHT HOLDERS.
#######################################################################

import hal
import glib
import time
import linuxcnc
import webbrowser

# Establish connection to command and status channels
c = linuxcnc.command()
s = linuxcnc.stat()

class HandlerClass:
    '''
    class with gladevcp callback handlers
    '''

    def on_button_press(self,widget,data=None):
        '''
        a callback method
        parameters are:
            the generating object instance, likte a GtkButton instance
            user data passed if any - this is currently unused but
            the convention should be retained just in case
        '''
        print ("on_button_press called")
        self.nhits += 1
        self.builder.get_object('hits').set_label("Hits: %d" % (self.nhits))

# ********************************************************************
#    AA    XX    XX IIIIIIII  SSSSSS      BBBBBBB
#   AAAA    XX  XX    II     SS    SS     BB    BB
#  AA  AA    XXXX     II      SSS         BBBBBBB
# AAAAAAAA   XXXX     II         SSS      BB    BB
# AA    AA  XX  XX    II     SS    SS     BB    BB
# AA    AA XX    XX IIIIIIII  SSSSSS      BBBBBBB
# ********************************************************************

#######################################################################
# B_Move_Idx_Fwd
# Purpose:              This is used to run the B axis forward using
#                       the G0 Gcode.
# Updated:              ver 1.0, 26 December 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Rotary
#   Button:             B_Move_Idx_Fwd  (Hal_Button)
#   Signal:             GtkButton/pressed
# ---------------------------------------------------------------------
# Data
#   Read from UI:       B_Feed - Feed rate set by user
#   Program Variables
#       Referenced:     (none)
#       Set:            B_Idx_Qty - the quantity of indexes so far.
#                           Forward increases this value.
#   Written to UI:      B_Idx_Qty - the quantity of indexes so far.
#                           Forward increases this value.
# ---------------------------------------------------------------------
# Gcodes Called:    (none)
#######################################################################
    def B_Move_Idx_Fwd(self,widget):

        print("=================================================")
        print("FUNCTION B_Move_Idx_Fwd")

        # Ensure the system is in MDI mode
        s.poll()
        if s.task_state != linuxcnc.MODE_MDI:
                c.mode(linuxcnc.MODE_MDI)
                c.wait_complete() # Wait for mode change to complete

        # Send an MDI command to move along the axis.
        Gcode = "G0 B" + str(self.B_Idx_Deg) + " F" + str(self.B_Feed)

        print(Gcode)
        c.mdi(Gcode)

        # Wait for the command to complete
        c.wait_complete()

        # increment the count and write out to the UI
        self.B_Idx_Qty = self.B_Idx_Qty + 1
        Prt1 = "B_Idx_Qty = " + str(self.B_Idx_Qty)
        print(Prt1)

        # B_Idx_Qtystr = str(self.B_Idx_Qty)
        # widget.set_label(B_Idx_Qty, B_Idx_Qtystr)

#######################################################################
# B_Move_Idx_Rev
# Purpose:              This is used to run the B axis in reverse using
#                       the G0 Gcode.
# Updated:              ver 1.0, 26 December 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Rotary
#   Button:             B_Move_Idx_Rev  (Hal_Button)
#   Signal:             GtkButton/pressed
# ---------------------------------------------------------------------
# Data
#   Read from UI:       B_Feed - Feed rate set by user
#   Program Variables
#       Referenced:     (none)
#       Set:            B_Idx_Qty - the quantity of indexes so far. Reverse
#                           decreases this value.
#   Written to UI:      B_Idx_Qty - the quantity of indexes so far. Reverse
#                           decreases this value.
# ---------------------------------------------------------------------
# Gcodes Called:        (none)
#######################################################################
    def B_Move_Idx_Rev(self,widget):

        print("=================================================")
        print("FUNCTION B_Move_Idx_Rev")

        # Ensure the system is in MDI mode
        s.poll()
        if s.task_state != linuxcnc.MODE_MDI:
                c.mode(linuxcnc.MODE_MDI)
                c.wait_complete() # Wait for mode change to complete

        # Send an MDI command to move along the axis.
        Gcode = "G0 B-" + str(self.B_Idx_Deg) + " F" + str(self.B_Feed)

        print(Gcode)
        c.mdi(Gcode)

        self.B_Idx_Qty = self.B_Idx_Qty - 1
        Prt1 = "B_Idx_Qty = " + str(self.B_Idx_Qty)
        print(Prt1)

        # Wait for the command to complete
        c.wait_complete()

#######################################################################
# DDDD   EEEEE  PPPP   RRRR   EEEEE    CC    AAA   TTTTT  EEEEE  DDDD 
# D   D  E      P   P  R   R  E       C  C  A   A    T    E      D   D
# D   D  E      P   P  R   R  E      C      A   A    T    E      D   D
# D   D  EEE    PPPP   RRRR   EEE    C      AAAAA    T    EEE    D   D
# D   D  E      P      R   R  E      C      A   A    T    E      D   D
# D   D  E      P      R   R  E       C  C  A   A    T    E      D   D
# DDDD   EEEEE  P      R   R  EEEEE    CC   A   A    T    EEEEE  DDDD 
# 
# DEPRECATED:  This was replaced by B_Set_Idx_by_DegDiv
#
# B_Set_Idx_by_Deg
# Purpose:              This is used to set the rotational distance
#                       measurement as degrees for the B axis.
# Updated:              ver 1.0, 26 December 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Rotary
#   Button:             B_Move_Idx_Deg  (HAL_RadioButton)
#   Signal:             GtkWidget/button-press-event
# ---------------------------------------------------------------------
# Data
#   Read from UI:       (none)
#   Program Variables
#       Referenced:     B_Idx_Dist - Distance set by user
#       Set:            B_Idx_Deg - Degrees to index during movement
#                       B_Idx_DegDiv - type of distance measurement
#                           (Deg or Div)
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        (none)
#######################################################################
    def B_Set_Idx_by_Deg(self,widget):

        print("=================================================")
        print("FUNCTION B_Set_Idx_by_Deg")

        self.B_Idx_Deg = self.B_Idx_Dist
        self.B_Idx_DegDiv = "Deg"

        Prt1 = "B_Idx_DegDiv = " + self.B_Idx_DegDiv
        print(Prt1)
        Prt2 = "B_Idx_Deg = " + str(self.B_Idx_Deg) + " deg"
        print(Prt2)



#######################################################################
# Sp0_Set_Idx_by_DegDiv
# Purpose:              This is used to set the rotational distance
#                       measurement for the Sp0 & Sp1 spindles.
#                       If degrees, set to divisions; 
#                       if divisions, set to degrees.
# Updated:              ver 1.0, 26 December 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Rotary
#                       REB_Tab_Sync
#   Button:             Sp0_Set_Idx_by_Deg  (HAL_RadioButton)
#   Signal:             GtkWidget/button-press-event
# ---------------------------------------------------------------------
# Data
#   Read from UI:       (none)
#   Program Variables
#       Referenced:     self.Sp0_Idx_Dist - distance field data
#       Set:            self.Sp0_Idx_Deg - degrees to index
#                       self.Sp0_Idx_DegDiv - type of distance
#                           measurement (Deg or Div)
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        (none)
#######################################################################
    def B_Set_Idx_by_DegDiv(self,widget):

        print("=================================================")
        print("FUNCTION B_Set_Idx_by_DegDiv")

        if self.B_Idx_DegDiv == "Deg":
		        self.B_Idx_DegDiv = "Div"
		        self.B_Idx_Deg = round(360 / self.B_Idx_Dist, 1)
        else:
		        self.B_Idx_DegDiv = "Deg"
		        self.B_Idx_Deg = round(self.B_Idx_Dist, 1)

        Prt1 = "B_Idx_Deg = " + str(self.B_Idx_Deg)
        print(Prt1)

        Prt2 = "self.B_Idx_DegDiv = " + self.B_Idx_DegDiv
        print(Prt2)

#######################################################################
# DDDD   EEEEE  PPPP   RRRR   EEEEE    CC    AAA   TTTTT  EEEEE  DDDD 
# D   D  E      P   P  R   R  E       C  C  A   A    T    E      D   D
# D   D  E      P   P  R   R  E      C      A   A    T    E      D   D
# D   D  EEE    PPPP   RRRR   EEE    C      AAAAA    T    EEE    D   D
# D   D  E      P      R   R  E      C      A   A    T    E      D   D
# D   D  E      P      R   R  E       C  C  A   A    T    E      D   D
# DDDD   EEEEE  P      R   R  EEEEE    CC   A   A    T    EEEEE  DDDD 
# 
# DEPRECATED:  This was replaced by B_Set_Idx_by_DegDiv
#
# B_Set_Idx_by_Div
# Purpose:              This is used to set the rotational distance
#                       measurement as divisions of a circle for the B
#                       axis (deg = 360/div).
# Updated:              ver 1.0, 26 December 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Rotary
#   Button:             B_Move_Idx_Div  (HAL_RadioButton)
#   Signal:             GtkWidget/button-press-event
# ---------------------------------------------------------------------
# Data
#   Read from UI:       (none)
#   Program Variables
#       Referenced:     B_Idx_Dist - Distance set by user
#       Set:            B_Idx_Deg - Degrees to index during movement
#                       B_Idx_DegDiv - type of distance measurement
#                           (Deg or Div)
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        (none)
#######################################################################
    def B_Set_Idx_by_Div(self,widget):

        print("=================================================")
        print("FUNCTION B_Set_Idx_by_Div")

        self.B_Idx_Deg = 360 / self.B_Idx_Dist

        self.B_Idx_DegDiv = "Div"

        Prt1 = "B_Idx_DegDiv = " + self.B_Idx_DegDiv
        print(Prt1)
        Prt2 = "B_Idx_Deg = " + str(self.B_Idx_Deg) + " deg"
        print(Prt2)

#######################################################################
# B_Set_Move_Dist
# Purpose:              This is used to set the movement distance for
#                           the B axis.
# Updated:              ver 1.0, 26 December 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Sync
#   Button:             B_Move_Dist (on setting the value)
#   Signal:             GtkSpinButton/value-changed
# ---------------------------------------------------------------------
# Data
#   Read from UI:       B_Move_Dist
#   Program Variables
#       Referenced:     (none)
#       Set:            self.B_Move_Dist
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        (none)
#######################################################################
    def B_Set_Move_Dist(self,widget):

        print("=================================================")
        print("FUNCTION B_Set_Move_Dist")

        self.B_Move_Dist = widget.get_value()

        print("B_Move_Dist = " + str(self.B_Move_Dist))

#######################################################################
# B_Set_Idx_Dist
# Purpose:              This is used to set the rotational distance
#                       (degrees or divisions of a circle) for the B
#                       axis.
# Updated:              ver 1.0, 26 December 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Rotary
#   Button:             B_Set_Idx_Dist  (HAL_SpinButton)
#   Signal:             GtkSpinButton/value-changed
# ---------------------------------------------------------------------
# Data
#   Read from UI:       B_Idx_Dist
#   Program Variables
#       Referenced:     B_Idx_Dist - Distance set by user
#       Set:            B_Idx_Deg - Degrees to index during movement
#                       B_Idx_DegDiv - type of distance measurement
#                           (Deg or Div)
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        (none)
#######################################################################
    def B_Set_Idx_Dist(self,widget):

        print("=================================================")
        print("FUNCTION B_Set_Idx_Dist")

        self.B_Idx_Dist = widget.get_value()

        if self.B_Idx_DegDiv == "Deg":
                self.B_Idx_Deg = round(self.B_Idx_Dist, 1)
        else:
                self.B_Idx_Deg = round(360 / self.B_Idx_Dist, 1)

        Prt1 = "B_Idx_DegDiv = " + self.B_Idx_DegDiv
        print(Prt1)
        Prt2 = "B_Idx_Deg = " + str(self.B_Idx_Deg) + " deg"
        print(Prt2)

#######################################################################
# B_Set_Idx_Feed
# Purpose:              This is used to set the movement speed for the
#                       B axis.
# Updated:              ver 1.0, 26 December 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Rotary    (HAL_SpinButton)
#   Button:             B_Feed
#   Signal:             GtkSpinButton/value-changed
# ---------------------------------------------------------------------
# Data
#   Read from UI:       B_Feed - Feed rate set by user
#   Program Variables
#       Referenced:
#       Set:            B_Feed
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        (none)
#######################################################################
    def B_Set_Idx_Feed(self,widget):

        print("=================================================")
        print("FUNCTION B_Set_Idx_Feed")

        self.B_Feed = widget.get_value()

        Prt1 = "B_Feed = " + str(self.B_Feed)
        print(Prt1)


# ********************************************************************
#    AA     LL       LL              AA    XX    XX EEEEEEEE  SSSSSS 
#   AAAA    LL       L              AAAA    XX  XX  EE       SSS   SS
#  AA  AA   LL       LL            AA  AA    XXXX   EE        SSS 
# AAAAAAAA  LL       LL           AAAAAAAA   XXXX   EEEEE        SSS 
# AA    AA  LL       LL           AA    AA  XX  XX  EE       SS    SS
# AA    AA  LLLLLLLL LLLLLLLL     AA    AA XX    XX EEEEEEEE  SSSSSS  
# ********************************************************************

#######################################################################
# OpenGcodeLibrary
# Purpose:              This is used to open the Rose Engine Butler
#                       Gcode library web page.
# Updated:              ver 1.0, 26 December 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Help
#   Button:             Gcode_Library
#   Signal:             GtkButton/pressed
# ---------------------------------------------------------------------
# Data
#   Read from UI:       (none)
#   Program Variables
#       Referenced:     (none)
#       Set:            self.Z_Sync_Bool
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        (none)
#######################################################################
    def OpenGcodeLibrary(self,widget):

        print("=================================================")
        print("FUNCTION OpenGcodeLibrary")

        url = "https://gcode.RoseEngineButler.com"
        webbrowser.open(url)

        Prt1 = "Opening website " + url
        print(Prt1)

#######################################################################
# OpenLibrary
# Purpose:              This is used to open the Rose Engine Butler
#                       web page.
# Updated:              ver 1.0, 26 December 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Help
#   Button:             OpenLibrary
#   Signal:             GtkButton/pressed
# ---------------------------------------------------------------------
# Data
#   Read from UI:       (none)
#   Program Variables
#       Referenced:     (none)
#       Set:            self.Z_Sync_Bool
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        (none)
#######################################################################
    def OpenLibrary(self,widget):

        print("=================================================")
        print("FUNCTION OpenLibrary")

        url = "https://www.RoseEngineButler.com"
        webbrowser.open(url)

        Prt1 = "Opening website " + url
        print(Prt1)

#######################################################################
# OpenUserManual
# Purpose:              This is used to open the Rose Engine Butler
#                       user manual web page.
# Updated:              ver 1.0, 26 December 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Help
#   Button:             User_Manual
#   Signal:             GtkButton/pressed
# ---------------------------------------------------------------------
# Data
#   Read from UI:       (none)
#   Program Variables
#       Referenced:     (none)
#       Set:            self.Z_Sync_Bool
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        (none)
#######################################################################
    def OpenUserManual(self,widget):

        print("=================================================")
        print("FUNCTION OpenUserManual")

        url = "https://manual.RoseEngineButler.com"
        webbrowser.open(url)

        Prt1 = "Opening website " + url
        print(Prt1)

#######################################################################
# Synchronized Movement                                               #
#######################################################################

#######################################################################
# Run_Sync_Fwd
# Purpose:              This is used to start the spindles rotating in
#                           reverse.
#                       Note:  this starts both Sp0 and Sp1.
# Updated:              ver 1.0, 26 December 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Sync
#   Button:             Run_Sync_Fwd  (Hal_Button)
#   Signal:             GtkButton/pressed
# ---------------------------------------------------------------------
# Data
#   Read from UI:       (none)
#   Program Variables
#       Referenced:     self.Sp0_Sync_Bool
#                       self.Sp1_Sync_Bool
#                       self.B_Sync_Bool
#                       self.U_Sync_Bool
#                       self.V_Sync_Bool
#                       self.X_Sync_Bool
#                       self.Y_Sync_Bool
#                       self.Z_Sync_Bool
#
#                       self.Sp0_Feed
#                       self.Sp1_Pct
#       Set:            (none)
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        S, M4
#######################################################################
    def Run_Sync_Fwd(self,widget):


# This is not complete yet  - R. Colvin #

        '''

        print("=================================================")
        print("FUNCTION Run_Sync_Fwd")


        if self.Sp0_Idx_Bool:
                self.Sp0_Idx_Bool = False
                print("Sp0_Idx_Bool = False")
        else:
                self.Sp0_Idx_Bool = True
                print("Sp0_Idx_Bool = True")








        # Ensure the system is in MDI mode
        c.mode(linuxcnc.MODE_MDI)
        s.poll()
        if s.task_state != linuxcnc.MODE_MDI:
                c.mode(linuxcnc.MODE_MDI)
                c.wait_complete() # Wait for mode change to complete

        # In case the values had not already been written to the
        # Gcode S values, write them.
        Sp1_Feed = self.Sp1_Pct * self.Sp0_Feed / 100

        # Send an MDI command to set the spindles' speed.
        sSp0_Feed = "S" + str(self.Sp0_Feed) + " $0"
        sSp1_Feed = "S" + str(Sp1_Feed) + " $1"

        print(sSp0_Feed)
        c.mdi(sSp0_Feed)

        print(sSp1_Feed)
        c.mdi(sSp1_Feed)

        # Send an MDI command to start spindles rotating.
        Gcode = "M4 $-1"

        print(Gcode)
        c.mdi(Gcode)

        # Wait for the command to complete
        c.wait_complete()
        '''

# ********************************************************************
#  SSSSSS  PPPPPPP  IIIIIIII N     NN DDDDDDD  LL       EEEEEEEE   0000
# SS    SS PP    PP    II    NN    NN DD    DD LL       EE        00  00
#  SSS     PP    PP    II    NNN   NN DD    DD LL       EEEEE    00    00
#     SSS  PPPPPPP     II    NN NN NN DD    DD LL       EE       00    00
# SS    SS PP          II    NN  NNNN DD    DD LL       EE        00  00
#  SSSSSS  PP       IIIIIIII NN    NN DDDDDDD  LLLLLLLL EEEEEEEE   0000
# ********************************************************************

#######################################################################
# Sp0_Move_Fwd
# Purpose:              This is used to start the spindles rotating
#                           forward.
#                       Note:  this starts both Sp0 and Sp1.
# Updated:              ver 1.0, 26 December 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Base
#   Button:             Sp0_Move_Fwd  (Hal_Button)
#   Signal:             GtkButton/pressed
# ---------------------------------------------------------------------
# Data
#   Read from UI:       (none)
#   Program Variables
#       Referenced:     self.Sp0_Feed
#                       self.Sp1_Pct
#       Set:            (none)
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        S, M3
#######################################################################
    def Sp0_Move_Fwd(self,widget):

        print("=================================================")
        print("FUNCTION Sp0_Move_Fwd")

        # Ensure the system is in MDI mode
        c.mode(linuxcnc.MODE_MDI)
        s.poll()
        if s.task_state != linuxcnc.MODE_MDI:
                c.mode(linuxcnc.MODE_MDI)
                c.wait_complete() # Wait for mode change to complete

        # Set the feed rates
        Sp1_Feed = self.Sp1_Pct * self.Sp0_Feed / 100

        # Send an MDI command to set the spindles' speed.
        sSp0_Feed = "S" + str(self.Sp0_Feed) + " $0"
        sSp1_Feed = "S" + str(Sp1_Feed) + " $1"

        print(sSp0_Feed)
        c.mdi(sSp0_Feed)

        print(sSp1_Feed)
        c.mdi(sSp1_Feed)

        # Send an MDI command to start spindles rotating.
        Gcode = "M3 $-1"

        print(Gcode)
        c.mdi(Gcode)

        # Wait for the command to complete
        c.wait_complete()

#######################################################################
# Sp0_Move_Idx_Fwd
# Purpose:              This is used to index the Sp0 spindle in a
#                           forward direction.
# Updated:              ver 1.0, 26 December 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Rotary
#   Button:             Sp0_Idx_Fwd
#   Signal:             GtkButton/pressed
# ---------------------------------------------------------------------
# Data
#   Read from UI:       (none)
#   Program Variables
#       Referenced:     self.Sp0_Idx_Deg
#                       self.Sp1_Pct
#       Set:            (none)
#   Written to UI:      B_Idx_Qty - the quantity of indexes so far.
#                           Forward increases this value.
# ---------------------------------------------------------------------
# Gcodes Called:        M19
#######################################################################
    def Sp0_Move_Idx_Fwd(self,widget):

        print("=================================================")
        print("FUNCTION Sp0_Move_Idx_Fwd")

        # Ensure the system is in MDI mode
        s.poll()
        if s.task_state != linuxcnc.MODE_MDI:
                c.mode(linuxcnc.MODE_MDI)
                c.wait_complete() # Wait for mode change to complete

        # Set spindle rotational speeds
        GcodeStr1 = "S0 " + str(self.Sp0_Feed)
        print(GcodeStr1)

        Sp1_Feed = self.Sp0_Feed * self.Sp1_Pct / 100
        GcodeStr2 = "S1 " + str(Sp1_Feed)
        print(GcodeStr2)

        c.mdi(GcodeStr1)
        c.mdi(GcodeStr2)

        # Send MDI command to start spindles rotating.
        GcodeStr3 = "M19 R" + str(self.Sp0_Idx_Deg) + " Q10 P1 $0"
        print(GcodeStr3)
        c.mdi(GcodeStr3)

        GcodeStr4 = "M19 R" + str(self.Sp0_Idx_Deg) + " Q10 P1 $1"
        print(GcodeStr4)
        c.mdi(GcodeStr4)

        # Wait for the command to complete
        c.wait_complete()

#######################################################################
# Sp0_Move_Idx_Rev
# Purpose:              This is used to index the Sp0 spindle in a
#                           reverse direction.
# Updated:              ver 1.0, 26 December 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Rotary
#   Button:             Sp0_Idx_Rev
#   Signal:             GtkButton/pressed
# ---------------------------------------------------------------------
# Data
#   Read from UI:       (none)
#   Program Variables
#       Referenced:     self.Sp0_Idx_Deg
#                       self.Sp1_Pct
#       Set:            (none)
#   Written to UI:      B_Idx_Qty - the quantity of indexes so far.
#                           Forward increases this value.
# ---------------------------------------------------------------------
# Gcodes Called:        M19
#######################################################################
    def Sp0_Move_Idx_Rev(self,widget):

        print("=================================================")
        print("FUNCTION Sp0_Move_Idx_Rev")

        # Ensure the system is in MDI mode
        s.poll()
        if s.task_state != linuxcnc.MODE_MDI:
                c.mode(linuxcnc.MODE_MDI)
                c.wait_complete() # Wait for mode change to complete

        # Set spindle rotational speeds
        GcodeStr1 = "S0 " + str(self.Sp0_Feed)
        print(GcodeStr1)

        Sp1_Feed = self.Sp0_Feed * self.Sp1_Pct / 100
        GcodeStr2 = "S1 " + str(Sp1_Feed)
        print(GcodeStr2)

        c.mdi(GcodeStr1)
        c.mdi(GcodeStr2)

        # Send MDI commands to start spindles rotating.
        GcodeStr3 = "M19 R" + str(self.Sp0_Idx_Deg) + " Q10 P2 $0"
        print(GcodeStr3)
        GcodeStr4 = "M19 R" + str(Sp1_Idx_Deg) + " Q10 P1 $1"
        print(GcodeStr4)

        c.mdi(GcodeStr3)

        # Wait for the command to complete
        c.wait_complete()

#######################################################################
# Sp0_Move_Rev
# Purpose:              This is used to start the spindles rotating in
#                           reverse.
#                       Note:  this starts both Sp0 and Sp1.
# Updated:              ver 1.0, 26 December 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Base
#   Button:             Sp0_Move_Rev  (Hal_Button)
#   Signal:             GtkButton/pressed
# ---------------------------------------------------------------------
# Data
#   Read from UI:       (none)
#   Program Variables
#       Referenced:     self.Sp0_Feed
#                       self.Sp1_Pct
#       Set:            (none)
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        S, M4
#######################################################################
    def Sp0_Move_Rev(self,widget):

        print("=================================================")
        print("FUNCTION Sp0_Move_Rev")

        # Ensure the system is in MDI mode
        c.mode(linuxcnc.MODE_MDI)
        s.poll()
        if s.task_state != linuxcnc.MODE_MDI:
                c.mode(linuxcnc.MODE_MDI)
                c.wait_complete() # Wait for mode change to complete

        # In case the values had not already been written to the
        # Gcode S values, write them.
        Sp1_Feed = self.Sp1_Pct * self.Sp0_Feed / 100

        # Send an MDI command to set the spindles' speed.
        sSp0_Feed = "S" + str(self.Sp0_Feed) + " $0"
        sSp1_Feed = "S" + str(Sp1_Feed) + " $1"

        print(sSp0_Feed)
        c.mdi(sSp0_Feed)

        print(sSp1_Feed)
        c.mdi(sSp1_Feed)

        # Send an MDI command to start spindles rotating.
        Gcode = "M4 $-1"

        print(Gcode)
        c.mdi(Gcode)

        # Wait for the command to complete
        c.wait_complete()

#######################################################################
# Sp0_Move_Stop
# Purpose:              This is used to stop the spindles rotating.
#                       Note:  this stops both Sp0 and Sp1.
# Updated:              ver 1.0, 26 December 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Base
#   Button:             Sp0_Move_Stop  (Hal_Button)
#   Signal:             GtkButton/pressed
# ---------------------------------------------------------------------
# Data
#   Read from UI:       (none)
#   Program Variables
#       Referenced:     (none)
#       Set:            (none)
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        M5
#######################################################################
    def Sp0_Move_Stop(self,widget):

        print("=================================================")
        print("FUNCTION Sp0_Move_Stop")

        # Ensure the system is in MDI mode
        s.poll()
        if s.task_state != linuxcnc.MODE_MDI:
                c.mode(linuxcnc.MODE_MDI)
                c.wait_complete() # Wait for mode change to complete

        # Send an MDI command to stop the spindles from rotating.
        Gcode = "M5"

        print(Gcode)
        c.mdi(Gcode)

        c.mdi("M5")

        # Wait for the command to complete
        c.wait_complete()

#######################################################################
# Sp0_Set_Feed
# Purpose:              This is used to set the base feed rate for the
#                           spindle (Sp0) & the rosette phaser
#                           multiplier (Sp1).  (Sp1 gets multiplied
#                           by the value of Sp1Pct
# Updated:              ver 1.0, 26 December 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Base
#   Button:             Sp0_Set_Feed  (Hal_SpinButton)
#   Signal:             GtkSpinButton/value-changed
# ---------------------------------------------------------------------
# Data
#   Read from UI:       Sp0_Feed from Sp0_Spd on the UI
#   Program Variables
#       Referenced:     (none)
#       Set:            self.Sp0_Feed - the speed for the spindle
#                           (Sp0)
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        S
#######################################################################
    def Sp0_Set_Feed(self,widget):

        print("=================================================")
        print("FUNCTION Sp0_Set_Feed")

        self.Sp0_Feed = round(widget.get_value(), 1)
        print("self.Sp0_Feed = " + str(self.Sp0_Feed))

        Sp1_Feed = round(self.Sp0_Feed * self.Sp1_Pct / 100, 2)

        Gcode0 = "S" + str(self.Sp0_Feed) + " $0"
        Gcode1 = "S" + str(Sp1_Feed) + " $1"

        # Ensure the system is in MDI mode
        s.poll()
        if s.task_state != linuxcnc.MODE_MDI:
                c.mode(linuxcnc.MODE_MDI)
                c.wait_complete() # Wait for mode change to complete

        # Send an MDI commands to set the spindle speeds.
        print(Gcode0)
        c.mdi(Gcode0)

        print(Gcode1)
        c.mdi(Gcode1)

        # Wait for the command to complete
        c.wait_complete()

#######################################################################
# DDDD   EEEEE  PPPP   RRRR   EEEEE    CC    AAA   TTTTT  EEEEE  DDDD 
# D   D  E      P   P  R   R  E       C  C  A   A    T    E      D   D
# D   D  E      P   P  R   R  E      C      A   A    T    E      D   D
# D   D  EEE    PPPP   RRRR   EEE    C      AAAAA    T    EEE    D   D
# D   D  E      P      R   R  E      C      A   A    T    E      D   D
# D   D  E      P      R   R  E       C  C  A   A    T    E      D   D
# DDDD   EEEEE  P      R   R  EEEEE    CC   A   A    T    EEEEE  DDDD 
# 
# DEPRECATED:  This was replaced by Sp0_Set_Idx_by_DegDiv
#
# Sp0_Set_Idx_by_Deg
# Purpose:              This is used to set the rotational distance
#                       measurement as degrees for the Sp0 & Sp1
#                       spindles.
# Updated:              ver 1.0, 26 December 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Rotary
#                       REB_Tab_Sync
#   Button:             Sp0_Set_Idx_by_Deg  (HAL_RadioButton)
#   Signal:             GtkWidget/button-press-event
# ---------------------------------------------------------------------
# Data
#   Read from UI:       (none)
#   Program Variables
#       Referenced:     self.Sp0_Idx_Dist - distance field data
#       Set:            self.Sp0_Idx_Deg - degrees to index
#                       self.Sp0_Idx_DegDiv - type of distance
#                           measurement (Deg or Div)
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        (none)
#######################################################################
    def Sp0_Set_Idx_by_Deg(self,widget):

        print("=================================================")
        print("FUNCTION Sp0_Set_Idx_by_Deg")

        self.Sp0_Idx_DegDiv = "Deg"
        self.Sp0_Idx_Deg = self.Sp0_Idx_Dist

        Prt1 = "Sp0_Idx_DegDiv = " + self.Sp0_Idx_DegDiv
        print(Prt1)
        Prt2 = "Sp0_Idx_Deg = " + str(self.Sp0_Idx_Deg) + " deg"
        print(Prt2)

#######################################################################
# Sp0_Set_Idx_by_DegDiv
# Purpose:              This is used to set the rotational distance
#                       measurement for the Sp0 & Sp1 spindles.
#                       If degrees, set to divisions; 
#                       if divisions, set to degrees.
# Updated:              ver 1.0, 26 December 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Rotary
#                       REB_Tab_Sync
#   Button:             Sp0_Set_Idx_by_Deg  (HAL_RadioButton)
#   Signal:             GtkWidget/button-press-event
# ---------------------------------------------------------------------
# Data
#   Read from UI:       (none)
#   Program Variables
#       Referenced:     self.Sp0_Idx_Dist - distance field data
#       Set:            self.Sp0_Idx_Deg - degrees to index
#                       self.Sp0_Idx_DegDiv - type of distance
#                           measurement (Deg or Div)
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        (none)
#######################################################################
    def Sp0_Set_Idx_by_DegDiv(self,widget):

        print("=================================================")
        print("FUNCTION Sp0_Set_Idx_by_DegDiv")

        if self.Sp0_Idx_DegDiv == "Deg":
		        self.Sp0_Idx_DegDiv = "Div"
		        self.Sp0_Idx_Deg = round(360 / self.Sp0_Idx_Dist, 1)
        else:
		        self.Sp0_Idx_DegDiv = "Deg"
		        self.Sp0_Idx_Deg = round(self.Sp0_Idx_Dist, 1)

        Prt1 = "Sp0_Idx_Deg = " + str(self.Sp0_Idx_Deg)
        print(Prt1)

        Prt2 = "self.Sp0_Idx_DegDiv = " + self.Sp0_Idx_DegDiv
        print(Prt2)

#######################################################################
# DDDD   EEEEE  PPPP   RRRR   EEEEE    CC    AAA   TTTTT  EEEEE  DDDD 
# D   D  E      P   P  R   R  E       C  C  A   A    T    E      D   D
# D   D  E      P   P  R   R  E      C      A   A    T    E      D   D
# D   D  EEE    PPPP   RRRR   EEE    C      AAAAA    T    EEE    D   D
# D   D  E      P      R   R  E      C      A   A    T    E      D   D
# D   D  E      P      R   R  E       C  C  A   A    T    E      D   D
# DDDD   EEEEE  P      R   R  EEEEE    CC   A   A    T    EEEEE  DDDD 
# 
# DEPRECATED:  This was replaced by Sp0_Set_Idx_by_DegDiv
#
# Sp0_Set_Idx_by_Div
# Purpose:              This is used to set the rotational distance
#                       measurement as divisions of a circle for the
#                       Sp0 & Sp1 spindles (deg = 360/div).
# Updated:              ver 1.0, 26 December 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Rotary
#                       REB_Tab_Sync
#   Button:             Sp0_Set_Idx_by_Div  (HAL_RadioButton)
#   Signal:             GtkWidget/button-press-event
# ---------------------------------------------------------------------
# Data
#   Read from UI:       (none)
#   Program Variables
#       Referenced:     self.Sp0_Idx_Dist - distance field data
#       Set:            self.Sp0_Idx_Deg - degrees to index
#                       self.Sp0_Idx_DegDiv - type of distance
#                           measurement (Deg or Div)
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        (none)
#######################################################################
    def Sp0_Set_Idx_by_Div(self,widget):

        print("=================================================")
        print("FUNCTION Sp0_Set_Idx_by_Div")

        self.Sp0_Idx_DegDiv = "Div"
        self.Sp0_Idx_Deg = 360 / self.Sp0_Idx_Dist

        Prt1 = "Sp0_Idx_DegDiv = " + self.Sp0_Idx_DegDiv
        print(Prt1)
        Prt2 = "Sp0_Idx_Deg = " + str(self.Sp0_Idx_Deg) + " deg"
        print(Prt2)

#######################################################################
# Sp0_Set_Idx_Dist
# Purpose:              This is used to set the distance that and index
#                           operation moves the spindles(s).  This is
#                           used with self.Sp0_Idx_DegDiv to set the
#                           actual movement distance.
# Updated:              ver 1.0, 26 December 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Base
#                       REB_Tab_Sync
#   Button:             Sp0_Set_Idx_Dist  (Hal_SpinButton)
#   Signal:             GtkSpinButton/value-changed
# ---------------------------------------------------------------------
# Data
#   Read from UI:       (none)
#   Program Variables
#       Referenced:     (none)
#       Set:            self.Sp0_Idx_Dist
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        (none)
#######################################################################
    def Sp0_Set_Idx_Dist(self,widget):

        print("=================================================")
        print("FUNCTION Sp0_Set_Idx_Dist")

        self.Sp0_Idx_Dist = round(widget.get_value(), 1)
        print("self.Sp0_Idx_Dist = " + str(self.Sp0_Idx_Dist))

#######################################################################
# Sp0_Set_Idx_OnOff
# Purpose:              This is used to set the use of Sp1 indexing
#                           on or off.
# Updated:              ver 1.0, 26 December 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Rotary
#                       REB_Tab_Sync
#   Button:             Sp0_Set_Idx_OnOff
#   Signal:             GtkToggleButton/toggled
# ---------------------------------------------------------------------
# Data
#   Read from UI:       (none)
#   Program Variables
#       Referenced:     (none)
#       Set:            self.Sp0_Idx_Bool
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        (none)
#######################################################################
    def Sp0_Set_Idx_OnOff(self,widget):

        print("=================================================")
        print("FUNCTION Sp0_Set_Idx_OnOff")

        if self.Sp0_Idx_Bool:
                self.Sp0_Idx_Bool = False
                print("Sp0_Idx_Bool = False")
        else:
                self.Sp0_Idx_Bool = True
                print("Sp0_Idx_Bool = True")

# ********************************************************************
#  SSSSSS  PPPPPPP  IIIIIIII N     NN DDDDDDD  LL       EEEEEEEE  1111
# SS    SS PP    PP    II    NN    NN DD    DD LL       EE       11 11
#  SSS     PP    PP    II    NNN   NN DD    DD LL       EEEEE       11
#     SSS  PPPPPPP     II    NN NN NN DD    DD LL       EE          11
# SS    SS PP          II    NN  NNNN DD    DD LL       EE          11
#  SSSSSS  PP       IIIIIIII NN    NN DDDDDDD  LLLLLLLL EEEEEEEE 11111111
# ********************************************************************

#######################################################################
# Sp1_Set_Idx_Dist
# Purpose:              This is used to set the rotational distance
#                           (degrees) for the Sp1 spindle (the
#                           rosette phaser/multiplier).
# Updated:              ver 1.0, 26 December 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Rotary
#   Button:             Sp1_Idx (on setting the value)
#   Signal:             GtkSpinButton/value-changed
# ---------------------------------------------------------------------
# Data
#   Read from UI:       Sp1_Idx
#   Program Variables
#       Referenced:     (none)
#       Set:            self.Sp1_Idx_Dist
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        (none)
#######################################################################
    def Sp1_Set_Idx_Dist(self,widget):

        print("=================================================")
        print("FUNCTION Sp1_Set_Idx_Dist")

        self.Sp1_Idx_Dist = widget.get_value()

#######################################################################
# Sp1_Set_Idx_OnOff
# Purpose:              This is used to set the use of Sp1 indexing
#                           on or off.
# Updated:              ver 1.0, 26 December 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Rotary
#   Button:             Sp1_Set_Idx_OnOff
#   Signal:             GtkToggleButton/toggled
# ---------------------------------------------------------------------
# Data
#   Read from UI:       (none)
#   Program Variables
#       Referenced:     (none)
#       Set:            self.Sp1_Idx_Bool
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        (none)
#######################################################################
    def Sp1_Set_Idx_OnOff(self,widget):

        print("=================================================")
        print("FUNCTION Sp1_Set_Idx_OnOff")

        if self.Sp1_Idx_Bool:
                self.Sp1_Idx_Bool = False
                print("Sp1_Idx_Bool = False")
        else:
                self.Sp1_Idx_Bool = True
                print("Sp1_Idx_Bool = True")

#######################################################################
# Sp1_Set_Move_Pct
# Purpose:              This is used to set the speed for the rosette
#                           phaser / multiplier (Sp0) as a percentage
#                           of the spindle speed.
# Updated:              ver 1.0, 26 December 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Base
#   Button:             Sp1_Set_Move_Pct  (Hal_SpinButton)
#   Signal:             GtkSpinButton/value-changed
# ---------------------------------------------------------------------
# Data
#   Read from UI:       (none)
#   Program Variables
#       Referenced:     (none)
#       Set:            self.Sp1_Pct
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        S
#######################################################################
    def Sp1_Set_Move_Pct(self,widget):

        print("=================================================")
        print("FUNCTION Sp1_Set_Move_Pct")

        self.Sp1_Pct = round(widget.get_value(), 2)
        Sp1_Feed = round(self.Sp0_Feed * self.Sp1_Pct / 100, 2)

        Gcode1 = "S" + str(Sp1_Feed) + " $1"

        print("self.Sp0_Feed = " + str(self.Sp0_Feed))
        print("self.Sp1_Pct = " + str(self.Sp1_Pct))
        print("Sp1_Feed = " + str(Sp1_Feed))

        # Ensure the system is in MDI mode
        s.poll()
        if s.task_state != linuxcnc.MODE_MDI:
                c.mode(linuxcnc.MODE_MDI)
                c.wait_complete() # Wait for mode change to complete

        # Send an MDI command to set the spindle speed.
        print(Gcode1)
        c.mdi(Gcode1)

        # Wait for the command to complete
        c.wait_complete()

# ********************************************************************
#    AA    XX    XX IIIIIIII  SSSSSS      UU    UU
#   AAAA    XX  XX    II     SS    SS     UU    UU
#  AA  AA    XXXX     II      SSS         UU    UU
# AAAAAAAA   XXXX     II         SSS      UU    UU
# AA    AA  XX  XX    II     SS    SS     UU    UU
# AA    AA XX    XX IIIIIIII  SSSSSS       UUUUUU
# ********************************************************************

#######################################################################
# U_Move_Minus
# Purpose:              This is used to index the U axis in the
#                           minus direction.
# Updated:              ver 1.0, 26 December 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Rotary
#   Button:             U_Idx_Minus
#   Signal:
# ---------------------------------------------------------------------
# Data
#   Read from UI:       (none)
#   Program Variables
#       Referenced:     self.U_Feed
#                       self.U_Idx
#       Set:            (none)
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        G0
#######################################################################
    def U_Move_Minus(self,widget):

        print("=================================================")
        print("FUNCTION U_Move_Minus")

        # Ensure the system is in MDI mode
        s.poll()
        if s.task_state != linuxcnc.MODE_MDI:
                c.mode(linuxcnc.MODE_MDI)
                c.wait_complete() # Wait for mode change to complete

        # Send an MDI command to move along the axis.
        Gcode = "G0 U-" + str(self.U_Idx_Dist) + " F" + str(self.U_Feed)

        print(Gcode)
        c.mdi(Gcode)

        # Wait for the command to complete
        c.wait_complete()

#######################################################################
# U_Move_Plus
# Purpose:              This is used to index the U axis in the
#                           plus direction.
# Updated:              ver 1.0, 26 December 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Rotary
#   Button:             U_Idx_Plus
#   Signal:
# ---------------------------------------------------------------------
# Data
#   Read from UI:       (none)
#   Program Variables
#       Referenced:     self.U_Feed
#                       self.U_Idx_Dist
#       Set:            (none)
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        G0
#######################################################################
    def U_Move_Plus(self,widget):

        print("=================================================")
        print("FUNCTION U_Move_Plus")

        # Ensure the system is in MDI mode
        s.poll()
        if s.task_state != linuxcnc.MODE_MDI:
                c.mode(linuxcnc.MODE_MDI)
                c.wait_complete() # Wait for mode change to complete

        # Send an MDI command to move along the axis.
        Gcode = "G0 U" + str(self.U_Idx_Dist) + " F" + str(self.U_Feed)

        print(Gcode)
        c.mdi(Gcode)

        # Wait for the command to complete
        c.wait_complete()

#######################################################################
# U_Set_Feed
# Purpose:              This is used to set the movement speed for the
#                           U axis.
# Updated:              ver 1.0, 26 December 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Linear
#   Button:             U_Feed (on setting the value)
#   Signal:             GtkSpinButton/value-changed
# ---------------------------------------------------------------------
# Data
#   Read from UI:       U_Feed
#   Program Variables
#       Referenced:     (none)
#       Set:            self.U_Feed
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        (none)
#######################################################################
    def U_Set_Feed(self,widget):

        print("=================================================")
        print("FUNCTION U_Set_Feed")

        self.U_Feed = round(widget.get_value(), 1)

        print("U_Set_Feed =")
        print(self.U_Feed)

#######################################################################
# U_Set_Idx_Dist
# Purpose:              This is used to set the movement distance for
#                           the U axis.
# Updated:              ver 1.0, 26 December 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Linear
#   Button:             U_Idx_Dist (on setting the value)
#   Signal:             GtkSpinButton/value-changed
# ---------------------------------------------------------------------
# Data
#   Read from UI:       U_Idx_Dist
#   Program Variables
#       Referenced:     (none)
#       Set:            self.U_Idx_Dist
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        (none)
#######################################################################
    def U_Set_Idx_Dist(self,widget):

        print("=================================================")
        print("FUNCTION U_Set_Idx_Dist")

        self.U_Idx_Dist = widget.get_value()

        print("U_Idx_Dist_chg_value =")
        print(self.U_Idx_Dist)

#######################################################################
# U_Set_Move_Dist
# Purpose:              This is used to set the movement distance for
#                           the U axis.
# Updated:              ver 1.0, 26 December 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Sync
#   Button:             U_Move_Dist (on setting the value)
#   Signal:             GtkSpinButton/value-changed
# ---------------------------------------------------------------------
# Data
#   Read from UI:       U_Move_Dist
#   Program Variables
#       Referenced:     (none)
#       Set:            self.U_Move_Dist
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        (none)
#######################################################################
    def U_Set_Move_Dist(self,widget):

        print("=================================================")
        print("FUNCTION U_Set_Move_Dist")

        self.U_Move_Dist = widget.get_value()

        print("U_Move_Dist = " + str(self.U_Move_Dist))

#######################################################################
# U_Set_Sync_OnOff
# Purpose:              This is used to identify if this axis should
#                           synchronized with the Spindle (or not).
# Updated:              ver 1.0, 26 December 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Sync
#   Button:             U_Sync_OnOff
#   Signal:             GtkToggleButton/toggled
# ---------------------------------------------------------------------
# Data
#   Read from UI:       (none)
#   Program Variables
#       Referenced:     (none)
#       Set:            self.U_Sync_Bool
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        (none)
#######################################################################
    def U_Set_Sync_OnOff(self,widget):

        print("=================================================")
        print("FUNCTION U_Set_Sync_OnOff")

        if self.U_Sync_Bool:
                self.U_Sync_Bool = False
                print("U_Sync_Bool = False")
        else:
                self.U_Sync_Bool = True
                print("U_Sync_Bool = True")

# ********************************************************************
#    AA    XX    XX IIIIIIII  SSSSSS      VV    VV
#   AAAA    XX  XX    II     SS    SS     VV    VV
#  AA  AA    XXXX     II      SSS         VV    VV
# AAAAAAAA   XXXX     II         SSS       VV  VV
# AA    AA  XX  XX    II     SS    SS       VVVV
# AA    AA XX    XX IIIIIIII  SSSSSS         VV
# ********************************************************************

#######################################################################
# V_Move_Minus
# Purpose:              This is used to index the V axis in the
#                           minus direction.
# Updated:              ver 1.0, 26 December 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Rotary
#   Button:             V_Idx_Minus
#   Signal:
# ---------------------------------------------------------------------
# Data
#   Read from UI:       (none)
#   Program Variables
#       Referenced:     self.V_Feed
#                       self.V_Idx_Dist
#       Set:            (none)
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        (none)
#######################################################################
    def V_Move_Minus(self,widget):

        print("=================================================")
        print("FUNCTION V_Move_Minus")

        # Ensure the system is in MDI mode
        s.poll()
        if s.task_state != linuxcnc.MODE_MDI:
                c.mode(linuxcnc.MODE_MDI)
                c.wait_complete() # Wait for mode change to complete

        # Send an MDI command to move along the axis.
        Gcode = "G0 V-" + str(self.V_Idx) + " F" + str(self.V_Feed)

        print(Gcode)
        c.mdi(Gcode)

        # Wait for the command to complete
        c.wait_complete()

#######################################################################
# V_Move_Plus
# Purpose:              This is used to index the V axis in the
#                           plus direction.
# Updated:              ver 1.0, 26 December 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Rotary
#   Button:             V_Idx_Plus
#   Signal:
# ---------------------------------------------------------------------
# Data
#   Read from UI:       (none)
#   Program Variables
#       Referenced:     self.V_Feed
#                       self.V_Idx_Dist
#       Set:            (none)
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        (none)
#######################################################################
    def V_Move_Plus(self,widget):

        print("=================================================")
        print("FUNCTION V_Move_Plus")

        # Ensure the system is in MDI mode
        s.poll()
        if s.task_state != linuxcnc.MODE_MDI:
                c.mode(linuxcnc.MODE_MDI)
                c.wait_complete() # Wait for mode change to complete

        # Send an MDI command to move along the axis.
        Gcode = "G0 V" + str(self.V_Idx_Dist) + " F" + str(self.V_Feed)

        print(Gcode)
        c.mdi(Gcode)

        # Wait for the command to complete
        c.wait_complete()

#######################################################################
# V_Set_Feed
# Purpose:              This is used to set the movement speed for the
#                           V axis.
# Updated:              ver 1.0, 26 December 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Linear
#   Button:             V_Feed (on setting the value)
#   Signal:             GtkSpinButton/value-changed
# ---------------------------------------------------------------------
# Data
#   Read from UI:       V_Feed
#   Program Variables
#       Referenced:     (none)
#       Set:            self.V_Feed
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        (none)
#######################################################################
    def V_Set_Feed(self,widget):

        print("=================================================")
        print("FUNCTION V_Set_Feed")

        self.V_Feed = round(widget.get_value(), 1)

        print("V_Set_Feed =")
        print(self.V_Feed)

#######################################################################
# V_Set_Idx_Dist
# Purpose:              This is used to set the movement distance for
#                           the V axis.
# Updated:              ver 1.0, 26 December 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Linear
#   Button:             V_Idx_Dist (on setting the value)
#   Signal:             GtkSpinButton/value-changed
# ---------------------------------------------------------------------
# Data
#   Read from UI:       V_Idx_Dist
#   Program Variables
#       Referenced:     (none)
#       Set:            self.V_Idx_Dist
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        (none)
#######################################################################
    def V_Set_Idx_Dist(self,widget):

        print("=================================================")
        print("FUNCTION V_Set_Idx_Dist")

        self.V_Idx_Dist = widget.get_value()

        print("V_Idx_Dist =")
        print(self.V_Idx_Dist)

#######################################################################
# V_Set_Move_Dist
# Purpose:              This is used to set the movement distance for
#                           the V axis.
# Updated:              ver 1.0, 26 December 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Sync
#   Button:             U_Move_Dist (on setting the value)
#   Signal:             GtkSpinButton/value-changed
# ---------------------------------------------------------------------
# Data
#   Read from UI:       V_Move_Dist
#   Program Variables
#       Referenced:     (none)
#       Set:            self.V_Move_Dist
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        (none)
#######################################################################
    def V_Set_Move_Dist(self,widget):

        print("=================================================")
        print("FUNCTION V_Set_Move_Dist")

        self.V_Move_Dist = widget.get_value()

        print("V_Move_Dist = " + str(self.V_Move_Dist))

#######################################################################
# V_Set_Sync_OnOff
# Purpose:              This is used to identify if this axis should
#                           synchronized with the Spindle (or not).
# Updated:              ver 1.0, 26 December 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Sync
#   Button:             V_Sync_OnOff
#   Signal:             GtkToggleButton/toggled
# ---------------------------------------------------------------------
# Data
#   Read from UI:       (none)
#   Program Variables
#       Referenced:     (none)
#       Set:            self.V_Sync_Bool
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        (none)
#######################################################################
    def V_Set_Sync_OnOff(self,widget):

        print("=================================================")
        print("FUNCTION V_Set_Sync_OnOff")

        if self.V_Sync_Bool:
                self.V_Sync_Bool = False
                print("V_Sync_Bool = False")
        else:
                self.V_Sync_Bool = True
                print("V_Sync_Bool = True")

# ********************************************************************
#    AA    XX    XX IIIIIIII  SSSSSS      YY    YY
#   AAAA    XX  XX    II     SS    SS      YY  YY
#  AA  AA    XXXX     II      SSS           YYYY
# AAAAAAAA   XXXX     II         SSS        XXXX
# AA    AA  XX  XX    II     SS    SS      XX   XX
# AA    AA XX    XX IIIIIIII  SSSSSS      XX     XX
# ********************************************************************

#######################################################################
# X_Move_Minus
# Purpose:              This is used to index the X axis in the
#                           minus direction.
# Updated:              ver 1.0, 26 December 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Rotary
#   Button:             X_Idx_Minus
#   Signal:             GtkButton/pressed
# ---------------------------------------------------------------------
# Data
#   Read from UI:       (none)
#   Program Variables
#       Referenced:     self.X_Feed
#                       self.X_Idx_Dist
#       Set:            (none)
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        G0
#######################################################################
    def X_Move_Minus(self,widget):

        print("=================================================")
        print("FUNCTION X_Move_Minus")

        # Ensure the system is in MDI mode
        s.poll()
        if s.task_state != linuxcnc.MODE_MDI:
                c.mode(linuxcnc.MODE_MDI)
                c.wait_complete() # Wait for mode change to complete

        # Send an MDI command to move along the axis.
        Gcode = "G0 X-" + str(self.X_Idx_Dist) + " F" + str(self.X_Feed)

        print(Gcode)
        c.mdi(Gcode)

        # Wait for the command to complete
        c.wait_complete()

#######################################################################
# X_Move_Plus
# Purpose:              This is used to index the X axis in the
#                           plus direction.
# Updated:              ver 1.0, 26 December 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Rotary
#   Button:             X_Idx_Plus
#   Signal:
# ---------------------------------------------------------------------
# Data
#   Read from UI:       (none)
#   Program Variables
#       Referenced:     self.X_Feed
#                       self.X_Idx_Dist
#       Set:            (none)
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        G0
#######################################################################
    def X_Move_Plus(self,widget):

        print("=================================================")
        print("FUNCTION _Move_Plus")

        # Ensure the system is in MDI mode
        s.poll()
        if s.task_state != linuxcnc.MODE_MDI:
                c.mode(linuxcnc.MODE_MDI)
                c.wait_complete() # Wait for mode change to complete

        # Send an MDI command to move along the axis.
        Gcode = "G0 X" + str(self.X_Idx_Dist) + " F" + str(self.X_Feed)

        print(Gcode)
        c.mdi(Gcode)

        # Wait for the command to complete
        c.wait_complete()

#######################################################################
# X_Set_Feed
# Purpose:              This is used to set the movement speed for the
#                           X axis.
# Updated:              ver 1.0, 26 December 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Linear
#   Button:             X_Feed (on setting the value)
#   Signal:             GtkSpinButton/value-changed
# ---------------------------------------------------------------------
# Data
#   Read from UI:       X_Feed
#   Program Variables
#       Referenced:     (none)
#       Set:            self.X_Feed
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        (none)
#######################################################################
    def X_Set_Feed(self,widget):

        print("=================================================")
        print("FUNCTION X_Set_Feed")

        self.X_Feed = round(widget.get_value(), 1)

        print("X_Set_Feed =")
        print(self.X_Feed)

#######################################################################
# X_Set_Idx_Dist
# Purpose:              This is used to set the movement distance for
#                           the X axis.
# Updated:              ver 1.0, 26 December 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Linear
#   Button:             X_Idx_Dist (on setting the value)
#   Signal:             GtkSpinButton/value-changed
# ---------------------------------------------------------------------
# Data
#   Read from UI:       X_Idx_Dist
#   Program Variables
#       Referenced:     (none)
#       Set:            self.X_Idx_Dist
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        (none)
#######################################################################
    def X_Set_Idx_Dist(self,widget):

        print("=================================================")
        print("FUNCTION X_Set_Idx_Dist")

        self.X_Idx_Dist = widget.get_value()

        print("X_Idx_Dist =")
        print(self.X_Idx_Dist)

#######################################################################
# X_Set_Move_Dist
# Purpose:              This is used to set the movement distance for
#                           the X axis.
# Updated:              ver 1.0, 26 December 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Sync
#   Button:             X_Move_Dist (on setting the value)
#   Signal:             GtkSpinButton/value-changed
# ---------------------------------------------------------------------
# Data
#   Read from UI:       X_Move_Dist
#   Program Variables
#       Referenced:     (none)
#       Set:            self.X_Move_Dist
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        (none)
#######################################################################
    def X_Set_Move_Dist(self,widget):

        print("=================================================")
        print("FUNCTION X_Set_Move_Dist")

        self.X_Move_Dist = widget.get_value()

        print("X_Move_Dist = " + str(self.X_Move_Dist))

#######################################################################
# X_Set_Sync_OnOff
# Purpose:              This is used to identify if this axis should
#                           synchronized with the Spindle (or not).
# Updated:              ver 1.0, 26 December 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Sync
#   Button:             X_Sync_OnOff
#   Signal:             GtkToggleButton/toggled
# ---------------------------------------------------------------------
# Data
#   Read from UI:       (none)
#   Program Variables
#       Referenced:     (none)
#       Set:            self.X_Sync_Bool
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        (none)
#######################################################################
    def X_Set_Sync_OnOff(self,widget):

        print("=================================================")
        print("FUNCTION X_Set_Sync_OnOff")

        if self.X_Sync_Bool:
                self.X_Sync_Bool = False
                print("X_Sync_Bool = False")
        else:
                self.X_Sync_Bool = True
                print("X_Sync_Bool = True")

# ********************************************************************
#    AA    XX    XX IIIIIIII  SSSSSS      YY    YY
#   AAAA    XX  XX    II     SS    SS      YY  YY
#  AA  AA    XXXX     II      SSS           YYYY
# AAAAAAAA   XXXX     II         SSS         YY
# AA    AA  XX  XX    II     SS    SS        YY
# AA    AA XX    XX IIIIIIII  SSSSSS         YY
# ********************************************************************

#######################################################################
# Y_Move_Minus
# Purpose:              This is used to index the Y axis in the
#                           minus direction.
# Updated:              ver 1.0, 26 December 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Rotary
#   Button:             Y_Idx_Minus
#   Signal:
# ---------------------------------------------------------------------
# Data
#   Read from UI:       (none)
#   Program Variables
#       Referenced:     self.Y_Feed
#                       self.Y_Idx_Dist
#       Set:            (none)
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        G0
#######################################################################
    def Y_Move_Minus(self,widget):

        print("=================================================")
        print("FUNCTION Y_Move_Minus")

        # Ensure the system is in MDI mode
        s.poll()
        if s.task_state != linuxcnc.MODE_MDI:
                c.mode(linuxcnc.MODE_MDI)
                c.wait_complete() # Wait for mode change to complete

        # Send an MDI command to move along the axis.
        Gcode = "G0 Y-" + str(self.Y_Idx_Dist) + " F" + str(self.Y_Feed)

        print(Gcode)
        c.mdi(Gcode)

        # Wait for the command to complete
        c.wait_complete()

#######################################################################
# Y_Move_Plus
# Purpose:              This is used to index the Y axis in the
#                           plus direction.
# Updated:              ver 1.0, 26 December 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Rotary
#   Button:             Y_Idx_Plus
#   Signal:
# ---------------------------------------------------------------------
# Data
#   Read from UI:       (none)
#   Program Variables
#       Referenced:     self.Y_Feed
#                       self.Y_Idx_Dist
#       Set:            (none)
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        G0
#######################################################################
    def Y_Move_Plus(self,widget):

        print("=================================================")
        print("FUNCTION Y_Move_Plus")

        # Ensure the system is in MDI mode
        s.poll()
        if s.task_state != linuxcnc.MODE_MDI:
                c.mode(linuxcnc.MODE_MDI)
                c.wait_complete() # Wait for mode change to complete

        # Send an MDI command to move along the axis.
        Gcode = "G0 Y" + str(self.Y_Idx_Dist) + " F" + str(self.Y_Feed)

        print(Gcode)
        c.mdi(Gcode)

        # Wait for the command to complete
        c.wait_complete()

#######################################################################
# Y_Set_Feed
# Purpose:              This is used to set the movement speed for the
#                           Y axis.
# Updated:              ver 1.0, 26 December 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Linear
#   Button:             Y_Feed (on setting the value)
#   Signal:             GtkSpinButton/value-changed
# ---------------------------------------------------------------------
# Data
#   Read from UI:       Y_Feed
#   Program Variables
#       Referenced:     (none)
#       Set:            self.Y_Feed
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        M5
#######################################################################
    def Y_Set_Feed(self,widget):

        print("=================================================")
        print("FUNCTION Y_Set_Feed")

        self.Y_Feed = round(widget.get_value(), 1)

        print("Y_Set_Feed =")
        print(self.Y_Feed)

#######################################################################
# Y_Set_Idx_Dist
# Purpose:              This is used to set the movement distance for
#                           the Y axis.
# Updated:              ver 1.0, 26 December 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Linear
#   Button:             Y_Idx_Dist (on setting the value)
#   Signal:             GtkSpinButton/value-changed
# ---------------------------------------------------------------------
# Data
#   Read from UI:       Y_Idx_Dist
#   Program Variables
#       Referenced:     self.Y_Idx_Dist
#       Set:            (none)
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        M5
#######################################################################
    def Y_Set_Idx_Dist(self,widget):

        print("=================================================")
        print("FUNCTION B_Set_Idx_Dist_by_Deg")

        self.Y_Idx_Dist = widget.get_value()

        print("Y_Idx_Dist =")
        print(self.Y_Idx_Dist)

#######################################################################
# Y_Set_Move_Dist
# Purpose:              This is used to set the movement distance for
#                           the Y axis.
# Updated:              ver 1.0, 26 December 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Sync
#   Button:             Y_Move_Dist (on setting the value)
#   Signal:             GtkSpinButton/value-changed
# ---------------------------------------------------------------------
# Data
#   Read from UI:       Y_Move_Dist
#   Program Variables
#       Referenced:     (none)
#       Set:            self.Y_Move_Dist
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        (none)
#######################################################################
    def Y_Set_Move_Dist(self,widget):

        print("=================================================")
        print("FUNCTION Y_Set_Move_Dist")

        self.Y_Move_Dist = widget.get_value()

        print("Y_Move_Dist = " + str(self.Y_Move_Dist))

#######################################################################
# Y_Set_Sync_OnOff
# Purpose:              This is used to identify if this axis should
#                           synchronized with the Spindle (or not).
# Updated:              ver 1.0, 26 December 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Sync
#   Button:             Y_Sync_OnOff
#   Signal:             GtkToggleButton/toggled
# ---------------------------------------------------------------------
# Data
#   Read from UI:       (none)
#   Program Variables
#       Referenced:     (none)
#       Set:            self.Y_Sync_Bool
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        (none)
#######################################################################
    def Y_Set_Sync_OnOff(self,widget):

        print("=================================================")
        print("FUNCTION Y_Set_Sync_OnOff")

        if self.Y_Sync_Bool:
                self.Y_Sync_Bool = False
                print("Y_Sync_Bool = False")
        else:
                self.Y_Sync_Bool = True
                print("Y_Sync_Bool = True")

# ********************************************************************
#    AA    XX    XX IIIIIIII  SSSSSS      ZZZZZZZZ
#   AAAA    XX  XX    II     SS    SS          ZZ
#  AA  AA    XXXX     II      SSS             ZZ
# AAAAAAAA   XXXX     II         SSS        ZZ
# AA    AA  XX  XX    II     SS    SS      ZZ
# AA    AA XX    XX IIIIIIII  SSSSSS      ZZZZZZZZ
# ********************************************************************

#######################################################################
# Z_Move_Minus
# Purpose:              This is used to index the Z axis in the
#                           minus direction.
# Updated:              ver 1.0, 26 December 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Rotary
#   Button:             Z_Idx_Minus
#   Signal:
# ---------------------------------------------------------------------
# Data
#   Read from UI:       (none)
#   Program Variables
#       Referenced:     self.Z_Feed
#                       self.Z_Idx_Dist
#       Set:            (none)
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        G0
#######################################################################
    def Z_Move_Minus(self,widget):

        print("=================================================")
        print("FUNCTION Z_Move_Minus")

        # Ensure the system is in MDI mode
        s.poll()
        if s.task_state != linuxcnc.MODE_MDI:
                c.mode(linuxcnc.MODE_MDI)
                c.wait_complete() # Wait for mode change to complete

        # Send an MDI command to move along the axis.
        Gcode = "G0 Z-" + str(self.Z_Idx_Dist) + " F" + str(self.Z_Feed)

        print(Gcode)
        c.mdi(Gcode)

        # Wait for the command to complete
        c.wait_complete()

#######################################################################
# Z_Move_Plus
# Purpose:              This is used to index the Z axis in the
#                           plus direction.
# Updated:              ver 1.0, 26 December 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Rotary
#   Button:             Z_Idx_Plus
#   Signal:
# ---------------------------------------------------------------------
# Data
#   Read from UI:       (none)
#   Program Variables
#       Referenced:     self.Z_Feed
#                       self.Z_Idx_Dist
#       Set:            (none)
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        G0
#######################################################################
    def Z_Move_Plus(self,widget):

        print("=================================================")
        print("FUNCTION Z_Move_Plus")

        # Ensure the system is in MDI mode
        s.poll()
        if s.task_state != linuxcnc.MODE_MDI:
                c.mode(linuxcnc.MODE_MDI)
                c.wait_complete() # Wait for mode change to complete

        # Send an MDI command to move along the axis.
        Gcode = "G0 Z" + str(self.Z_Idx_Dist) + " F" + str(self.Z_Feed)

        print(Gcode)
        c.mdi(Gcode)

        # Wait for the command to complete
        c.wait_complete()

#######################################################################
# Z_Set_Feed
# Purpose:              This is used to set the movement speed for the
#                           Z axis.
# Updated:              ver 1.0, 26 December 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Linear
#   Button:             Z_Feed (on setting the value)
#   Signal:             GtkSpinButton/value-changed
# ---------------------------------------------------------------------
# Data
#   Read from UI:       Z_Feed
#   Program Variables
#       Referenced:     (none)
#       Set:            self.Z_Feed
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        M5
#######################################################################
    def Z_Set_Feed(self,widget):

        print("=================================================")
        print("FUNCTION Z_Set_Feed")

        self.Z_Feed = round(widget.get_value(), 1)

        print("Z_Set_Feed =")
        print(self.Z_Feed)

#######################################################################
# Z_Set_Idx_Dist
# Purpose:              This is used to set the movement distance for
#                           the Z axis.
# Updated:              ver 1.0, 26 December 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Linear
#   Button:             Z_Idx_Dist (on setting the value)
#   Signal:             GtkSpinButton/value-changed
# ---------------------------------------------------------------------
# Data
#   Read from UI:       Z_Idx_Dist
#   Program Variables
#       Referenced:     (none)
#       Set:            self.Z_Idx_Dist
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        M5
#######################################################################
    def Z_Set_Idx_Dist(self,widget):

        print("=================================================")
        print("FUNCTION Z_Set_Idx_Dist")

        self.Z_Idx_Dist = widget.get_value()

        print("Z_Idx_Dist =")
        print(self.Z_Idx_Dist)

#######################################################################
# Z_Set_Move_Dist
# Purpose:              This is used to set the movement distance for
#                           the Z axis.
# Updated:              ver 1.0, 26 December 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Sync
#   Button:             Z_Move_Dist (on setting the value)
#   Signal:             GtkSpinButton/value-changed
# ---------------------------------------------------------------------
# Data
#   Read from UI:       Z_Move_Dist
#   Program Variables
#       Referenced:     (none)
#       Set:            self.Z_Move_Dist
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        (none)
#######################################################################
    def Z_Set_Move_Dist(self,widget):

        print("=================================================")
        print("FUNCTION Z_Set_Move_Dist")

        self.Z_Move_Dist = widget.get_value()

        print("Z_Move_Dist = " + str(self.Z_Move_Dist))

#######################################################################
# Z_Set_Sync_OnOff
# Purpose:              This is used to identify if this axis should
#                           synchronized with the Spindle (or not).
# Updated:              ver 1.0, 26 December 2025, R. Colvin
# ---------------------------------------------------------------------
# Called from:
#   UI:                 REB_Tab_Sync
#   Button:             Z_Sync_OnOff
#   Signal:             GtkToggleButton/toggled
# ---------------------------------------------------------------------
# Data
#   Read from UI:       (none)
#   Program Variables
#       Referenced:     (none)
#       Set:            self.Z_Sync_Bool
#   Written to UI:      (none)
# ---------------------------------------------------------------------
# Gcodes Called:        (none)
#######################################################################
    def Z_Set_Sync_OnOff(self,widget):

        print("=================================================")
        print("FUNCTION Z_Set_Sync_OnOff")

        if self.Z_Sync_Bool:
                self.Z_Sync_Bool = False
                print("Z_Sync_Bool = False")
        else:
                self.Y_Sync_Bool = True
                print("Z_Sync_Bool = True")


#######################################################################
# __init__
# Purpose:              This is used to initialize everything.
# Updated:              ver 1.0, 26 December 2025, R. Colvin
#######################################################################
    def __init__(self, halcomp,builder,useropts):
        '''
        Handler classes are instantiated in the following state:
        - the widget tree is created, but not yet realized (no toplevel window.show() executed yet)
        - the halcomp HAL component is set up and the widhget tree's HAL pins have already been added to it
        - it is safe to add more hal pins because halcomp.ready() has not yet been called at this point.

        after all handlers are instantiated in command line and get_handlers() order, callbacks will be
        connected with connect_signals()/signal_autoconnect()

        The builder may be either of libglade or GtkBuilder type depending on the glade file format.
        '''

        self.halcomp        = halcomp
        self.builder        = builder
        self.nhits          = 0

        ###############################################################
        # Global Program Variables - declare and set initial value.
        ###############################################################

        self.B_Feed         = 10.0      # B axis feed rate
        self.B_Idx_Deg      = 90.0      # B axis index degrees
        self.B_Idx_DegDiv   = "Deg"     # B axis index by degrees or divisions
        self.B_Idx_Dist     = 90.0      # B axis index distance
        self.B_Idx_Qty      = 0         # B axis index counter
        self.B_Move_Dist    = 0.0       # B axis move distance
        self.B_Sync_Bool    = False     # Sync this axis with the spindle?

        self.Sp0_Feed       = 1.0       # Sp0 Speed
        self.Sp0_Idx_Bool   = False     # Index this spindle?
        self.Sp0_Idx_DegDiv = "Deg"     # Sp0 & Sp1 spindles: index by degrees or divisions
        self.Sp0_Idx_Deg    = 90.0      # Sp0 index degrees
        self.Sp0_Idx_Dist   = 90.0      # B axis index distance
        self.Sp0_Idx_Qty    = 0         # Sp0 axis index counter
        self.Sp0_Sync_Bool  = False     # Sync this spindle with the axes?

        self.Sp1_Idx_Bool   = False     # Index this spindle?
        self.Sp1_Idx_Dist   = 90.0      # Sp1 index degrees
        self.Sp1_Idx_Qty    = 0         # Sp1 axis index counter
        self.Sp1_Pct        = 100.0     # Sp1 speed percentage of Sp0 speed
        self.Sp1_Sync_Bool  = False     # Sync this spindle with the axes?

        self.U_Feed         = 1.0       # U axis feed rate
        self.U_Idx_Dist     = 0.0       # U axis index distance
        self.U_Idx_Qty      = 0         # U axis index counter
        self.U_Move_Dist    = 0.0       # U axis move distance
        self.U_Sync_Bool    = False     # Sync this axis with the spindle?

        self.V_Feed         = 1.0       # V axis feed rate
        self.V_Idx_Dist     = 0.0       # V axis index distance
        self.V_Idx_Qty      = 0         # V axis index counter
        self.V_Move_Dist    = 0.0       # V axis move distance
        self.V_Sync_Bool    = False     # Sync this axis with the spindle?

        self.X_Feed         = 1.0       # X axis feed rate
        self.X_Idx_Dist     = 0.0       # X axis index distance
        self.X_Idx_Qty      = 0         # X axis index counter
        self.X_Move_Dist    = 0.0       # X axis move distance
        self.X_Sync_Bool    = False     # Sync this axis with the spindle?

        self.Y_Feed         = 1.0       # Y axis feed rate
        self.Y_Idx_Dist     = 0.0       # Y axis index distance
        self.Y_Idx_Qty      = 0         # Y axis index counter
        self.Y_Move_Dist    = 0.0       # Y axis move distance
        self.Y_Sync_Bool    = False     # Sync this axis with the spindle?

        self.Z_Feed         = 1.0       # Z axis feed rate
        self.Z_Idx_Dist     = 0.0       # Z axis index distance
        self.Z_Idx_Qty      = 0         # Z axis index counter
        self.Z_Move_Dist    = 0.0       # Z axis move distance
        self.Z_Sync_Bool    = False     # Sync this axis with the spindle?


def get_handlers(halcomp,builder,useropts):
    '''
    this function is called by gladevcp at import time (when this module is passed with '-u <modname>.py')

    return a list of object instances whose methods should be connected as callback handlers
    any method whose name does not begin with an underscore ('_') is a  callback candidate

    the 'get_handlers' name is reserved - gladevcp expects it, so do not change
    '''
    return [HandlerClass(halcomp,builder,useropts)]

#
