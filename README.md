# Open_Balancecalculation
A Python program for your own finances.

Most people do their accounting in tablesheets programs like Excel, if at all. It may be practical, but it could also be better. With too much time on my hands and even more interest in the Python language, this program was born. So this tool is used for cost accounting, how much money one has spent and how much is consequently still available. At the same time, the protection of your personal data is ensured, because the databases are created locally. No CLoud, but also no communication to the outside.



## Version
Each digit in the version number represents a development status. 

The last digit is incremented for bug fixes - means bugs were fixed but program was not extended. The second digit represents function updates. New functions, or new features that extend the program as such. Allows also new bugs. ;) The foremost digit represents the major version. When this is superscripted, we are talking about a major program change. For example, the addition of a GUI. "Don't ask me when this is coming". 

A major update could also change the program so much that the database from the previous versions is no longer compatible. In this case I would provide a function to adapt the database for the current version.

For the update histroy, look under "Info", in the file "Updatehistory.md".



#### newest Verison
v0.1.0

The first version of the program. The standard version, here we are begining. On this point, the program deliver everything what is needed to create and read your database. You can create entrys and calculade your balance based on them.

#### planed, next comming Version
v0.2.0

In the upcoming version, an automatic report is planned. So you should be able to see his balance, even without that they are explezit requested. 

Furthermore, I would also like to add a savings plan. Simple calculation: salary, minus savings target, minus expected expenses, minus current expenses, equal to residual value that can be spent. And these words I still need to rewrite in python code.  

Not to forget, at the current time, only options can be read, but not adjusted. At least not via the program. I would like to change this - the user should not be forced to do hardcoding.



## Install
Actually, we haven't a installer. Currently you need to install the program manuel, place the folder on a location, where you can finded again and start the main.py with python 3.



## Manuel
At the current time, this is a terminal-only program. Hardcore Linux users are probably already starting to drool. For the manual, start the program and use the command "help", or the corresponding command including the flag "-h", "--help" or "? 

Just try it, the program is self-explanatory. 



## Support
You want to support me, then take over the language packs. Text is designed so that it is not in the code, but in separate language files. You could adapt these according to your language. The original language file "en_US.xml" is felted with a bad english from me.

Other wishes or comments you can send me via "Issues".



## License
This project is licensed under the GPL-3.0 License.
