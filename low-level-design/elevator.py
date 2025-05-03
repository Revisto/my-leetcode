
from enum import Enum

class Direction(Enum):
    DOWN = -1
    IDLE = 0
    UP = 1

class Request:
    def __init__(self, pick_up_floor):
        self.pick_up_floor = pick_up_floor

class ElevatorDisplay:
    @staticmethod
    def open_doors(floor):
        print(f"Opening doors at floor: {floor}")
    def close_doors(floor):
        print(f"Closing doors at floor: {floor}")
    def enter_destination(floor):
        print(f"Level {floor}: Get in passengers")
        destination = int(input("Please enter your destination: "))
        return destination

class Elevator:
    def __init__(self, id, current_floor = 0):
        self.id = id
        self.pick_up_floors = list()
        self.destination_floors = list()
        self.direction = Direction.IDLE
        self.current_floor = current_floor
    
    def step(self):
        if self.destination_floors == list() and self.pick_up_floors == list():
            self.direction = Direction.IDLE
            return
        
        if self.current_floor in self.destination_floors + self.pick_up_floors:
            ElevatorDisplay.open_doors(self.current_floor)
            while self.current_floor in self.destination_floors:
                self.destination_floors.remove(self.current_floor)

            if self.current_floor in self.pick_up_floors:
                self.new_destination(ElevatorDisplay.enter_destination(self.current_floor))
            while self.current_floor in self.pick_up_floors:
                self.pick_up_floors.remove(self.current_floor)
            ElevatorDisplay.close_doors(self.current_floor)
            return

        if self.direction != Direction.DOWN:
            if self.get_highest_floor_to_go() > self.current_floor:
                self.direction = Direction.UP
                self.current_floor += 1
            else:
                self.direction == Direction.DOWN
                self.current_floor -= 1
            return
        
        if self.direction != Direction.UP:
            if self.get_lowest_floor_to_go() < self.current_floor:
                self.direction = Direction.DOWN
                self.current_floor -= 1
            else:
                self.direction == Direction.UP
                self.current_floor += 1
            return
        
    def new_pick_up(self, floor):
        self.pick_up_floors.append(floor)
        self.pick_up_floors.sort()
    
    def new_destination(self, floor):
        self.destination_floors.append(floor)
        self.destination_floors.sort()

    def get_lowest_floor_to_go(self):
        go_to_floors = list()
        if self.destination_floors:
            go_to_floors.append(self.destination_floors[0])
        if self.pick_up_floors:
            go_to_floors.append(self.pick_up_floors[0])
        return min(go_to_floors)
        

    def get_highest_floor_to_go(self):
        go_to_floors = list()
        if self.destination_floors:
            go_to_floors.append(self.destination_floors[-1])
        if self.pick_up_floors:
            go_to_floors.append(self.pick_up_floors[-1])
        return max(go_to_floors)

    def __str__(self):
        return f"Elevator {self.id} At {self.current_floor}, Direction: {self.direction}"

class ElevatorManger:
    def __init__(self, elevators):
        self.elevators = elevators

    def find_elevator_score(self, elevator: Elevator, request: Request):
        if elevator.current_floor == request.pick_up_floor:
            return float("inf")
        if elevator.current_floor > request.pick_up_floor:
            if elevator.direction != Direction.UP:
                return -1 * (elevator.current_floor - request.pick_up_floor)
            else:
                return -1 * ((max(elevator.destination_floors[-1], elevator.pick_up_floors[-1]) - elevator.current_floor) + (elevator.current_floor - request.pick_up_floor))
        else:
            if elevator.direction != Direction.DOWN:
                return -1 * (request.pick_up_floor - elevator.current_floor) 
            else:
                return -1 * ((elevator.current_floor - min(elevator.destination_floors[0], elevator.pick_up_floors[0])) + (request.pick_up_floor - elevator.current_floor))

    def find_best_elevator(self, request: Request):
        best_score = float("-inf")
        best_elevator = None
        for elevator in self.elevators:
            current_score = self.find_elevator_score(elevator, request)
            print(current_score)
            if best_score < current_score:
                best_score = current_score
                best_elevator = elevator
        return best_elevator

    def request_elevator(self, request: Request):
        chosen_elevator = self.find_best_elevator(request)
        chosen_elevator.new_pick_up(request.pick_up_floor)

    def process(self, steps):
        for i in range(steps):
            print("-" * 56)
            for elevator in elevators:
                elevator.step()
                print(elevator)

elevators = [
    Elevator("A", 0),
    Elevator("B", 0),
]
manager = ElevatorManger(elevators)
manager.process(2)
manager.request_elevator(Request(5))
manager.process(2)
manager.request_elevator(Request(4))
manager.process(10)

