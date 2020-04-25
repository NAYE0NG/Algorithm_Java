import sys
sys.setrecursionlimit(1000000)

answer = 0
def swap(numbers, a, b, cnt, K) :
    global answer
    if cnt <= answer :
        # chaeck
        under_K = True
        for i in range(len(numbers)-1) :
            if abs(numbers[i] - numbers[i+1]) > K :
                under_K = False
                break 
        if under_K :
            answer = min(answer, cnt)

        #swap
        for x in range(a, len(numbers)) :
            for y in range(len(numbers)) :
                if x != y and (x,y) != (a,b) and (x,y) != (b,a) :
                    numbers[x], numbers[y] = numbers[y], numbers[x]
                    swap(numbers, x, y, cnt+1, K)
                    numbers[x], numbers[y] = numbers[y], numbers[x]

def solution(numbers, K):
    global answer
    answer = 40321

    swap(numbers, -1, -1, 0, K) 

    if answer == 40321 :
        answer = -1
    return answer

print(solution([3, 7, 2, 8, 6, 4, 5, 1], 3))



"""
문제 설명
자연수 N개가 중복없이 들어있는 배열이 있습니다. 이때, 서로 다른 두 원소의 위치를 바꾸는 Swap 연산을 이용해 원소들의 위치를 바꿔 서로 인접한 원소의 차가 K 이하가 되도록 하려 합니다. 단, Swap 연산을 최대한 적게 사용해야 합니다

배열 numbers가 매개변수로 주어질 때, 서로 인접한 원소의 차가 K 이하가 되도록 하는데 필요한 Swap 횟수의 최솟값을 return 하도록 solution 함수를 완성해주세요.

제한사항
numbers의 길이(N)는 1 이상 8 이하입니다.
numbers의 원소는 1 이상 100 이하인 자연수입니다.
숫자는 중복없이 들어있습니다.
K는 1 이상 100 이하인 자연수입니다.
서로 인접한 원소의 차가 K 이하가 되도록 할 수 있는 방법이 없다면 -1을 return 하세요.
입출력 예
numbers	k	result
[10, 40, 30, 20]	20	1
[3, 7, 2, 8, 6, 4, 5, 1]	3	2
입출력 예 설명
입출력 예 #1
30과 40의 위치를 바꾸면 [10, 30, 40, 20]이 되며, 인접한 원소의 차가 모두 20 이하가 됩니다.

입출력 예 #2
3과 4의 위치를 바꾸고, 2와 5의 위치를 바꾸면 [4, 7, 5, 8, 6, 3, 2, 1]이 되며, 인접한 원소의 차가 모두 3 이하가 됩니다.
"""