import random
import outputReport

class Population:
    select_list = dict()
    pop_score = dict()
    chromosome_num = 200

    def __init__(self, level):

        self.level = level
        self.average = []
        self.best = []
        self.worst = []

    # make Population.chromosome_num chromosome
    def makePopulation(self):
        # initialize the population
        count = 0
        while count != Population.chromosome_num:
            p = ""
            for j in range(len(self.level)):
                t = random.randint(0, 2)
                if j > 0:
                    while (t == 1 and p[j - 1] == '1') or (t == 2 and p[j - 1] == '2'):
                        t = random.randint(0, 2)
                p = p + str(t)

            Population.pop_score[p] = 0
            if count != len(Population.pop_score):
                count += 1

    # check success or not
    def check_success(self, chromosome):
        scores = []
        max_score = 0
        #print("len", len(self.level), "chromosome", len(chromosome))
        for i in range(len(chromosome)-1):
            if (chromosome[i]!='1' and self.level[i+1]=='G') or (chromosome[i]!='2' and self.level[i+1]=='L'):
                scores.append(i+1)
        scores.append(len(chromosome)-1)
        if len(scores) == 1:
            max_score = len(chromosome)
        else:
            max_score = scores[0]+1
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
        for i in Population.pop_score.keys():
            score = self.check_success(i)
            if score==len(i):
                score += 5
            score += self.mashroom_hit(i)
            score += self.kill_Gumpa(i)
            Population.pop_score[i]=score

    # select based on scores
    # select the best half of population
    def select(self):
        population_score = {k: v for k, v in sorted(Population.pop_score.items(), key=lambda item: item[1])}
        self.worst.append(list(Population.pop_score.items())[0][1])
        self.best.append(list(Population.pop_score.items())[-1][1])
        filtered_vals = [v for _, v in population_score.items()]
        self.average.append(sum(filtered_vals) / len(filtered_vals))
        Population.select_list = {k: population_score[k] for k in list(population_score)[Population.chromosome_num//2:]}


    def check_repeat(self, chromosome):
        for i in range(len(chromosome)-1):
            if (chromosome[i] == '1' and chromosome[i+1] == '1') or (chromosome[i] == '2' and chromosome[i+1] == '2'):
                return False
        return True

    def crossOver(self):
        population = dict()
        count = 0
        while True:
            parent1 = random.randint(0, ((Population.chromosome_num//2)-1))
            parent2 = random.randint(0, ((Population.chromosome_num//2)-1))

            while (True):
                t = random.randint(1, len(self.level))
                parent1str = list(Population.select_list.items())[parent1][0]
                parent2str = list(Population.select_list.items())[parent2][0]
                if t==6:
                    parent1str = parent1str.replace('1','0', 1)

                child1 = parent1str[:t] + parent2str[t:]
                child2 = parent2str[:t] + parent1str[t:]

                if self.check_repeat(child1) and self.check_repeat(child2):
                    break
            population[child1] = 0
            if len(population) != count:
                count += 1
            if len(population)==Population.chromosome_num:
                break
            population[child2] = 0
            if len(population) != count:
                count += 1
            if len(population)==Population.chromosome_num:
                break
        Population.pop_score = population

    def mutation(self):
        population = dict()
        i = 0
        while True:
            t = random.randint(0, 10)
            if t < 2 and ('1' in list(Population.pop_score.items())[i][0]):
                s = list(Population.pop_score.items())[i][0]
                s = s.replace('1', '0', 1)
                if not(s in Population.pop_score.keys() or (s in population)):
                    population[s] = 0
                    i += 1
                else:
                    population[list(Population.pop_score.items())[i][0]] = 0
                    i += 1
            else:
                population[list(Population.pop_score.items())[i][0]] = 0
                i += 1
            if i==Population.chromosome_num:
                break
        Population.pop_score = population

    def calling_methods(self):
        self.makePopulation()
        for i in range(10):
            self.calculateScore()
            self.select()
            self.crossOver()
            self.mutation()

        print("population average", self.average)
        outputReport.drawing_average_best_worst(self.average, self.best, self.worst)

        return max(self.best)


#chromosome = Population('____G_____')
#print(chromosome.calling_methods())
