#-*- encoding: utf-8 -*-
'''
== Book Admin
[국민대학교]20093326_이의재
'''

class Books: 
    @staticmethod
    def set_book_info(name, author, price):
        with open('book_admin.txt',
                  'a') as file:
            file.write('name : {0}, author : {1}, price : {2}\n'.format(name,
                                                                      author,
                                                                      price))

    @staticmethod
    def get_book_info():
        with open('book_admin.txt',
                  'r') as file:
            data = file.readlines()

        return data
        
    
import ast

def get_data_in_list(data):
    # type change
    try:
        data = ast.literal_eval(data)

        if type(data) == str:
            raise Exception
        
        # 타입이 리스트거나 딕셔너리 일경우 재귀
        for i in data:
            get_data_in_list(i)
    # 리스트나 딕셔너리가아닐 때
    except Exception:
        # Case Dict
        if type(data) == dict:
            Books().set_book_info(name = data['name'],
                                author = data['author'],
                                price = data['price'])
        # Case List
        elif type(data) == list:
            Books().set_book_info(name = data[0],
                          author = data[1],
                          price = data[2])
        


#[['파이썬3 Bible', '이강성', 14000],['무소유', '법정스님', 10000]]
#[{'name':'파이썬', 'author': '이강성', 'price': 14000},{'name':'무소유', 'author': '법정스님', 'price': 10000}]

while(True):        
    print('==@ 넣을 데이터를 넣어주세요.')
    print('e.g >> ["파이썬3 Bible", "이강성", 14000]\n' +
          '        또는 {"name":"파이썬", "author": "이강성", "price": 14000}\n' +
          '(종료 : exit)')

    data = input('>>')

    # Escape Check
    if data == 'exit':
        break
    
    # type change
    try:
        data = ast.literal_eval(data)

        if type(data) == str:
            raise Exception
        
        # list in list in list in일 경우를 대비하여 재귀로
        print('\n==@ 현재 저장 된 데이터 목록\n')
        for i in data:
            get_data_in_list(i)
        else:
            # NoneType Exception
            lines = Books().get_book_info()
            for i in lines:
                print(i,
                      end='')
            
    # Exception
    except Exception as e:
        print(e)
        print('\n==@잘못 된 데이터 입니다.\n')

        
        
    
    
