class Person:
    people = {}
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self

def create_person_list(people: list) -> list:
    for person in people:
        name = person["name"]
        age = person["age"]
        Person(name, age)
    for peopl in people:
        p = Person.people[peopl["name"]]
        if "wife" in peopl:
            p.wife = Person.people[peopl["wife"]]
        if "husband" in peopl:
            p.husband = Person.people[peopl["husband"]]
    return [Person.people[person["name"]] for person in people]
