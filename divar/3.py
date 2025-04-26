class Desk:
    def __init__(self, floor_number, desk_number):
        self.id = f"{floor_number}-{desk_number}"
        self.floor_number = floor_number
        self.desk_number = desk_number
        self.assigned_to = None
        self.end_time = 0

    def is_available(self, time):
        if self.assigned_to is None:
            return True

        return self.end_time <= time

    def assign(self, time, duration, assigned_to):
        self.assigned_to = assigned_to
        self.end_time = time + duration

    def __str__(self):
        return self.id


class Floor:
    def __init__(self, floor_number, desks_count):
        self.floor_number = floor_number
        self.desks = [
            Desk(floor_number, desk_number) for desk_number in range(1, desks_count + 1)
        ]

    def get_available_desk(self, time):
        for desk in self.desks:
            if desk.is_available(time):
                return desk

        return None

    def __str__(self):
        return f"Floor {self.floor_number}"


class WorkingSpace:
    def __init__(self, floor_desks_count):
        self.floors = [
            Floor(floor_number, floor_desks_count[floor_number])
            for floor_number in floor_desks_count
        ]

    def request_desk(self, username, timestap, duration):
        for floor in self.floors:
            available_desk = floor.get_available_desk(timestap)
            if available_desk:
                available_desk.assign(timestap, duration, username)
                return f"{username} got desk {available_desk}"
        return "no desk available"


floors_count = int(input())
floor_desks_count = dict()
for floor_number in range(1, floors_count + 1):
    desks_count = int(input())
    floor_desks_count[floor_number] = desks_count

working_space = WorkingSpace(floor_desks_count)

while True:
    command = input()
    if command == "end":
        break

    timestamp, action, username, duration = command.split(" ")
    timestamp = int(timestamp)
    duration = int(duration)

    if action == "request_desk":
        result = working_space.request_desk(username, timestamp, duration)
        print(result)
