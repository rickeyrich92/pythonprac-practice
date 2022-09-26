#!/usr/bin/env python3

import sys
import re

def ftp(args):
    ip_dict = {}
    args = args.split("\n")
    return_str = ''
    count = 0
    for a in args:
        a = a.split(';')
        #print(a[8])
        if len(a) > 7:
            search = a[8]
            answer = a[9]
            if search == 'FTP' and 'Request' in a[9]:
                if a[2] in ip_dict:
                    ip_dict[a[2]] += 1
                else:
                    #count+=1
                    ip_dict[a[2]] = 1

    sort_dict = sorted(ip_dict.items(), key=lambda x: x[1], reverse=False)
    #print(answer)
    #print(sort_dict)
    return sort_dict
        
    #print(ip_dict)
        #print(search)        
        #print(count)        

#this function is part of the python boilerplate. the first line defining the main function should not need any edits.
def main(args): #defines our main function
    fopen = open(args, 'r') #opening our argument file 
    fread = fopen.read() #reading the argument file to be passed to our function
    #print(fread)
    #print(fread[:])
    print(ftp(fread)) #prints the output of our main function

if __name__ == '__main__': #this checks if the script is being run directly or if it was imported into another script (only runs main function if the script is being run directly)
    args = sys.argv[1] #this gathers the command line arguments
    main(args) #this calls the main function and passes the command line arguments (it actually starts the script)