
#; in linux is used to tell terminal that we want to execute another command after current

import subprocess #module name for netowrking

interface = input("Interface")
new_mac = input("New Mac address")

print("[+] changing MAC address for"+" "+interface +"to"+" "+new_mac)


#subprocess.call("ifconfig" + interface+  "down", shell = True)  #shell = true so we run linux commands
#subprocess.call("ifconfig"+ interface+ "hw ether"+ new_mac, shell = True)
#subprocess.call("ifconfig" + interface+ "up", shell = True)

#more secure vesion of commands than above
subprocess.call(["ifconfig",interface,"down"]) #instead of a string we can use a list
subprocess.call(["ifconfig",interface,"hw","ether",new_mac])
subprocess.call(["ifconfig",interface,"up"])



#note my interface is different from urs choose your own interface whos mac you want to change
#


#note my interface is different from urs choose your own interface whos mac you want to change
#
