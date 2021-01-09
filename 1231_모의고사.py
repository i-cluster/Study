# PROS 완전탐색 42840
# https://bit.ly/3rHgoYo

def solution(answers):
    std = [[1, 2, 3, 4, 5, 5], [2, 1, 2, 3, 2, 4, 2, 5, 8], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 10]]

    score = [0, 0, 0]
    for i in range(len(answers)):
        for j in range(3):
            if std[j][i % std[j][-1]] == answers[i]: score[j] += 1
    return [i + 1 for i in range(3) if score[i] == max(score)]