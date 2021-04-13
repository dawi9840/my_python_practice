class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age
'''
d1 = Dog("AAA", 18)
d2 = Dog("BBB", 31)
print("dog1 name: ", d1.name)
print("dog2 age: ", d2.age)
d2.set_age(23)
print("d2_v2 dog age: ", d2.get_age())
'''
#d3 = Dog("CCC", 19)
#print("dog3 name: ", d3.get_name())
'''
dogs_name = ["Bob", "Tim"]
dogs_age = [32, 14]
'''
IMAGE_SIZE = 64
img_rows, img_cols = IMAGE_SIZE, IMAGE_SIZE
print("img_rows:", img_rows)
print("img_cols:", img_cols)
