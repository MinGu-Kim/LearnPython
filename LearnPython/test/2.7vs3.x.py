#파이썬 2.7 과 파이썬 3.x의 차이점

'''
[ print문 사용의 차이점 ]

2.7 예>>>print "안녕 파이썬!!!"  (괄호를 사용해도 상관 없다. 2.7 이하 버전에서는 오류가 발생할 수 있다.)

3.x 예>>> print ("안녕 파이썬!!!") (괄호를 사용하지 않을 경우에는 오류가 발생한다.)

 [ 줄바꿈(\n:개행문자) 방지의 차이점]

  -- 기본적으로 파이썬에서는 print문 실행시에 항상 문자열 끝에 \n문자가 출력되도록 한다.
      개행(줄바꿈)이 일어나도록 하기 위함이다. 이러한 개행문자를 생략할 수 있는 방법은
	  2.7과 3.x버전에서 차이가 있다.

	  3.x버전에서는 end파라미터를 이용해서 끝 문자를 설정하여 \n을 생략할 수 있다.
	  2.7 버전에서는 콤마(,)를 이용하여 \n을 생략하였다.

 2.7 예>>>print "안녕 파이썬!!!",;print "하이"
 3.x 예>>>print ("안녕 파이썬!!!", end = " ");print ("하이")

[자동 형변환의 차이점]

3.x 버전에서는 숫자 연산시 자동으로 형변환(캐스팅)이 이루어진다.
2.7 버전에서는 형변환이 이루어지지 않는다.

3.x 예>>> 5/2
        2.5 (결과값이 실수형이 나온다.)


2.7 예>> 5/2
        2
        >> 5/2.0
		2.5

[input 사용의 차이점]

3.x버전에서는 input 내장함수를 이용하여 키보드로부터 입력을 받지만,
2.7버전에서는 raw_input 내장함수를 이용하였다.

3.x버전에서는 raw_input 더이상 지원하지 않는다.

[소스 인코딩의 차이점]

2.7버전에서는 utf-8 를 사용하기 위해서
첫줄에 # -*- coding: utf-8 -*- 사용했다.

3.x 버전에서는 utf-8이 기본 소스 인코딩으로 지정 되었다.
utf-8 이외에 다른 인코딩을 사용해야 할 경우에는 해당 인코딩을 첫줄에 명시해야한다.
예> # -*- coding: euc-kr -*-

2.7버전에서는 utf-8을 사용하기 위해서는 첫줄에 인코딩을 명시해야지만
인코딩 오류를 막을 수 있다.

[예외 처리 차이점]
try~except 사용시 except문의 에러변수명 표기 방식이 다르다.

3.x 예>
try:
	2/0
except ZeroDivisionError as e:
	print("0으로 나눌 수 없습니다")

2.7 예>
try:
	2/0
except ZeroDivisionError, e:
	print("0으로 나눌 수 없습니다")

3.x : as 사용
2.7: 콤마(,) 사용
'''
