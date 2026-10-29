class Program:
    def __init__(self, code, color, seconds):
        self.code = code
        self.color = color
        self.seconds = seconds

    def ans(self):
        print("code :", self.code)
        print("color :", self.color)
        print("second :", self.seconds)

unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

# Please write your code here.

program = Program(unlock_code, wire_color, seconds)
program.ans()