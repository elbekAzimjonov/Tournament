class Team:
    def __init__(self, name):
        self.name = name
        self.members = []

    def add_member(self, participant):
        if len(self.members) < 5:
            self.members.append(participant)
        else:
            print(f"Team {self.name} is already full.")