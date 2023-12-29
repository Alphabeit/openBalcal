# Open_Balancecalculation
openBalcal, a Python program for your own finances.

Most people do their accounting in tablesheets programs like Excel, if at all. It may be practical, but it could also be better. With too much time on my hands and even more interest in the Python language, this program was born. So this tool is used for cost accounting, how much money one has spent and how much is consequently still available. At the same time, the protection of your personal data is ensured, because the databases are created locally. No CLoud, but also no communication to the outside.



## Version
Each digit in the version number represents a development status. 

The last digit is incremented for bug fixes - means bugs were fixed but program was not extended. The second digit represents function updates. New functions, or new features that extend the program as such. Allows also new bugs. ;) The foremost digit represents the major version. When this is superscripted, we are talking about a major program change. For example, the addition of a GUI. "Don't ask me when this is coming". 

A major update could also change the program so much that the database from the previous versions is no longer compatible. In this case I would provide a function to adapt the database for the current version.

For the update histroy, look under "Info", in the file "Updatehistory.md".



#### newest Verison
v0.2.0

Okay, start we with the changes for the userside. 

- At first, we have include some date functions. 
So, you can call as example the curentlly month also with "this_month", instead of the YYYYMMDD Syntax.
Also, if you didn't deciede a specific date, it will be today, automatic. 

- Next, it was included a Report Function.
So with every program start, the program shows you the balance of today and this_month.
Maybe the fastest way to know your balance.
In the future, you should decide by you own, with topics and time periods are showed with the reports.

But how does its look for the developers and this someone, how are interested in the code?

- At first, I have pull some functions in the folder "lowerfunction". 
There are scripts, where the user not didn't work directly.
As example, the "lowerfunctions" are called by the "functions" and there are called by the "main script".

- At next, I have included a flag function-script. 
So the commands are not written by this own anymore, instead now, every command is built by the flag functions.
The result, the "function" scripts a smaller and the command structure is uniform.
Not to forget, for the future is much more easier to write new commands.

- Also, I have change a little bit the lang-file. 
Duplicates are removed and error message are include.
I even include some information about the last change, so when someone would translate the lang files and a new update is coming, he could see, what he needs to change and what can be stay the same.

- Last but not least, the program gets an alias. 
Open_Balancecalculation is the name of this program and this will stay.
But for a search over google or a call over the command line, its to long.
So I present the alias "openBalcal", for OPEN_BALalnceCALculation.

I wish you a good start in the coming year.

#### planed, next comming Version
v0.3.0

In the upcoming version, I plan some invidual options, so thats you can decider more, what you see and whta not.

Furthermore, I would also like to add a savings plan. Simple calculation: salary, minus savings target, minus expected expenses, minus current expenses, equal to residual value that can be spent.

Not to forget, I create some installation scripts, for Linux and Windows.



## Install
Comming with v0.3.0.



## Manuel
At the current time, this is a terminal-only program. Hardcore Linux users are probably already starting to drool. For the manual, start the program and use the command "help", or the corresponding command including the flag "-h", "--help" or "? 

Just try it, the program is self-explanatory. 



## Support
You want to support me, then take over the language packs. Text is designed so that it is not in the code, but in separate language files. You could adapt these according to your language. The original language file "en_US.xml" is felted with a bad english from me.

Other wishes or comments you can send me via "Discussions".



## License
This project is licensed under the GPL-3.0 License.
