# 임시파일(tempfile) 모듈 : 임시적으로 파일을 만들어 사용할때 유용하게 쓰이는 모듈이다.
"""
tempfile.mktemp() : 임시로 파일을 만들어서 돌려주는 함수(중복되지 않도록 만들어준다.)

tempfile.TemporaryFile() : 임시적인 저장공간으로 사용될 파일 객체를 돌려주는 함수,  w+b 모드를 갖는다.

mode		|		해설
-------------------------------------
  w		    | 쓰기모드로 파일 열기
  r			| 읽기모드로 파일 열기
  a			| 추가모드로 파일 열기
  b			| 바이너리 모드로 파일 열기
-------------------------------------

w+, r+, a+ 파일을 업데이트 할 용도로 사용
b는 w, r, a 뒤에 붙여서 사용한다.

r : 단지 읽기 위해서 사용하는 모드, 포인터위치는 파일 처음에 위치한다.
r+ : 읽기와 쓰기 모드로 파일을 연다. 포인터위치는 파일 처음에 위치한다.

w : 파일을 쓰기모드로 열고, 파일이 없는 경우에는 새로 만든다. 포인터위치는 파일 처음에 위치한다.
w+ : 읽기와 쓰기 모드로 열고, 파일이 없을 경우에는 새로 만든다. 포인터의 위치는 파일 처음에 위치한다.

a: 쓰기모드로 파일을 열고, 파일이 없는 경우에는 새로 만든다. 포인터위치는 파일의 끝에 위치한다.
a+ : 읽기와 쓰기모드로 파일을 연다. 파일이 존재하지 않을 경우에는 파일을 생성한다. 포인터의 위치는
파일 끝에 위치한다.

모드활용 예>>>
	파일 읽으려면 ----> r, r+, w+, a+
	파일을 쓰려면 ----> r+, w, w+, a, a+
	없는 파일을 생성하려면 -----> w, w+, a, a+
	파일을 덮어쓰려면 ------> w, w+
	파일을 덧붙이려면 -------- 앞쪽에 붙이려면 :r+
								|
								+--- 뒷쪽에 붙이려면 :a, a+
"""