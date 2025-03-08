#Multithreading in Python
#Firstly The important thing is: When our function runs it is executed in the main thread..
#So to do multithreading we have to make multiple threads 
#For the we have Threading package.

from threading import *
from time import sleep


class Hello(Thread):  #Now since Hello inherits Threads it is a thread class now
    def run(self):    #Run is a function of Thread class that runs thread
        for i in range(5):
            print("Hello")
            sleep(1)  #Required since once thread startsit will continue print Hello but we need Alternative hello and Hi 
            #So We print Hello and then sleep for 1 sec. While which Hi get printed and sleeps


class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)


t1 = Hello() 
t2 = Hi()  #Two threads are created

t1.start() #Start function is used to start are thread. it ultimately can run method that we have overrided from Thread class.
sleep(0.2) #Now at some point when sleep for both clashes Since they were starting almost together. They will again print HelloHi in same line or the order may distrub
#So to keep a time difference we stop here for 0.2 second so that both doesnt cross.
t2.start()

#print("Main Thread")   #Since this will execute on Main thread it will come in between

#But we want it to be executed after t1 and t2 finishes and join main thread again.

#So we use join on t1 and t2

t1.join()
t2.join()

print("Bye form Main Thread")

