Enter file contents herea#-*- conding: utf-8 -*-
'''
==@ 로또 번호 추출기
[국민대학교]20093326_이의재
'''

import random
from datetime import datetime

class PeaceLotto:

    def __init__(self, date):
        self.__date = date
        self.__MIN = 1
        self.__MAX = 45
        self.__SIZE = 6
        # 중복 방지 집합사용
        self.__number = set([])
        
    def get_lotto_number(self):
        print('{0} 현재 추천 로또 번호.'.format(self.__date))
        while True:
            if len(self.__number) == self.__SIZE:
                return self.__number
            
            self.__number.add(random.randrange(self.__MAX) + 1)
        



a = PeaceLotto(datetime.now())
print(a.get_lotto_number())


