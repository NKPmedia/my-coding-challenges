""" 
A long running webserver is writing to a log file, one request summary per line. 
Here is an example file: 

Reference:
https://leetcode.com/discuss/interview-question/1533097/Google-Onsite-L4

Input:
# timestamp(millis), URL, status, processing time
1000001, /index.html, 200, 150 
1000002, /article/1234.html, 500, 1 
1000005, /index.html, 200, 50 
1001000, /article/4321.html, 200, 10

Return all the input timestamp but associated with the number of requests being
processed at the time of the timestamp. 

Output :
1000001 --> 1
1000002 --> 2  (since the first process is still running, timestamp 1000002
would have two processes running) 
1000005 --> 2  (since the first process is still running, timestamp 1000005
would have two processes running) 
1001000 --> 1


# Example Diagram:
1=======================150
	2====3
			5=====50          
						   1000========1010
"""