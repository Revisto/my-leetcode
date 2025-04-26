class Reservation:
    def __init__(self, username, start_time, duration):
        self.username = username
        self.start_time = start_time
        self.end_time = start_time + duration


class Desk:
    def __init__(self, floor_number, desk_number):
        self.id = f"{floor_number}-{desk_number}"
        self.floor_number = floor_number
        self.desk_number = desk_number
        self.reservations = []

    def is_available(self, from_time, duration):
        end_time = from_time + duration
        for reservation in self.reservations:
            if not (
                end_time <= reservation.start_time or from_time >= reservation.end_time
            ):
                return False
        return True

    def assign(self, time, duration, username):
        new_reservation = Reservation(username, time, duration)
        self.reservations.append(new_reservation)

    def __str__(self):
        return self.id


class Floor:
    def __init__(self, floor_number, desks_count, floor_type):
        self.floor_number = floor_number
        self.desks = [
            Desk(floor_number, desk_number) for desk_number in range(1, desks_count + 1)
        ]
        self.floor_type = floor_type

    def get_available_desk(self, from_time, duration):
        for desk in self.desks:
            if desk.is_available(from_time, duration):
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
            available_desk = floor.get_available_desk(timestap, duration)
            if available_desk:
                available_desk.assign(timestap, duration, username)
                if floor.floor_type == "special":
                    return f"{username} got desk {available_desk} for {self.special_floor_fee}"
                return f"{username} got desk {available_desk}"
        return "no desk available"

    def reserve_desk(self, username, timestamp, from_time, duration):
        for floor in self.floors:
            if floor.floor_type != "special":
                continue
            available_desk = floor.get_available_desk(from_time, duration)
            if available_desk:
                available_desk.assign(from_time, duration, username)
                return f"{username} reserved desk {available_desk} for {self.special_floor_fee}"
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

    parts = command.split(" ")
    timestamp = int(parts[0])
    action = parts[1]
    username = parts[2]

    if action == "request_desk":
        floor_type = parts[3]
        duration = int(parts[4])
        result = working_space.request_desk(username, timestamp, duration, floor_type)
        print(result)

    elif action == "reserve_desk":
        from_time = int(parts[3])
        duration = int(parts[4])
        result = working_space.reserve_desk(username, timestamp, from_time, duration)
        print(result)
