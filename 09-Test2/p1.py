def f(player1, player2):
    score1, score2 = 0, 0
    for i in player1:
        if i == "A" or i == "Q" or i == "K" or i == "J" or i == "T":
            score1 += 10
        else:
            score1 += int(i)
    for j in player2:
        if j == 'A' or j == "Q" or j == "K" or j == "J" or j == "T":
            score2 += 10
        else:
            score2 += int(j)
    return score1 > score2


print(f("AJ972","AQT72"))
print(f("9532","K8"))
print(f("987","AT4"))