import random


class Population:
    def __init__(self, level):

        self.level = level
        self.population_score = dict()
        self.selectList = None


    # TODO: make 200 chromosome
    def makePopulation(self):
        # initialize the population
        count = 0
        while count != 200:
            p = ""
            for j in range(len(self.level)):
                t = random.randint(0, 2)
                if j > 0:
                    while t == 1 and p[j - 1] == '1':
                        t = random.randint(0, 2)

                    while t == 2 and p[j - 1] == '2':
                        t = random.randint(0, 2)
                p = p + str(t)
            self.population_score[p] = 0
            if count != len(self.population_score):
                count += 1

    # check success or not
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

    # calculate the score
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

    # select based on scores
    # select the best half of population
    def select(self):
        population_score = {k: v for k, v in sorted(self.population_score.items(), key=lambda item: item[1])}
        self.selectList = {k: population_score[k] for k in list(population_score)[100:]}
        print("len", len(self.selectList))

    def check_repeat(self, chromosome):
        for i in range(len(chromosome)-1):
            if (chromosome[i] == '1' and chromosome[i+1] == '1') or (chromosome[i] == '2' and chromosome[i+1] == '2') :
                return False
        return True

    def crossOver(self):
        population = dict()

        count = 0
        while count < 200:
            parent1 = random.randint(0, 99)
            parent2 = random.randint(0, 99)

            while (True):
                t = random.randint(1, len(self.level))

                parent1str = list(self.selectList.items())[parent1][0]
                parent2str = list(self.selectList.items())[parent2][0]

                child1 = parent1str[:t] + parent2str[t:]
                child2 = parent2str[:t] + parent1str[t:]

                if self.check_repeat(child1) and self.check_repeat(child2):
                    break

            population[child1] = 0
            if len(population) != count:
                count += 1

            population[child2] = 0
            if len(population) != count:
                count += 1

            print("child , parent 1", child1, parent1str)
            print("child , parent 2", child2, parent2str)

        self.population_score = population

    def mutation(self):
        population = dict()
        for i in range(100):
            t = random.randint(0, 10)
            print("t in mu", t)
            if t < 2:
                if '1' in list(self.population_score.items())[i][0]:
                    s = list(self.population_score.items())[i][0]
                    s = s.replace('1', '0', 1)
                    population[s] = 0
            else:
                population[list(self.population_score.items())[i][0]] = 0

        self.population_score = population



chromosome = Population('__G__M__')
chromosome.makePopulation()
chromosome.calculateScore()
chromosome.select()
chromosome.crossOver()
chromosome.mutation()