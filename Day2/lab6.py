#You live 4 miles away from university.The bus drives at 25mph but spends 2 mins at each of the stops on the way.
#How long will the bus journey take?Alternatively,you could run to the university.
#You jog the first mile at 7mph;then run the next two at 15mph;before jogging the last at 7mph again.
#Will this be quicker or slower then the bus?
distance=4
speed1=25
time= (4/speed1)*60
total_time=time+(10*2)
speed2=7
time1=(1/speed2)*60
speed3=15
time2=(2/speed3)*60
speed4=7
time3=(1/speed4)*60
totaltime1=time1+time2+time3
print("The total time to reach university by bus is: ", total_time)
print ("The total time to reach univesity by walking is: ", totaltime1)
if totaltime1>total_time:
    print ("walking is faster to reach to the university")
else:
    print("Going by bus is faster than walking")
    