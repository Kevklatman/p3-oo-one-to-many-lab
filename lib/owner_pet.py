

class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all=[]
    def __init__(self, name, pet_type, owner=None):
        self.name=name
        if pet_type not in Pet.PET_TYPES:
            raise Exception("is not pet type")
        self.pet_type=pet_type
        self.owner=owner
        Pet.all.append(self)


class Owner:
    def __init__(self, name):
        self.name=name
    def add_pet(self, pet):
        if not isinstance(Pe):
            raise Exception("Invalid pet. Expected an instance of Pet.")
        self.pets.append(pet)
    def pets(self):
        return self.pets