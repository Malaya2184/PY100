# making time table and convert  in to gst time


class Time:
    """Attributes; hour, minute, second"""
    def __init__(time,h=0,m=0,s=0):
        time.hours=h
        time.minutes=m
        time.seconds=s

    def difference_time(self, other):
        difference=Time()
        difference.hours=other.hours-self.hours
        difference.minutes=other.minutes-self.minutes
        difference.seconds=other.seconds-self.seconds
        if difference.seconds < 0:
            difference.minutes -= 1
            difference.seconds += 60
        if difference.minutes < 0:
            difference.hours -= 1
            difference.minutes += 60
        if difference.hours < 0:
            difference.hours += 24
        return difference
    def print_time(self):
        print(self.hours,self.minutes,self.seconds)
    def convert_ist_to_gmt(self):
        gmt=Time()
        if ((self.hours>5) and (self.minutes>30)):
            gmt.hours=self.hours-5
            gmt.minutes=self.minutes-30
            gmt.seconds=self.seconds
            return gmt
        else:
            gmt.hours=24-5+self.hours



test_time=Time(1,40,0)
diff=Time(5,30,0)
currTime=Time(16,39,30)
lab_start=Time(15,30,0)
lab_end=Time(18,0,0)

Time.print_time(diff.difference_time(test_time))

#print(currTime.hours,lab_start.hours,lab_end.hours)

output_time1=Time.difference_time(lab_start,currTime)
print(output_time1.hours,output_time1.minutes,output_time1.seconds)

output_time=lab_start.difference_time(currTime)
print(output_time.hours,output_time.minutes,output_time.seconds)



#print(currTime.hours,currTime.minutes, currTime.seconds)
#Time.print_time(currTime)
#lab_start.print_time()

#Time.print_time(lab_end)
#Time.difference_time(lab_start,lab_end)
#lab_start.difference_time(lab_end)
#print_time(output_time)

#currTime.hours=16
#currTime.minutes=39
#currTime.seconds=30

#lab_start.hours=15
#lab_start.minutes=30
#lab_start.seconds=0