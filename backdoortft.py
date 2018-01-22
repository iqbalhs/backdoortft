import datetime;

def backdoortft(time = None):
	if time == None:
		now = datetime.datetime.now()
 		time = int(str(now.hour) + str(now.minute))
 	
 	return (9999 - time)**2

if __name__ == "__main__":
	print backdoortft()