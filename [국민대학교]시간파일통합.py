#-*- coding: utf-8 -*-
'''
==@ 로또 번호 추출기 
[국민대학교]20093326_이의재 
''' 

from datetime import datetime, timedelta
import time, glob


class DateType:
    def __init__(self):
        self.__nameType = '{0}_DATE.txt'
        self.__printType = '{0:^4} - {1:^2} - {2:^2} {3:^2} : {4:^2}\n'
        
    def getPrintType(self):
        return self.__printType
    def getNameType(self):
        return self.__nameType



# Init Start Date
'''
주어진 과거로부터 미래까지 매 분마다 파일 생성
'''
date = datetime.now() - timedelta(days = 5)
dateClass = DateType()

while True:
    time.sleep(1/1000)
    
    with open(dateClass.getNameType().format(date.strftime('%Y-%m-%d')),
              'a') as file:
        file.write(self.__printType.format(date.year,
                                           date.month,
                                           date.day,
                                           date.hour,
                                           date.minute))
        date = date + timedelta(minutes = 1)

    if date == datetime.now():
        break
'''
위 함수에서 나온 파일들을 통합하는 함수
'''
# new File Create
dataList = []
# Get file List
fileNameList = glob.glob('*_DATE.txt')
for i in fileNameList:
    with open(i,
              'r') as file:
        # added list content
        dataList.extend(file.readlines())
        
with open(dateClass.getNameType().format('ALL'),
          'w+') as file:
    [file.write(i) for i in dataList]

    



    
