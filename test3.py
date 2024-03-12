class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def hasage(self):
        if hasattr(self, 'age'):
            print("aaa", end='\n')
            print(getattr(self, 'age'))
            return True
        else:
            return False

    def setage(self, age):
        setattr(self, 'age', age)

    def getage(self):
        return getattr(self, 'age')

    def printclass(self):
        print("{0}'s salary is {1}, and his age is {2}".format(self.name, self.salary, self.getage()))


def main():
    name = input()
    salary = int(input())
    e = Employee(name, salary)
    if e.hasage():
        print(e.hasage, end='\n')
        e.printclass()
    else:
        age = int(input())
        print(e.hasage(), end='\n')
        e.setage(age)
        e.printclass()


if __name__ == "__main__":
    main()