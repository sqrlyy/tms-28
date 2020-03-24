class ChoiceException(Exception):
    choice = [1, 2, 3, 4, 5, 6]

    def __init__(self, message='AAA'):
        super().__init__(message)

    # def __str__(self):
    #     if not self.__value.isgigit() and self.__value not in self.choice:
    #         return 'Enter 1-6!'
