#!/bin/bash/python3
import time 
import subprocess

#SUBSCAN

TDomain = input("what is your target domain?")
TIP = input("what is your target IP?")
TFolder = input("what is your desired folder name?")

mkdir = f"mkdir ~/go/bin/'{TFolder}'"
subprocess.call(mkdir, shell=True)

wayback1 = f"echo '{TDomain}' > ~/go/bin/'{TFolder}'/targeturl.txt"
subprocess.call(wayback1, shell=True)

wayback2 = f"cat /go/bin/'{TFolder}'/targeturl.txt | ~/go/bin/./waybackurls > ~/go/bin/'{TFolder}'/target.urls"
subprocess.call(wayback2, shell=True)

wayback3 = f"cat /go/bin/'{TFolder}'/target.urls | httprobe > ~/go/bin/'{TFolder}'/'{TDomain}'.txt"
subprocess.call(wayback3, shell=True)

#targeturl.txt = necessary input for waybacktool
#target.urls = waybacktool output, to be filtered
#[TDomain].txt = waybacktool output, filtered, continued on:

sublist3r = f"sublist3r -d '{TDomain}' >> ~/go/bin/'{TFolder}'/'{TDomain}'.txt" 
subprocess.call(sublist3r, shell=True)
#append and add

dig = f"dig axfr @'{TIP}' '{TDomain}' >> ~/go/bin/'{TFolder}'/'{TDomain}'.txt" 
subprocess.call(dig, shell=True)
#append and add

amass = f"amass enum -passive -d '{TDomain}' >> ~/go/bin/'{TFolder}'/'{TDomain}'.txt" 
subprocess.call(amass, shell=True)
#append and add

selection = f"cat ~/bin/go/'{TFolder}'/'{TDomain}'.txt | awk {{print $1}} | sort -u > '{TDomain}'result.txt" 
subprocess.call(selection, shell=True)
#filter into new txt with final result
