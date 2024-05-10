#!/usr/bin/python3
 # Creator: Christopher / Alphabeit
 # v0.3.0
 # last Update: 20240510

from openbalcal.funcs.main import menu_cli
from openbalcal.funcs.third import config

config.ProvideFiles_Config()
config.UpdateOption()
config.ProvideFiles_DBs()

menu_cli.CLI()
