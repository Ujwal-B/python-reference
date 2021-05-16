class chef:
    # custom functions
    def make_chicken(self):
        print("The chef makes chicken")
    def make_salad(self):
        print("The chef makes salad")
    def make_special_dish(self):
        print("The chef makes biryani")

class chinese_chef(chef):                       # the chinese_chef class inherits all characteristics of the chef class
    def make_special_dish(self):                # the make_special_dish() function is overwritten to suit the new class
        print("The chef makes fried noodles")
    def make_fried_rice(self):                  # other custom functions which aren't there in the parent class
        print("The chef makes fried rice")

mychef1 = chef()
mychef2 = chinese_chef()
mychef1.make_special_dish()                     # executes function from chef class
mychef2.make_special_dish()                     # executes function from chinese_chef class
