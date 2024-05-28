class Node:
    def __init__(self, fNumber, fType, pName, capacity, src, dest, date, duration):
        self.fNumber = fNumber
        self.fType = fType
        self.pName = pName
        self.capacity = capacity
        self.src = src
        self.dest = dest
        self.date = date
        self.duration = duration
        self.next = None

class FlightLinkedList:
    def __init__(self):
        self.head = None

    def add_flight(self, fNumber, fType, pName, capacity, src, dest, date, duration):
        new_flight = Node(fNumber, fType, pName, capacity, src, dest, date, duration)
        if not self.head:
            self.head = new_flight
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_flight

    def delete_flight(self, fNumber):
        current = self.head
        prev = None
        while current:
            if current.fNumber == fNumber:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True
            prev = current
            current = current.next
        return False

    def update_flight(self, fNumber, new_flight_data):
        current = self.head
        while current:
            if current.fNumber == fNumber:
                current.fNumber = new_flight_data['fNumber']
                current.fType = new_flight_data['fType']
                current.pName = new_flight_data['pName']
                current.capacity = new_flight_data['capacity']
                current.src = new_flight_data['src']
                current.dest = new_flight_data['dest']
                current.date = new_flight_data['date']
                current.duration = new_flight_data['duration']
                return True
            current = current.next
        return False
    def display_flights(self):
        current = self.head
        while current:
            print(f"Flight: {current.fNumber}, Capacity: {current.capacity}, Duration: {current.duration}")
            current = current.next
    def append_flight(self, fNumber, fType, pName, capacity, src, dest, date, duration):
        new_flight = Node(fNumber, fType, pName, capacity, src, dest, date, duration)
        if not self.head:
            self.head = new_flight
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_flight
