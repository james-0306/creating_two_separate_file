class FileSeparator:
    def __init__(self, input_file, even_file, odd_file):
        self.input_file = input_file
        self.even_file = even_file
        self.odd_file = odd_file

    def process(self):
        with open(self.input_file, "r") as file:
            numbers = file.read().split()

        input_numbers = [int(num) for num in numbers]

        



