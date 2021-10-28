Nation = {}
Population = 0

def Add_State():
    State(input('Enter Name of State: '))

class State:
    def __init__(self, name):
        self.name = name
        self.cities = {}
        Nation[self.name] = self
    def Add_City(self):
        name = input('Enter Name of City: ')
        NewCity = City(name)
        self.cities[NewCity.name] = NewCity

class City:
    def __init__(self, name):
        self.name = name
        self.people = {}
    def Add_Person(self):
        name, age = input('Enter Name of Person: '), int(input('Enter Age of Person: '))
        NewPerson = Person(name, age)
        self.people[NewPerson.name] = NewPerson

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.box = []
        global Population
        Population += 1
    def Store(self, item):
        self.box.append(item)

print(Nation, Population)
print('--------------------')

Add_State()
print(Nation)
state = list(Nation.keys())[0]
Nation[state].Add_City()
print(Nation[state].cities)
city = list(Nation[state].cities.keys())[0]
Nation[state].cities[city].Add_Person()
print(Nation[state].cities[city].people)
person = list(Nation[state].cities[city].people.keys())[0]
Nation[state].cities[city].people[person].Store(input('Item: '))
print(Nation[state].cities[city].people[person].name, 
Nation[state].cities[city].people[person].age, 
Nation[state].cities[city].people[person].box)

print('--------------------')
print(Nation, Population)

# TODO: script to make many states, cities, people, items...



