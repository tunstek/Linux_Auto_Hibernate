import sys, time, datetime


if len(sys.argv) != 2:
    print "Please give a single argument in minutes"
else:
    seconds = int(sys.argv[1]) * 60
    print "Going to hibernate every " + sys.argv[1] + " minute(s).."
    while True:
        #sleep for alloted time
        time.sleep(seconds)

        currentDateTime = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
        log = "Hibernating.. - " + currentDateTime
        file = open("log.txt" ,'a+')
        file.write(log)
        file.close()
        con_out = subprocess.check_output(['pm-hibernate'])
