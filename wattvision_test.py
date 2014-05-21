import wattvision_api
	
#constants to test with
sensor_id=''
api_id=''
api_key=''
time=''
watts=
watthours=

#for get call	
type=''
start_time=''
end_time=''

print(wattvision_api.post(sensor_id,api_id,api_key,time,watts,watthours))
arr=wattvision_api.get(sensor_id,api_id,api_key,type,start_time,end_time)

for i in arr:
    print (i['v'])
