# Total score is sum of scores for each round.
# Score of a single round is the score for the shape you selected, 1 rock 2 paper 3 scissors PLUS the outcome of the round (0 loss 3 tie 6 win)


# Need to change the X Y Z from rock paper scissors, to whatever wins, draws, loses. x = lose y = draw z = win

with open('puzzleinput.txt', 'r') as input:
    score = 0
    for line in input:
        round = line.split()
        # Whatever loses
        if round[1] == 'X':
            if round[0] == 'A':
                score += 3
            elif round[0] == 'B':
                score += 1
            elif round[0] == 'C':
                score += 2

        elif round[1] == 'Y':
            score += 3
            if round[0] == 'A':
                score += 1
            elif round[0] == 'B':
                score += 2
            elif round[0] == 'C':
                score += 3

        elif round[1] == 'Z':
            score += 6
            if round[0] == 'A':
                score += 2
            elif round[0] == 'B':
                score += 3
            elif round[0] == 'C':
                score += 1
    print(score)