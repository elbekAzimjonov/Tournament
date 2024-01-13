class Tournament:
    def __init__(self):
        self.individual_participants = []
        self.teams = []
        self.events = []

    def add_individual_participant(self, participant):
        if len(self.individual_participants) < 20:
            self.individual_participants.append(participant)
        else:
            print("Tournament is full for individual participants.")

    def add_team(self, team):
        if len(self.teams) < 4:
            self.teams.append(team)
        else:
            print("Tournament is full for teams.")

    def add_event(self, event):
        self.events.append(event)

    def run_tournament(self):
        for event in self.events:
            event.determine_points()