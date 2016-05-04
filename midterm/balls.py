import random

def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
    '''
    counter = 0.0
    for i in range(numTrials):
        balls = ["red" for m in range(4)] + ["green" for n in range(4)]
        draw = []
        for x in range(3):
            number = int(random.random() * len(balls))
            draw.append(balls[number])
            del balls[number]
        if all(ball == "red" for ball in draw) or all(ball == "green" for ball in draw):
            counter += 1
    return counter / numTrials

print drawing_without_replacement_sim(1000)