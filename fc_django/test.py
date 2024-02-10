def func():
    print('hello world')

func()

'''
# 가변 인자 리스트
    - *args
    - 함수 정의에서 매개변수 이름 앞에 *을 붙여서 정의
    - 여러 인자를 유연하게 처이할 수 있게 활용
    - 튜플로 묶여서 전달 됨
    - 원하는 만큼의 인자를 전달할 수 있음
    - 다른 매개변수와 함께 사용할 수 있으며, 일반 매개변수 뒤에 위치해야함
    - 하나만 정의 가능
'''
'''
# 키워드 가변 인자 리스트
    - **kwagrs
    - 함수 정의에서 매개변수 이름 앞에 **을 붙여서 정의
    - 여러 인자를 유연하게 처리할 수 있게 활용
    - 딕셔너리로 묶여서 전달
    - 원하는 만큼의 인자를 전달할 수 있음
    - 매개변수 이름과 값을 직접 연결하여 호출(매개변수명 = 값)
'''
'''
# 전역변수와 지역변수
    - 전역변수 : 가상 상위 코드블록에 정의된 변수, 프로그램 어디에서도 사용가능, global
    - 지역변수 : 특정 함수 내에서 정의된 함수, 함수 내부에서만 접근 가능, 지역변수는 함수 호출이 완료되면 자동으로 소명
'''
'''
# 모듈
    - 모듈을 import하여 다른 파일에서 호출할 수 있다.
'''
'''
# 패키지 초기화
    - __init__.py
        - 이 디렉토리가 파이썬 패키지임을 알려주는 파일
        - 패키지 수준에서 사용되는 변수, 함수, 또는 초기화 로직이 정의됨
        - 하위 모듈을 미리 로드하거나, 전역변수를 정의하는 등
        - __all__을 활용하여, 참조하게 만들 모듈만 선택 가능
        ex) __all__ = [
                "모듈1",
                "모듈2",
                "모듈3,
                ]
'''


