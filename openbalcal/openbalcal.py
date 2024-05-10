#!/usr/bin/python3
 # Creator: Christopher / Alphabeit
 # v0.3.0
 # last Update: 20240510

from funcs.main import menu_cli
from funcs.third import config

config.ProvideFiles()
config.UpdateOption()

menu_cli.CLI()
