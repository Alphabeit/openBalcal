#!/usr/bin/python3
 # Creator: Christopher / Alphabeit
 # v0.2.0
 # last Update: 20231227

from Functions import Menu, Reports
from Functions.lowerFunctions import Lang

print(Lang.Load_text("openBalcal.py", "text_1"))   # Welcome Message
print(Lang.Load_text("openBalcal.py", "text_2"))   # Info for Help

Reports.Report()   # Print the Reports

want_to_exit = False   # Loop condition, as long as False -> the loop will run --- the stop-order, resp. the True come from Module -> UserChoice
while not want_to_exit is True:
    # Choice_Menu, starts all another functions
    want_to_exit = Menu.Terminal_menu()  # starts function and returns the loop condition



