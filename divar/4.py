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
    def __init__(self, floor_number, desks_count, floor_type):
        self.floor_number = floor_number
        self.desks = [
            Desk(floor_number, desk_number) for desk_number in range(1, desks_count + 1)
        ]
        self.floor_type = floor_type

    def get_available_desk(self, time):
        for desk in self.desks:
            if desk.is_available(time):
                return desk

        return None

    def __str__(self):
        return f"Floor {self.floor_number}"


class WorkingSpace:
    def __init__(self, floor_desks_count, special_floor_fee):
        self.floors = [
            Floor(
                floor_number=floor_number,
                desks_count=floor_desks_count[floor_number]["count"],
                floor_type=floor_desks_count[floor_number]["type"],
            )
            for floor_number in floor_desks_count
        ]
        self.special_floor_fee = special_floor_fee

    def request_desk(self, username, timestap, duration, floor_type):
        for floor in self.floors:
            if floor.floor_type != floor_type:
                continue
            available_desk = floor.get_available_desk(timestap)
            if available_desk:
                available_desk.assign(timestap, duration, username)
                if floor.floor_type == "special":
                    return f"{username} got desk {available_desk} for {self.special_floor_fee}"
                return f"{username} got desk {available_desk}"
        return "no desk available"


floors_count, special_floor_fee = input().split(" ")
floors_count = int(floors_count)
floor_desks_count = dict()
for floor_number in range(1, floors_count + 1):
    desks_count, floor_type = input().split()
    desks_count = int(desks_count)
    floor_desks_count[floor_number] = {"type": floor_type, "count": desks_count}

working_space = WorkingSpace(floor_desks_count, special_floor_fee)

while True:
    command = input()
    if command == "end":
        break

    timestamp, action, username, floor_type, duration = command.split(" ")
    timestamp = int(timestamp)
    duration = int(duration)

    if action == "request_desk":
        result = working_space.request_desk(username, timestamp, duration, floor_type)
        print(result)
