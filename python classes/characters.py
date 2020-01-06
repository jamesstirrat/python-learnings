import random

class Warrior:
    sneaky = True

    def __init__(self, name, sneaky=True, **kwargs):
        self.name = name
        self.sneaky = sneaky 
    
        for key, value in kwargs.items():
            setattr(self, key, value)
        
    def pickpocket(self):    
            print("Called by {}".format(self))
            return self.sneaky and bool(random.randint(0, 1))
    
    def hide(self, light_levels):
        return self.sneaky and light_levels < 10
            