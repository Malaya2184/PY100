# 3. We have a Billing Engine which calculates the call charge based on the following rates and
# durations.
#           1. Connection Duration: 60 sec
#           Rate for First 60 seconds. 0.05$ for first 60 sec

#           2. Incremental Duration: 30 sec
#           Effective Rate after Connection Duration so in our example after 60 sec. 0.05$ for
#           followed 30 sec.

#           3. Rate: 0.05
#           Example: Duration of a call is 140 sec
#           Then 0.05$ for 60 sec (connection duration)
#           Remaining duration = 140 - 60
#           = 80 sec
#           So for 80 seconds means 3 units 80/30 =~ 3
#           Remaining charge = 3 * 0.05$
#           = 0.15 $
#           Total Charge = 0.05$ + 0.15$
#           = 0.20$
# Write a Program to calculate the total cost from call duration, connection duration, incremental
# duration and rate.


total_duration = int( input('Enter the total duration: '))
Initial_rate = 0.05
if total_duration > 60:
    remaining_duration = total_duration - 60
    # print(remaining_duration)
    if remaining_duration > 30:
        x= remaining_duration//30
        y= remaining_duration % 30
        if y != 0:
            total_cost= 0.05 + x*0.05 + 0.05
            formated_total_cost = "{:.2f}".format(total_cost)
            print('total cost is', formated_total_cost, "$")
        else:
            total_cost= 0.05 + x*0.05
            formated_total_cost = "{:.2f}".format(total_cost)
            print('total cost is', formated_total_cost, "$")

elif total_duration == 0:
    total_cost = 0
    formated_total_cost = "{:.2f}".format(total_cost)
    print('total cost is', formated_total_cost, "$")
else:
    print('total cost is', Initial_rate,"$")