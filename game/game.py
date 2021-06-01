import population
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
                print("game level" , i)
                self.play(i)
                print("level", i, "score:", self.scores[-1])
            else:
                print("goal is not accessible")

    def play(self, level):
        newPopulation = population.Population(level)
        s = newPopulation.calling_methods()
        self.scores.append(s)

    # check if this level is possible
    def check_possible(self, level):
        for j in range(len(level)-1):
            if (level[j]=='G' and level[j+1]=='L' or level[j]=='L' and level[j+1]=='G'):
                return False
        return True

g = Game(["__M_____", "____G_____", "__G___L_", "__G__G_L___","____G_ML__G_", "____G_MLGL_G_", "_M_M_GM___LL__G__L__G_M__", "____G_G_MMM___L__L_G_____G___M_L__G__L_GM____L____", "___M____MGM________M_M______M____L___G____M____L__G__GM__L____ML__G___G___L___G__G___M__L___G____M__", "_G___M_____LL_____G__G______L_____G____MM___G_G____LML____G___L____LMG___G___GML______G____L___MG___"])
g.playEachLevel()
