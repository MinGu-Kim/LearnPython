''' [[ 파일 입출력 ]]

   . 파일 생성

   파일객체 = open(파일이름, 파일 열기모드)

   --- 파일 열기 모드 --
   .. r 모드 : 읽기모드 - 파일을 읽기 용도로 사용할때
   .. w 모드 : 쓰기모드 - 파일에 내용을 쓸 때 (쓰기모드로 열 때
                                파일이 존재하는 경우에는 원래있던 내용이 모두 지워지고 열린다.
								파일이 존재하지 않을 경우에는 새로운 파일 생성된다.)
   .. a 모드 : 추가모드 - 파일에 새로운 내용을 추가 할 때

'''

# fp = open("test_new.txt", 'w')

#close()는 생량해도 무방하다. 파이썬에서는 프로그램 종료시 열린 파일 객체들을 자동으로 닫아준다.
#그렇지만, 될수 있으면 직접 닫아주는것이 올바른 방법이다.
#쓰기 모드로 열었던 파일을 닫지 않고 재사용하는 경우에는 에러가 발생하기 때문에
#닫아주는 습관을 갖자!!
# fp.close()
#
# # 파일에 내용을 출력하기
# fp = open("test_new.txt", 'w')
# for.py i in range(1,5) :
#     content = "%d 번째 줄...\n" %i
#     fp.write(content)
#
# fp.close()
#
# for.py i in range(1,10) :
#     content = "%d 번째 줄..." % i
#     print(content)

# 파일을 읽어 오는 방법 : readline()

fp = open("test_new.txt", 'r')
date = fp.readline() # 읽어온 첫번째 라인을 리턴
print(date)
fp.close()

fp = open("test_new.txt", 'r')
if __name__ == '__main__':
    while True : # true와 True는 서로 다르다. 참과 거짓을 나타내는 것은 True, False
        data = fp.readline() # 더이상 파일에서 읽어올 라인이 없는 경우에는 None을 리턴한다
        if not data : break
        print(data)

# readlines() : 파일 전체 내용 읽어 옴
fp = open("test_new.txt", 'r')
datas = fp.readlines() # readlines() 리턴값이 리스트이다.
print(datas)           # 이함수는 모든 라인을 읽어서 리스트에 리턴한다.
for data in datas :
    print(data)

fp.close()

# .read() 함수를 이용한 파일 읽기
fp = open("test_new.txt", 'r')
data = fp.read() # read()함수는 파일 내용 전체를 문자열로 리턴을한다.
print("====================")
print(data)
fp.close()

# a 모드를 이용해서 파일에 내용을 추가하기
# fp = open("test_new.txt", 'a')
#
# for.py i in range(4,7) :
#     data = "%d line... \n" %i
#     fp.write(data)
# fp.close()

# with문을 이용해서 파일 객체  : with문을 이용하면 파일을 닫을 필요없다. 자동으로 파일을 닫아준다.
fp = open("test_2.txt", 'w')
fp.write("file in out second test")
fp.close()

with open("test_2.txt", 'w') as fp:
    fp.write("file in out with test")