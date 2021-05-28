import chromosome

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
                print("level" , i, "score:", s)
            else:
                print("goal is not accessible")

    # check if this level is possible
    def check_possible(self, level):
        for j in range(len(level)-1):
            if (level[j]=='G' and level[j+1]=='L' or level[j]=='L' and level[j+1]=='G'):
                return False
        return True

g = Game(["____G__L__", "___G_M___L_"])
g.playEachLevel()
