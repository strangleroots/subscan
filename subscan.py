#!/bin/bash/python3
import time 
import subprocess

#SUBSCAN

TDomain = input("what is your target domain?")
TIP = input("what is your target IP?")
TFolder = input("what is your desired folder name?")

mkdir = "mkdir +'[TFolder]' ~/bin/go"
subprocess.call(mkdir, shell=True)

wayback1 = "[TDomain] > ~/bin/go/[TFolder]/Targeturl.txt"
subprocess.call(wayback1, shell=True)

wayback2 = "cat /bin/go/[TFolder]/Targeturl.txt | ./waybackurls > ~/bin/go/[TFolder]/target.urls"
subprocess.call(wayback2, shell=True)

wayback3 = "cat /bin/go/[TFolder]/target.urls | httprobe > ~/bin/go/[TFolder]/[TDomain].txt"
subprocess.call(wayback3, shell=True)

#targeturl.txt = necessary input for waybacktool
#target.urls = waybacktool output, to be filtered
#[TDomain].txt = waybacktool output, filtered, continued on:

sublist3r = "sublist3r -d [TDomain] >> ~/bin/go/[TFolder]/[TDomain].txt" 
subprocess.call(sublist3r, shell=True)
#append and add

dig = "dig axfr @[TIP] [TDomain] >> ~/bin/go/[TFolder]/[TDomain].txt" 
subprocess.call(dig, shell=True)
#append and add

amass = "amass enum -passive -d [TDomain] >> ~/bin/go/[TFolder]/[TDomain].txt" 
subprocess.call(amass, shell=True)
#append and add

selection = "cat ~/bin/go/[TFolder]/[TDomain].txt | awk '{print $1}' | sort -u > [TDomain]result.txt" 
subprocess.call(selection, shell=True)
#filter into new txt with final result
