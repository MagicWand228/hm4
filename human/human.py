
class Fireworker:
    def __init__(self, attribute_a):
        self.attribute_a = attribute_a

    def method_a(self):
        return f"Fireworker: {self.attribute_a}"

class Policeman:
    def __init__(self, attribute_b):
        self.attribute_b = attribute_b

    def method_b(self):
        return f"Policeman: {self.attribute_b}"

class Medic:
    def __init__(self, attribute_c):
        self.attribute_c = attribute_c

    def method_c(self):
        return f"Medic: {self.attribute_c}"

class ComplexClass(Medic, Policeman, Fireworker):
    def __init__(self, attribute_a, attribute_b, attribute_c):
        Medic.__init__(self, attribute_a)
        Policeman.__init__(self, attribute_b)
        Fireworker.__init__(self, attribute_c)

    def display_all(self):
        return f"{self.method_a()} | {self.method_b()} | {self.method_c()}"



complex_object = ComplexClass("Value A", "Value B", "Value C")

print(complex_object.display_all())