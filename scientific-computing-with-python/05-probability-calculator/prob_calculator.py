import copy
import random

class Hat:
    def __init__(self,**kwargs):
        self.contents = []
        for k,v in kwargs.items():
            for i in range(v):
                self.contents.append(k)
        self.full_contents = copy.deepcopy(self.contents)

    def draw(self, num_balls_drawn):
        drawn_balls = []
        if num_balls_drawn <= len(self.contents):
            for r in range(num_balls_drawn):
                index = random.randrange(len(self.contents))
                drawn_balls.append(self.contents.pop(index))
        else:
            # if leftover is less than num_balls_drawn
            # return all
            self.contents = copy.deepcopy(self.full_contents)

            # try to draw but give up if num_balls_drawn is
            # still more than total number of balls
            try:
                for r in range(num_balls_drawn):
                    index = random.randrange(len(self.contents))
                    drawn_balls.append(self.contents.pop(index))
            except ValueError:
                pass
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    M = 0
    N = num_experiments

    expected_contents = []
    for k,v in expected_balls.items():
        for i in range(v):
            expected_contents.append(k)

    for n in range(num_experiments):
        drawn_balls  = hat.draw(num_balls_drawn)

        # count if expected_balls are in the drawn_balls
        c = 0
        for k, v in expected_balls.items():
            if drawn_balls.count(k) >= v:
                c += 1

        # all keys are present in correct amounts or more
        if c == len(expected_balls.keys()):
            M += 1
    
    probability = M / N

    return probability
