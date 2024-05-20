import math #pi와 sqrt구현을 위하여 사용함

class Line:
    def __init__(self, length = 1): #초기값은 1로 설정된다.
        if type(length) == int or type(length) == float: #매개변수가 int or float인지 확인
            if length > 0: #매개변수가 0이상인지 확인
                pass
            else:
                length = 1 #초기값 1로 설정된다.
        else:
            length = 1 #초기값 1로 설정된다.
        self.__length = length
    def set_length(self, length): #length값을 수정할 수 있다.
        if type(length) == int or type(length) == float:  # 매개변수가 int or float인지 확인
            if length > 0:  # 매개변수가 0이상인지 확인
                self.__length = length

    def get_length(self): #length값을 얻을 수 있다.
        return self.__length
def area_square(line):
    """길이를 입력받아 정사각형의 넓이를 계산하는 함수
    :param line: int or float Line 클래스의 객체,한변의 길이가 된다.
    :return: int or float 사각형 넓이 출력
    """
    if type(line) == Line:
        return line.get_length() ** 2
    else:
        return 0 #매개변수의 타입이 Line이 아니라면 0반환
def area_circle(line):
    """길이를 입력받아 원의 넓이를 계산하는 함수
    :param line: int or float Line 클래스의 객체,반지름 길이가 된다.
    :return: int or float 원 넓이 출력
    """
    if type(line) == Line:
        return line.get_length() ** 2 * math.pi
    else:
        return 0 #매개변수의 타입이 Line이 아니라면 0반환
def area_regular_triangle(line):
    """길이를 입력받아 정삼각형의 넓이를 계산하는 함수
    :param line: int or float Line 클래스의 객체,한변의 길이가 된다.
    :return: int or float 정삼각형 넓이 출력
    """
    if type(line) == Line:
        return line.get_length() ** 2 * math.sqrt(3)/4
    else:
        return 0 #매개변수의 타입이 Line이 아니라면 0반환

