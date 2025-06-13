class MultiplicationTable:
    def __init__(self, number, limit):
        self.number = number      # number to generate the table for
        self.limit = limit        # range limit

    def generate_table(self):
        print(f"\nMultiplication Table for {self.number} up to {self.limit}:\n")
        for i in range(1, self.limit + 1):
            print(f"{self.number} x {i} = {self.number * i}")

# ----------- Main Code -----------
if __name__ == "__main__":
    # User input
    try:
        num = int(input("Enter the number you want the table of: "))
        lim = int(input("Enter the range (limit) of the table: "))

        # Create object and generate table
        table = MultiplicationTable(num, lim)
        table.generate_table()
        
    except ValueError:
        print("Please enter valid integers only.")
