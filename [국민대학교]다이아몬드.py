#-*- coding: utf-8 -*-
'''
== Diamond Printing
[국민대학교]20093326_이의재
'''

# Width and Height min size 3
# Size is odd

# Exception
MIN, MAX = 3, 99999
while(True):
        size = input("최솟값 : 3\n최댓값 : 99999\n홀 수만 입력가능 >>")

        try:
                # Str To Integer
                size = int(size)
                
                # 범위 및 홀수 검사
                if MIN <= size\
                   and size <= MAX\
                   and size % 2 == 1:
                        break
                else:print('\m==@범위 및 홀수를 확인 하세요.\n')
        except Exception.ValueError:
                # Integer형이 아닐 대
                print('숫자를 입력하세요.')
                
print('Size : {0:2}\n==@정마름모의 다이아몬드를 출력.\n'.format(size))
data = []
for i in range(size):
        # center line
        if i == int(size / 2):
                repeat = size
        # edge line
        elif i == 0 or i == size -1:
                repeat = 1
        else:
                repeat = size - (abs(int(size / 2) - i) * 2)       
        data.append('{0:^{1}}'.format('*' * repeat, size))

with open('{0}Diamond.txt'.format(size),
          'w') as file:
        file.write('Size : {0:2}\n==@정마름모의 다이아몬드를 출력.\n'.format(size))
        for i in data:
                file.write(i + '\n')
                print(i)
        

