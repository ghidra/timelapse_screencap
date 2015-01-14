timelapse_screencap
===================

basic python time lapse screen capturing utility
tested with python 2.6 on centos 6.5

usage
=====
python main.py filename scale path time_increment_in_seconds

there is no real argument handling at the moment. So they must be put in in order.
you can omit them from the backend first. 
time in seconds defaults to 1 second. 
path defaults to the current working directory.
scale defaults to 1.
filename defaults to screencap.

it will then drop files number sequentially into the path folder.
stop it with good old command-c


to-do
====
Other than argument handling, I want to add yet another argument to start the sequence over at a given frame number. Otherwise you might overwrite you last capture if you are not careful. It doesnt ask you before hand, it just starts writing.
