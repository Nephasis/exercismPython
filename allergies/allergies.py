def is_power_2(num):
    return ((num & (num - 1)) == 0) and num > 0

class Alergies:

    def __init__(self, score):
        self.score = score
        self.alergenes = {
            'eggs': 1,
            'peanuts': 2,
            'shellfish': 4,
            'strawberries': 8,
            'tomatoes': 16,
            'chocolate': 32,
            'pollen': 64,
            'cats': 128
        }

    def is_allergic_to(self, alergene):
        if self.score == 0:
            return False
        elif is_power_2(self.score):
            return self.score
        else:
            pass

print Alergies(4).is_allergic_to('cats')
print Alergies(4).score
