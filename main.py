#!./venv/bin python3
 # Creator: Christopher / Alphabeit
 # v0.1.0
 # last Update: 20231029

from Functions import Menu   # Main function, Choice-Menu, starts all function for user



want_to_exit = False   # Loop condition, as long as False -> the loop will run --- the stop-order, resp. the True come from Module -> UserChoice

while not want_to_exit is True:
    # Choice_Menu, starts all another functions
    want_to_exit = Menu.Terminal_menu()  # starts function and letzt return the loop condition



