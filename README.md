timelapse_screencap
===================

basic python time lapse screen capturing utility
tested with python 2.6 on centos 6.5

usage
=====
python main.py path filename time_increment_in_seconds

there is no real argument handling at the moment. So they must be put in in order.
you can omit them from the backend first. 
time in seconds defaults to 1 second. 
filename defaults to screencap.
path defaults to the current working directory.

it will then drop files number sequentially into the path folder.
stop it with good old command-c
