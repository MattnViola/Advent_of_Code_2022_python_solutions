# Total score is sum of scores for each round.
# Score of a single round is the score for the shape you selected, 1 rock 2 paper 3 scissors PLUS the outcome of the round (0 loss 3 tie 6 win)

with open('puzzleinput.txt', 'r') as input:
    score = 0
    for line in input:
        round = line.split()
        # Check for score awarded from choice. Then check if it won or draw and add points.
        if round[1] == 'X':
            score += 1
            if round[0] == 'A':
                score += 3
            elif round[0] == 'C':
                score += 6
        elif round[1] == 'Y':
            score += 2
            if round[0] == 'B':
                score += 3
            elif round[0] == 'A':
                score += 6
        elif round[1] == 'Z':
            score += 3
            if round[0] == 'C':
                score += 3
            elif round[0] == 'B':
                score += 6
    print(score)
