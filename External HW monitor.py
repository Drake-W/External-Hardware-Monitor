from __future__ import print_function
import json
import requests
from time import sleep
import re
from subprocess import Popen
import datetime as dt
from gpiozero import LED

led = LED(10)
led2 = LED(11)

led.on()
led2.on()

#Popen(['python','graphtest.py']) #opens the graph script

cu = open("cpuusage.txt", "w")
ct = open("cputemp.txt", "w")
gu = open("gpuusage.txt", "w")
gt = open("gputemp.txt", "w")
counter = 0
counter1 = 60

for i  in range(60):
    fill = "{},0\n".format(i)
    ct.write(fill)
    cu.write(fill)
    gt.write(fill)
    gu.write(fill)


cu.close()
ct.close()
gu.close()
gt.close()

#configs
motherboard = 2
cpu = 3
cputemp = 15
cpuusage = 17
memused = 31
memavail = 32
gpu = 33
gpuclock = 35
gputemp = 39
gpuusage = 41

#dump the json into a file
#with open("data_file.json", "w") as write_file:
#    json.dump(data, write_file, indent =4)

#print json to console
#print (json.dumps(data, indent=4))

def get_stuff(data_dict):
    #gets: min,max,value from input and returns in a list alongside children's
    # create new object of the relevant data fields
    
    #returns min/max/value headers
    my_data = {k:data_dict[k] for k in ['Text','Min', 'Max', 'Value']}
    
    #returns just values
    #my_data = [data_dict[k] for k in ['Min', 'Max', 'Value']]
    
    # recursively get each child's data and add that to a new list
    children_data = [d for child in data_dict['Children'] for d in get_stuff(child)]
    # add our data to the start of the children's data
    return [my_data] + children_data
    
#output = get_stuff(data)
#print(json.dumps(output,indent=4))
while 1 > 0:
	response = requests.get("http://192.168.50.148:8085/data.json")
	data = json.loads(response.text)
	output = get_stuff(data)
	
	print("\n" * 100) #clears console
	
	print("System Info")
	print("Mobo: ", end='\t')
	print(output[motherboard]['Text'])
	print("CPU: ", end='\t')
	print(output[cpu]['Text'])
	print("GPU: ", end='\t')
	print(output[gpu]['Text'])
	print("\n\n\n")
	
	print( "\t\tMin\t\tValue\t\tMax")
	
	print ("CPU Temp", end='\t')
	print (output[cputemp]['Min'], end='\t\t')
	print (output[cputemp]['Value'], end='\t\t')
	print (output[cputemp]['Max'])
	
	print ("CPU Load", end='\t')
	print (output[cpuusage]['Min'], end='\t\t')
	print (output[cpuusage]['Value'], end='\t\t')
	print (output[cpuusage]['Max'])
	
	print ("GPU Temp", end='\t')
	print (output[gputemp]['Min'], end='\t\t')
	print (output[gputemp]['Value'], end='\t\t')
	print (output[gputemp]['Max'])
	
	print ("GPU Load", end='\t')
	print (output[gpuusage]['Min'], end='\t\t')
	print (output[gpuusage]['Value'], end='\t\t')
	print (output[gpuusage]['Max'])
	
	print ("GPU Clock", end='\t')
	print (output[gpuclock]['Min'], end='\t')
	print (output[gpuclock]['Value'], end='\t')
	print (output[gpuclock]['Max'])
	
	print ("Memory Used", end='\t')
	print (output[memused]['Min'], end='\t\t')
	print (output[memused]['Value'], end='\t\t')
	print (output[memused]['Max'])
	
	print ("Memory Avilable", end='\t')
	print (output[memavail]['Min'], end='\t\t')
	print (output[memavail]['Value'], end='\t\t')
	print (output[memavail]['Max'])
	
	#cpu temp export block
	x = (output[cputemp]['Value'])
	x = re.sub(r'[^\d.]+', '', x)
	x = float(x)
	x = int(x)
	heck = "{},{}".format(counter1,x)
	ct = open("cputemp.txt", "a")
	ct.write(heck)
	ct.write("\n")
	ct.close()


	#cpu usage export block
	x = (output[cpuusage]['Value'])
	x = re.sub(r'[^\d.]+', '', x)
	x = float(x)
	x = int(x)
	heck = "{},{}".format(counter1,x)
	cu = open("cpuusage.txt", "a")
	cu.write(heck)
	cu.write("\n")
	cu.close()

	#gpu temp export block
	x = (output[gputemp]['Value'])
	x = re.sub(r'[^\d.]+', '', x)
	x = float(x)
	x = int(x)
	heck = "{},{}".format(counter1,x)
	cu = open("gputemp.txt", "a")
	cu.write(heck)
	cu.write("\n")
	cu.close()
	
	if x < 50:
		led.on()
		led2.off()
	if 50 <= x < 60:
		led.off()
		led2.off()
	if x >= 60:
		led.off()
		led2.on()

	#gpu usage export block
	x = (output[gpuusage]['Value'])
	x = re.sub(r'[^\d.]+', '', x)
	x = float(x)
	x = int(x)
	heck = "{},{}".format(counter1,x)
	cu = open("gpuusage.txt", "a")
	cu.write(heck)
	cu.write("\n")
	cu.close()



	counter1 = counter1 + 1
	if counter < 60:
		counter = counter + 1
	if counter > 59:
		with open('cputemp.txt', 'r') as fin:
			data = fin.read().splitlines(True)
			fin.close()
		with open('cputemp.txt', 'w') as fout:
			fout.writelines(data[1:])
			fout.close()
		with open('cpuusage.txt', 'r') as fin:
			data = fin.read().splitlines(True)
			fin.close()
		with open('cpuusage.txt', 'w') as fout:
			fout.writelines(data[1:])
			fout.close()
		with open('gputemp.txt', 'r') as fin:
			data = fin.read().splitlines(True)
			fin.close()
		with open('gputemp.txt', 'w') as fout:
			fout.writelines(data[1:])
			fout.close()
		with open('gpuusage.txt', 'r') as fin:
			data = fin.read().splitlines(True)
			fin.close()
		with open('gpuusage.txt', 'w') as fout:
			fout.writelines(data[1:])
			fout.close()
		
	sleep(1)

#print (output[cpuusage]['Value'])
''' how to convert a value to a float
x = (output[gpuusage]['Value'])
x = re.sub(r'[^\d.]+', '', x)
x = float(x)
'''
