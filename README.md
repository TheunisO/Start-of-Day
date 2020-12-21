# Start-of-Day
I use a few different applications when I work. This python project allowed me to reduce the amount of clicks I need to get my day started. 

I set out to create a single click option for starting the programs I use on a daily basis. 
There were several deprecated libraries I wanted to use but I ended up using the subprocess library which worked well. 

Though I had to make a small change (adding in an additional \ in the pathname of the objects, I had little trouble setting this up.

In order to run these applications on your own machine you will need to do the following;
1. Download the code
2. Change the commented lines to reflect the apps which you want to use.
3. Find the application in your programs list and copy the file path.
  3a. I found this to be easiest by typing in the application name, selecting Open File Location, selecting the app, going to properties, and copying the file location. 
4. Paste the file path between the quotation marks, and add another \  to each existing \. You will see double (\\) at each separation. 
5. Save and run. 

I had some issues with the quotation marks not copying correctly or being difficult so I would erase the entire line and copy it from the previous one before pasting in the file path. I also removed the extraneous single quotes. 

The applications will likely throw an error if I change the file path or try to move things around too much. 
