#!/usr/bin/python
# you need to install dependent programs and 
# utilities such as speedtest-cli, a command line 
# interface program that tests your bandwidth speeds 
# via speedtest.net 
import os
import sys 
import csv 
import datetime 
import time 


def test():

        #run speedtest-cli
        print('Running test')
        a = os.popen("speedtest-cli --simple").read()
        #b = str(a)
        #print(b)
        print('Test Completed')


        #split the 3 line result (ping,down,up)
        lines = a.split('\n')
        print(a)
        #print(lines[0])
        ts = time.time() 
        date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S') 

        #if speedtest could not connect set the speeds to 0 

        if "Cannot" in a:
                print("Failed Connection") 
                #print(a) 
                p = 0 
                d = 0 
                u = 0 
                print(date, p, d, u) 

                #save the data to file for local network plotting 
                out_file = open('/sdcard/python3/data.csv', 'a') 
                writer = csv.writer(out_file) 
                writer.writerow((date,ts*1000,p,d,u)) 
                out_file.close()

        elif "Errno 110" in a:
                print("Connection Timed Out")
                p = 0
                d = 0
                u = 0
                print(date, p, d, u)

        else:
                print("Successful Connection") 
                p = lines[0][6:11] 
                d = lines[1][10:14] 
                u = lines[2][8:12] 
                print(date,p, d, u) 

                #save the data to file for local 
                #network plotting 

                out_file = open('/sdcard/python3/data.csv', 'a') 
                writer = csv.writer(out_file) 
                writer.writerow((date,ts*1000,p,d,u))
                out_file.close()

        return


if __name__ == '__main__':
        test()
        print('completed')
