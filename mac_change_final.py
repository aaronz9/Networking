import subprocess #module name for netowrking

subprocess.call("ifconfig wlp6s0 down", shell = True)  #shell = true so we run linux commands
subprocess.call("ifconfig wlp6s0 hw ether  34:e6:ad:92:e0:3f", shell = True)
subprocess.call("ifconfig wlp6s0 up", shell = True)



#note my interface is different from urs choose your own interface whos mac you want to change
#