# openBalcal
openBalcal, shourtform for Open_Balancecalculation, a Python program for your own finances.

Most people do their accounting in tablesheets programs like Excel, if at all. It may be practical, but it could also be better. With too much time on my hands and even more interest in the Python language, this program was born. This tool is used for cost accounting, how much money one has spent and how much is consequently still available. The databases is created locally - no Cloud, no communication to the outside.



## Version
Each digit in the version number represents a development status. 

The last digit is incremented for bug fixes - means bugs were fixed but program was not extended. The second digit represents function updates. New functions, or new features that extend the program as such. Allows also new bugs. ;) The foremost digit represents the major version. When this is superscripted, we are talking about a major program change. For example, the addition of a GUI. "Don't ask me when this is coming". 

For the update histroy, look the file "Updatehistory.md".



#### newest Verison
v0.3.0

- At first, I have write the programm from brand new. The language and config file are now `.yaml`, not `.xml` any more. The code is more clean and should be faster.

- Next, the program can now be installed und upgraded. See a step below at "Install & Upgrade". The installation is Linux only. The code will placed in `/usr/bin` and the database in your homedirectory `~/openbalcal`. If you want to upgrade the code, you can easy use the installprocess again. The code will be overwrite, the database not.

- The programm is under Linux now avalibale as command. So you dont need to go in a spezific folder anymore, or start explizit the script. Just enter `balcal` in terminal and here we go.

- At least, a `search` function have found this way in the tool. So you can filter your entrys based on some search criteria.

For the case, you have used the version v0.2.0 or older, you need the copy your database from the old folder, in the new folder inside your homedirectory.



#### planed, next comming Version
v0.4.0

It sould be possible to delete old entrys. To explicitly select entrys, I need to include Entry-IDs. Be prepared to reload the database, but I also write some code vor this.

I also should write a manuel. Its in process... 

Last but not least, I want to include some Self-entering values. Entrys like Apartment-Rent or the Netflix-Abo, thats they include every month again himself. 



## Install & Upgrade
For install, you the following 3 commands. For upgrade, use this too.

```
sudo git clone https://github.com/Alphabeit/openBalcal.git
cd Open_Balancecalculation
sudo bash install.sh
```

The program is splitet in two parts, the code and the databases. The code will be install from here, resp. overwritten during an update. The database will be created by the code, as long no database exsist. So if you upgrade the program, it will regnorice the database and continue to use.



## First Steps

After the programm is installed, just enter `balcal` in the Terminal. balcal is a Sydonym for BALanceCALculation.



## Manuel
At the current time, this is a terminal-only program. Hardcore Linux users are probably already starting to drool. For the manual, start the program and use the command `help`, or the corresponding command including the flag `-h`, `--help` or `?`.  

Just try it, the program is self-explanatory. 



## Support
You want to support me, then take over the language packs. Text is designed so that it is not in the code, but in separate language files. You could adapt these according to your language. The original language file "en_US.xml" is felted with a bad english from me.

Other wishes or comments you can send me via "Discussions".



## License
This project is licensed under the GPL-3.0 License. You can use it for free.
