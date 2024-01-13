class Event:
    def __init__(self, name, event_type):
        self.name = name
        self.event_type = event_type
        self.participants = []

    def add_participant(self, participant):
        self.participants.append(participant)

    def determine_points(self):
        # You can implement the logic to determine points based on event type and participants' ranks.
        pass