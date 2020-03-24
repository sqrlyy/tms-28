class Math:
    def __init__(self, first_number, second_number):
        self.first_number = first_number
        self.second_number = second_number

    def __str__(self):
        return f'First number: {self.first_number}, second number: {self.second_number}'

    def sum(self):
        return self.first_number + self.second_number

    def sub(self):
        return self.first_number - self.second_number

    def mul(self):
        return self.first_number * self.second_number

    def div(self):
        return self.first_number / self.second_number
