import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
sys.stdin = io.TextIOWrapper(sys.stdin.buffer,encoding='utf-8')

birthday = input()
date = input()


birList = birthday.split(".")
dateList = date.split(".")

birYear = int(birList[0])
birMonth = int(birList[1])

dateYear = int(dateList[0])
dateMonth = int(dateList[1])

if dateMonth > birMonth:
    print(dateYear - birYear)
elif dateMonth < birMonth:
    print(dateYear - birYear - 1)
else:
    birDay = int(birList[2])
    dateDay = int(dateList[2])
    if dateDay >= birDay:
        print(dateYear - birYear)
    else:
        print(dateYear - birYear - 1)




