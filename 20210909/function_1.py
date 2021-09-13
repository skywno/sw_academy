# challenges: https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do


import sys

sys.stdin = open("function_1_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    word = input()
    if word == word[::-1]:
        print(word)
        print("입력하신 단어는 회문 (palindrome)입니다.")
