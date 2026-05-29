class TeamMember:
    def __init__(self,name,uid):
        self.name= name
        self.uid = uid
    def display(self):
        print("TeamMember: ",{self.name}, "UID: ",{self.uid})

class Worker:
    def __init__(self, pay, jobtitle):
        self.pay = pay
        self.jobtitle = jobtitle
    def display(self):
        print("Worker: ",{self.jobtitle}, "pay: ",{self.pay})

class TeamLeader(TeamMember, Worker):
    def __init__(self, name, uid, pay, jobtitle, exp):
        self.exp = exp
        TeamMember.__init__(self, name, uid)
        Worker.__init__(self, pay, jobtitle)
    def display(self):
        TeamMember.display(self) # explicit calling for team member display
        Worker.display(self) # explicit calling for worker display
        print(f"Experience: {self.exp}")

TL = TeamLeader("Mythily", 1001, 250000, "Scrum Master", 5)
TL.display()        