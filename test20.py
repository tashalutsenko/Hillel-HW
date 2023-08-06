class String(str):

    def __add__(self, other):
        return String(super().__add__(str(other)))

    def __sub__(self, other):
        return String(self.replace(str(other), "", 1))


print(String('New') + String(890))