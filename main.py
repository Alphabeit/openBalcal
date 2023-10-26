#!./venv/bin python3
 # Creator: Christopher / Alphabeit
 # v0.0.1
 # last Update: 20231026

# from Functions import Report   # standard, report
from Functions import UserChoice   # Main function, Choice-Menu, starts all function for user



want_to_exit = False   # Loop condition, as long as False -> the loop will run --- the stop-order, resp. the True come from Module -> UserChoice

while not want_to_exit is True:
    # reports, give the curently status of money_balance
    # Reports.sss
    # Choice_Menu, starts all another functions
    want_to_exit = UserChoice.choice_menu()   # starts function and letzt return the loop condition



