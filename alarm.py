current_time = int(input("What is the current time in hours: "))
hours_to_wait = int(input("Enter the hours to wait until the alarm goes off: "))

wait_time = hours_to_wait % 24
time_alarm_goes_off = (wait_time + current_time) % 24
print("Time Alarm Goes off: " + str(time_alarm_goes_off))
