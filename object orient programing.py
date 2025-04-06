'''class person:
    name="harry"
    occupation="software developer"
    networth=10
    def info(self):
        print(f"{self.name} is a {self.occupation}.")
a=person()
b=person()
a.name="shubham"
a.occupation="accountant"

b.name="shaurya"
b.occupation="student"
#print(a.name,a.occupation)
a.info()
b.info()'''


class person:
    def __init__(self,name,occ):
        print(f"{name} is a {occ}")
        self.name=name
        self.occ=occ
a=person("Harry","Developer")
b=person("divya","HR")
