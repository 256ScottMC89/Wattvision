Wattvision
==========

This code allows the post and get call from wattvision to be tested, and allows them to be used in a python application. There are several parameters in the wattvision_test.py file. They are:

sensor_id (this is your sensor id)
api_id (this is your api id)
api_key (this is your api key)
time (YYYY-MM-DDTHH:MM:SS)
watts (watts)
watthours (watthours)

type (rate or consumption)
start_time (YYYY-MM-DDTHH:MM:SS)
end_time (YYYY-MM-DDTHH:MM:SS)

This code requires the requests library to be installed, instructions for installing it are here http://docs.python-requests.org/en/latest/user/install/

either wattvision_test or wattvision_gui will work with wattvision_api
