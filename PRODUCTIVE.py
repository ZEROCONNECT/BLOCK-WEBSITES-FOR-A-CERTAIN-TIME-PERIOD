import time
from datetime import datetime as dt #now we don't have to do datetime.datetime

hosts_temp='hosts'
#using the r allow us to escape escape character
hosts_path=r'c:\windows\system32\drivers\etc\hosts'
redirect='127.0.0.1'
sites_that_kill_me=['www.facebook.com','youtube.com']
#these 4 element need their own respective lines on the host file and redirect ip
print(dt.now())

while True:
    #if you look at the output of dt.now() you will see the out0put format
    #we are creating 3 datetime objects and comparing them
    if dt(dt.now().year,dt.now().month,dt.now().day,9)< dt.now()<dt(dt.now().year,dt.now().month,dt.now().day,17):
        print('working hours')

#now we can load,read and write to the hosts file,using the r+ allows reading and writing to the file
        with open(hosts_path,'r+') as file:
            content = file.read() #this will load the entire file
            for site in sites_that_kill_me:
                if site in content:
                    pass
                else:
                    file.write(redirect+' '+site+'\n')
    else:
        with open(hosts_path,'r+')as file:
# the read lines method will produce a list with each str item
#then check the read lines list against our sites that kill me list, and if items then i want them out,but no menthod to delete the append list

             content = file.readlines()

#once read_line is complete the pointer will be sitting at the very end of the file
#so any append method will add from the point of the pointer
#seek method will place pointer where we want

             file.seek(0)
             for line in content :
             #if item not there,append a new file hosts via writing a new file
                if not any(site in line for site in sites_that_kill_me):
                 file.write(line)
#truncate method will delete all things UNDER the specified section
             file.truncate()
        print('time to play!!!')
    time,sleep(5)