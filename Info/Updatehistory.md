# v0.1.0
The first version of the program. The standard version, here we are begining. On this point, the program deliver everything what is needed to create and read your database. You can create entrys and calculade your balance based on them. - 20231101



# v0.2.0
20231227

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
