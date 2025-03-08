#If a bird acts like duck walks like duck. Its a duck..;}

class Pycharm:
    def execute(self):
        print("executing code...")

class VSCode:
    def execute(self):
        print("executing code using VSCode...")


class Laptop:
    def code(self, ide):  #This is called duck typing.. Doesnt matter what is the type of Ide if it have execute method it works.
        ide.execute()




ide = Pycharm()

l1 = Laptop()

l1.code(ide)