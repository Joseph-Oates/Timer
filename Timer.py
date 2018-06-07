def Timer():

	import time
	print "this is a two minute timer!"

	start = raw_input("Enter begin to start the timer!: ")
	if start == "begin":
		timeLoop = True

	seconds = 0
	minutes = 0

	while timeLoop:
		seconds += 1
		print "Minutes " + str(minutes) + " Seconds " + str(seconds)
		time.sleep(1)
		if seconds == 59:
			minutes += 1

		if minutes == 1:
			seconds = 0
			timeLoop = False
			print "Minutes " + str(minutes) + " Seconds " + str(seconds) 
			print "Time's up!"

Timer()