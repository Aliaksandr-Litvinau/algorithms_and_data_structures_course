import time

time_start = time.time()
i = 0
while i < 1000000000:
    # Do nothing
    i += 1

time_finish = time.time()
time_span = time_finish - time_start
print(time_span, 'seconds')
"""Each iteration of the cycle consists of 3 actions 
(that is, 3 billion commands are executed (instead of 1 billion)):
1. add 1, 
2. check the condition, 
3. go back to the beginning of the cycle"""
