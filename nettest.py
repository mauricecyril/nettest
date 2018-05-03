#!/usr/bin/python
#
# you need to install dependent programs and 
# utilities such as speedtest-cli, https://github.com/sivel/speedtest-cli
# a command line interface program that tests your bandwidth speeds 
# via speedtest.net 


import os
import sys 
import csv 
import datetime 
import time 
import threading

# Define global variable for file location where data will be stored
global filelocation
# Edit the path between ' ' and save the extension as csv
filelocation = str('/sdcard/python3/data.csv')

def speedtest():

        #run speedtest-cli
        print('Running Test')
        a = os.popen("speedtest-cli --simple").read()
        print('Test Completed')


        #split the 3 line result (ping,down,up)
        lines = a.split('\n')
        print(a)
        ts = time.time() 
        date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S') 

        #if speedtest could not connect set the speeds to 0 
        if "Cannot" in a:
                msg = str("Failed Connection")
                p = 0 
                d = 0 
                u = 0 
                print(msg, date, p, d, u) 

                #save the data to file for local network plotting 
                out_file = open(filelocation, 'a') 
                writer = csv.writer(out_file) 
                writer.writerow((date,msg,p,d,u)) 
                out_file.close()

        #if speedtest connection reset by peer, set the speeds to 0 
        elif "Errno 104" in a:
                msg = str("Connection Reset by Peer")
                p = 0
                d = 0
                u = 0
                print(msg, date, p, d, u)

                #save the data to file for local network plotting 
                out_file = open(filelocation, 'a') 
                writer = csv.writer(out_file) 
                writer.writerow((date,msg,p,d,u)) 
                out_file.close()
                
        #if speedtest Times out set the speeds to 0 
        elif "Errno 110" in a:
                msg = str("Connection Timed Out")
                p = 0
                d = 0
                u = 0
                print(msg, date, p, d, u)

                #save the data to file for local network plotting 
                out_file = open(filelocation, 'a') 
                writer = csv.writer(out_file) 
                writer.writerow((date,msg,p,d,u)) 
                out_file.close()

        #if speedtest cannot determine Name or Service set the speeds to 0 
        elif "Errno -2" in a:
                msg = str("Name or Service Not Known")
                p = 0
                d = 0
                u = 0
                print(msg, date, p, d, u)

                #save the data to file for local network plotting 
                out_file = open(filelocation, 'a') 
                writer = csv.writer(out_file) 
                writer.writerow((date,msg,p,d,u)) 
                out_file.close()
                
        #if speedtest successfully pings set connection as successful         
        else:
                msg = str("Successful Connection") 
                p = lines[0][6:11] 
                d = lines[1][10:14] 
                u = lines[2][8:12] 
                print(msg, date, p, d, u) 

                #save the data to file for local network plotting 
                out_file = open(filelocation, 'a') 
                writer = csv.writer(out_file) 
                writer.writerow((date,msg,p,d,u))
                out_file.close()

        return


if __name__ == '__main__':
        # Run the script in an infinte loop [press Ctrl + C to end]
        while True:
            speedtest()
            print("Script Completed and Results Logged")
            time.sleep(120)
