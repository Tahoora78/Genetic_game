import random


class Population:
    def __init__(self, level):

        self.level = level
        self.population_score = dict()


    # TODO: make 200 chromosome
    def makePopulation(self):
        # initialize the population
        count = 0
        while count != 200:
            p = ""
            for j in range(len(self.level)):
                t = random.randint(0, 2)
                p = p + str(t)
            self.population_score[p] = 0
            if count != len(self.population_score):
                count += 1

    #TODO: check success or not
    def check_success(self, chromosome):
        scores = []
        max_score = 0
        for i in range(len(chromosome)-1):
            if (chromosome[i]!='1' and self.level[i+1]=='G') or (chromosome[i]!='2' and self.level[i+1]=='L'):
                scores.append(i+1)
        scores.append(len(chromosome)-1)
        if len(scores) == 1:
            max_score = len(chromosome)
        else:
            print("scores", scores)
            max_score = scores[0]+1
            print("sc", max_score)
            for j in range(0, len(scores)-1):
                score = abs(scores[j+1]-scores[j])
                if score > max_score:
                    max_score = score
        return max_score

    # TODO: calculate the score
    #
    def mashroom_hit(self, chromosome):
        score = 0
        for i in range(len(chromosome)-1):
            if self.level[i]=='M' and chromosome[i-1]!='1':
                score +=2
        return score

    def kill_Gumpa(self, chromosome):
        score = 0
        if 'G' in self.level:
            for i in range(len(self.level)-2):
                if self.level[i] == 'G' and chromosome[i-2]=='1':
                    score += 2
        return score

    def calculateScore(self):
        #self.population_score[chromosome]=0
        for i in self.population_score.keys():
            score = self.check_success(i)
            print("scoreee", score)
            if score==len(i):
                score += 5
            score += self.mashroom_hit(i)
            score += self.kill_Gumpa(i)
            self.population_score[i]=score

    # TODO: select based on scores
    # select the best half of population
    def select(self):
        population_score = {k: v for k, v in sorted(self.population_score.items(), key=lambda item: item[1])}
        print("population", population_score)

    def crossOver(self):
        pass

    def mutation(self):
        pass
chromoseme = Population('__G__M__')
chromoseme.makePopulation()
chromoseme.calculateScore()
chromoseme.select()