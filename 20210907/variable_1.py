# challenge:
# 1~9 사이의 정수 a를 입력받아 a + aa + aaa + aaaa 의 값을 계산하는 프로그램을 작성하십시오.
# site: https://swexpertacademy.com/main/solvingProblem/solvingProblem.do

import sys

sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    a = input()
    ret = int(a) + int(a + a) + int(a + a + a) + int(a + a + a + a)
    print(ret)
    # ///////////////////////////////////////////////////////////////////////////////////
