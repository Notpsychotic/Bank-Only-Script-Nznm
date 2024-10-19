# Pilgrimage Ownership Management System

class Pilgrim:
    def __init__(self, name, age, uniform):
        self.name = name
        self.age = age
        self.uniform = uniform

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Uniform: {self.uniform}"

class PilgrimageOwnership:
    def __init__(self):
        self.pilgrims = []

    def accept_pilgrim(self, name, age, uniform):
        new_pilgrim = Pilgrim(name, age, uniform)
        self.pilgrims.append(new_pilgrim)
        print(f"Accepted {name} into the pilgrimage.")

    def list_pilgrims(self):
        for pilgrim in self.pilgrims:
            print(pilgrim)

if __name__ == "__main__":
    pilgrimage = PilgrimageOwnership()
    pilgrimage.accept_pilgrim("John Doe", 30, "White Robe")
    pilgrimage.accept_pilgrim("Jane Smith", 25, "Blue Robe")
    print("\nList of Pilgrims:")
    pilgrimage.list_pilgrims()
