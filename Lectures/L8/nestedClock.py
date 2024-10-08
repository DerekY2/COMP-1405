''' 
    COMP 1005/1405 - Lecture 8 Nest Loops -- 12 - hour clock
    Name: Sean Benjamin
    Date: October 2, 2024
'''
'''
    Note: You do not need to include these comments in your assignment (but you may).  These comments
          are for educational purposes.
          
    The nested clock code has been modified from Dr. Robert Collier's example from 
    the COMP 1005/1405 Fall 2021 course.
    
'''


# the time library is imported to gain access to the sleep function
# the sleep function causes your program to wait for the number of 
# seconds specified in your argument
import time

# don't forget that the range function has default values for the
# stop and step parameters (but no default for the stop parameter)
# range(start, stop, step)  # all three arguments provided
# range(start, stop)        # start and stop provided, step defaults to 1
# range(stop)               # stop provided, start defaults to 0, step defaults to 1



# outer loop, governing the hour
# minimum hour value is 1, so "start" is 1
# maximum hour value is 12, so "stop" needs to be 13

# for h in range(1, 13, 1):
for h in range(1, 13):

	# inner loop, governing the minute
	# minimum minute value is 0, so "start" is 0 (which is the default)
	# maximum minute value is 59, so "stop" needs to be 60

	# for m in range(0, 60, 1):
	for m in range(60):
		# our 'innermost' loop counts the seconds
		for s in range(60):
		
			# if you wanted your clock to actually work (sort of) 
			# you could have your program wait 1 second here...
			# ...but this won't work well because your computer
			# will be doing other stuff as well, meaning that you
			# will spend more than 1 second total on each iteration
			# time.sleep(1)

			# adding a pause here makes the whole process a bit easier to follow
			# when trying to monitor the output on the terminal
			print(f"Time: Hours {h} : Minutes {m} : Seconds {s}")
			time.sleep(1)

