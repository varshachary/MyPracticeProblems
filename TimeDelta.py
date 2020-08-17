"""
When users post an update on social media,such as a URL, image, status update etc., other users in their network are able to view this new post on their news feed. Users can also see exactly when the post was published, i.e, how many hours, minutes or seconds ago.

Since sometimes posts are published and viewed in different time zones, this can be confusing. You are given two timestamps of one such post that a user can see on his newsfeed in the following format:

Day dd Mon yyyy hh:mm:ss +xxxx

Here +xxxx represents the time zone. Your task is to print the absolute difference (in seconds) between them.

Input Format

The first line contains , the number of testcases.
Each testcase contains  lines, representing time  and time .
"""
from datetime import datetime

def delta(d1,d2):
    f= '%a %d %b %Y %H:%M:%S %z'
    d1 = datetime.strptime(d1, f) 
    d2 = datetime.strptime(d2, f) 
    diff = (d2-d1).total_seconds()  
    return abs(int(diff))

for _ in range(int(input())):
    print(delta(input(), input()))
