import chromosome
import random
import outputReport


class Game:
    def __init__(self, levels):
        # Get a list of strings as levels
        # Store level length to determine if a sequence of action passes all the steps
        self.levels = levels
        self.scores = []

    def playEachLevel(self):
        for i in self.levels:
            if self.check_possible(i):
                ch = chromosome.Population(i)
                s = ch.calling_methods()
                self.scores.append(s)
                del ch
                #self.scores.append(chromosome.Population(i).calling_methods())
                print("level", i, "score:", self.scores[-1])
            else:
                print("goal is not accessible")

    # check if this level is possible
    def check_possible(self, level):
        for j in range(len(level)-1):
            if (level[j]=='G' and level[j+1]=='L' or level[j]=='L' and level[j+1]=='G'):
                return False
        return True

g = Game(["__G___L_", "__M_____", "____G_____","__G__G_L___","__G__G_L___"])
g.playEachLevel()
