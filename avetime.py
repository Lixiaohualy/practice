import sys,re,datetime

cost_total = 0
count = 0

def read_data(file):
	global cost_total
	global count
	origFile = open(file)
	
	start_time = ""
	end_time = "" 
	while 1:
		line = origFile.readline()
		if line =="":
			break
		if line.find(":") >= 0:
			tlist = line.split(" ")
			timestring = "%s-%s-%s %s"%(tlist[5][0:4], tlist[1], tlist[2], tlist[3])
			if start_time == "":
				start_time=datetime.datetime.strptime(timestring, "%Y-%b-%d %H:%M:%S")
			else:
				count +=1
				end_time=datetime.datetime.strptime(timestring, "%Y-%b-%d %H:%M:%S")
				cost_total+=(end_time-start_time).total_seconds()
				break	
		    
	origFile.close()


prefix = sys.argv[1]
for i in range(1,6):
	read_data(prefix + str(i) + '.log')
print('count: %d, avg cost: %f' %(count, cost_total/count))

