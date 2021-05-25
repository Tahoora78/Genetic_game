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
                t = random.randint(0,2)
                p = p + str(t)
            self.population[p] = 0
            if count != len(self.population):
                count += 1

    #TODO: check success or not
    def check_success(self, chromosome):
        score = []
        for i in range(len(chromosome)-1):
            if (chromosome[i]!='1' and self.level[i+1]=='G') or (chromosome[i]!='2' and self.level[i+1]=='L'):
                score.append(i)



    # TODO: calculate the score
    #
    def calculateScore(self):

        for i in self.population_score:
            pass


    # TODO: select based on scores
    # select the best half of population
    def select():
        pass

    def crossOver():
        pass

    def mutation():
        pass
chromoseme = Chromosome('___g__m_')
d = chromoseme.makePopulation()
