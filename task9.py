class FSM:
    def __init__(self):
        self.A = "A"
        self.B = "B"
        self.C = "C"
        self.D = "D"
        self.E = "E"
        self.F = "F"

        self.start = self.A
        self.current_state = self.start

    def smash(self):
        if self.current_state == self.A:
            self.current_state = self.B
            return 0
        elif self.current_state == self.B:
            self.current_state = self.C
            return 2
        elif self.current_state == self.C:
            self.current_state = self.D
            return 4
        elif self.current_state == self.D:
            self.current_state = self.E
            return 5
        elif self.current_state == self.E:
            self.current_state = self.F
            return 6
        elif self.current_state == self.F:
            self.current_state = self.B
            return 8
        else:
            raise KeyError

    def rock(self):
        if self.current_state == self.A:
            self.current_state = self.A
            return 1
        elif self.current_state == self.B:
            self.current_state = self.E
            return 3
        elif self.current_state == self.F:
            self.current_state = self.C
            return 7
        else:
            raise KeyError


def main():
    evaluator = FSM()

    return evaluator
  
o = main()
print(o.rock()) # 1
print(o.smash()) # 0
print(o.smash()) # 2
