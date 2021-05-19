from playsound import playsound
import datetime

extracted_time=open('D:\\------PYTHON CODES---------\\Data\\data.txt','rt')
gettime=extracted_time.read()
print(gettime)
Time=str(gettime)

delete_time=open('D:\\------PYTHON CODES---------\\Data\\data.txt','r+')
delete_time.truncate(0)
delete_time.close()

def ringnow(gettime):
    time_to_set=str(gettime)

    time_now = time_to_set.replace('set','')
    time_now = time_now.replace('alarm','')
    time_now = time_now.replace('for','')
    time_now = time_now.replace('and',':')
    time_now = time_now.replace('colon',':')
    print(time_now)

    alarm_time=str(time_now)

    while True:
        current_time=datetime.datetime.now().strftime('%H:%M')

        if current_time == alarm_time:
            playsound("D:\\music\\alarm ringtone.mp3")
            playsound("D:\\music\\alarm ringtone3.mp3")
            break


ringnow(Time)