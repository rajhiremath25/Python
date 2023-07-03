# in multi level inheritance we have parent, child, grand child

class Parent:
    def assign_name(self, name):
        self.name = name

    def show_name(self):
        return self.name

class Child(Parent):

    def assign_age(self, age):
        self.age = age

    def show_age(self):
        return self.age


class GrandChild(Child):

    def assign_gender(self, gender):
        self.gender = gender

    def show_gender(self):
        return self.gender

grandChild = GrandChild()
grandChild.assign_name("Raj H")
grandChild.assign_age(20)
grandChild.assign_gender("M")

print(grandChild.show_name())
print(grandChild.show_age())
print(grandChild.show_gender())