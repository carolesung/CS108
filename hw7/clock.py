#File: clock.py
#Name: Carole(Chia Jung) Sung
#Login Name: carole07@bu.edu
#Assignment: Hw7 Part2
#Date: Feb 8 2018
#Description: Contains a function that prints out intervals of hours and minutes
#within a specified period of time

def print_times(startHour, stopHour, increment):
    #prints out intervals of hours and mins within a specified period of time

    if 60%increment!=0:
        #Checks whether the 3rd argument is valid
        print("Increment Invalid!! Must be a factor of 60")
        
    elif stopHour > startHour:
        #Storing how many times the second for loop should run for in minsCount

        minsCount = 60//increment
        for hour in range(startHour, stopHour+1):
            #Hour loop
            
            startMin = 0
            for mins in range(minsCount):
                #Minute loop that prints time that pads number with zero if width!=2
                print("{:0>2d}".format(hour)+":"+"{:0>2d}".format(startMin))
                startMin = startMin + increment
        print("Time's Up!")
    else:
        #Checks whether the 2nd argument is valid
        print("Ending hour must be after the starting hour!!")
