#-*- coding: utf-8 -*-
'''
==3 by 3 Multiplication
[국민대학교]20093326_이의재
'''

def printRow(danNum, multipleNum, endStr = '\n'):
        result = danNum * multipleNum
        print('{0:2} X {1:2} = {2:2}'.format(danNum,
                                             multipleNum,
                                             result),
              end = endStr)

        
#2~9 단을 구하고 한번에 3개의 단을 출력
for dan  in range(2, 9, 3):
        # 1~9의 값을 곱하기
	for j in range(1,10):
		# e.g if dan == 2 2단 출력
		printRow(danNum = dan,
                         multipleNum = j,
                         endStr = ' ')
		# e.g if dan == 2 then +1하여 3단 출력
		printRow(danNum = (dan + 1),
                         multipleNum = j,
                         endStr = ' ')

		# e.g if dan == 2 then +2하여 4단 출력
		# Not print 10 dan
		if dan + 2 < 10:
			printRow(danNum = (dan + 2),
                                 multipleNum = j)
                                 
                # 10 단일 경우 무시
		else:print();
        # 개행 출
	else: print()	
