import time
my_time = int(input("enter the time in seconds: "))
# for x in range(1,my_time+1):
#     time.sleep(1) #puts a one second delay
#     print(x)
# for x in range(my_time,0,-1):
#     time.sleep(1) #puts a one second delay
#     print(x)
for x in reversed(range(1,my_time+1)):
    time.sleep(1) #puts a one second delay
    seconds = x%60
    minutes = int((x/60)%60)
    hours = int(x/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
print("TIME'S UP!")