class Player:
    def __init__(self,firstname,lastname,team=None):
        self.first_name=firstname
        self.last_name=lastname
        self.scores=[]
        self.team=team

    def add_score(self,score):   
        self.scores.append(score)
        return None

    def total_score(self):
        totalscore=sum(self.scores)
        return totalscore

    def average_score(self):
        
        ave_score=self.total_score()/len(self.scores)
        return ave_score
            
            
torres= Player('Fernando','Torres','Chelsea')
for i in range(5):
    goals=int(input('enter the goals: '))
    torres.add_score(goals)
print torres.total_score()
print torres.average_score()


    
