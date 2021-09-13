# challenges: https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

import sys


def main():
    sys.stdin = open("function_2_input.txt", "r")

    T = int(input())

    for test_case in range(1, T + 1):
        # ///////////////////////////////////////////////////////////////////////////////////
        player1_name = input()
        player2_name = input()
        player1_hand = input()
        player2_hand = input()
        print(rock_paper_scissor(player1_hand, player2_hand))


def rock_paper_scissor(one, another):
    result = ""
    if one == another:
        result = "비겼습니다!"
    if one == "바위":
        if another == "보":
            result = "보가 이겼습니다!"
        else:
            result = "바위가 이겼습니다!"
    elif one == "보":
        if another == "바위":
            result = "보가 이겼습니다!"
        else:
            result = "가위가 이겼습니다!"
    elif one == "가위":
        if another == "바위":
            result = "바위가 이겼습니다!"
        elif another == "보":
            result = "가위가 이겼습니다!"

    return result


if __name__ == "__main__":
    main()
