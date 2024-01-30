#import datetime

n = int(input())
print("{}:{}:{}".format(int(n/3600),int(n%3600/60),int(n%60)))

#duration = int(input())
#print(str(datetime.timedelta(seconds = duration)))

#seconds = seconds (24*3600)
#hour = seconds //3600
#seconds %= 3600
#minutes = seconds // 60
#seconds %= 60
#print("%d:%02d:%02d" % (hour, minutes, seconds))
