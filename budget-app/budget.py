class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.total = 0
        self.spents = 0

    def get_balance(self):
        return self.total

    def check_funds(self, amount):
        self.amount = amount
        balance = self.get_balance()

        if self.amount > balance:
            return False
        else:
            return True

    def deposit(self, amount, description=""):
        self.amount = amount
        self.description = description
        
        # append to ledger
        self.ledger.append({"amount": self.amount,
            "description": self.description,
            })

        # add amount in total
        self.total += self.amount

    def withdraw(self, amount, description=""):
        self.amount = amount
        self.description = description

        balance = self.get_balance()

        if self.check_funds(self.amount):
            # append to ledger
            self.ledger.append({"amount": self.amount *-1,
                "description": self.description,
                })

            # deduct amount from total
            self.total -= self.amount
            self.spents += self.amount
            return True
        else:
            return False


    def transfer(self, amount, dest):
        self.amount = amount
        self.description = f"Transfer to {dest.name}"

        if self.check_funds(self.amount):
            # add withdrawal
            self.withdraw(self.amount, self.description)

            # add deposit
            description = f"Transfer from {self.name}"
            dest.deposit(self.amount, description)

            return True
        else:
            return False

    def __str__(self):
        line = ""

        # headder
        title = f"{self.name.title().center(30, '*')}\n"
        line += title

        # items
        ledger = self.ledger
        for item in ledger:
            description = item["description"][:23]
            width = len(description)
            amount = item["amount"]
            rjust_width = 30-width
            line += f"{description}" + f"{amount:.2f}"[:7].rjust(rjust_width) + "\n"

        # total
        total = self.get_balance()
        line += f"Total: {total:.2f}"

        return line

def create_spend_chart(categories):

    n_categories = len(categories)
    width = 4 + n_categories*3

    # make empty plot
    line = ""
    line += "Percentage spent by category\n"
    for y_point in reversed(range(0,110,10)):
        spaces = " "*n_categories*3 + " "
        line += f"{y_point}|".rjust(4) + f"{spaces}" + "\n"

    # dashes
    dashes = "-"*(n_categories*3) + "-"
    line += dashes.rjust(width+1) + "\n"

    # names
    new_labs = [category.name.title() for category in categories]
    max_len = max(map(len,new_labs))
    for i, category in enumerate(new_labs):
        if len(category) != max_len:
           new_labs[i] = category + " " * (max_len - len(category))
    chars = [[c for c in category] for category in new_labs]
    zlabs = list(zip(*chars))
    for lab in zlabs:
        line += " " *  3
        for r in range(n_categories):
            if r != n_categories-1:
                line += " "*2 + f"{lab[r]}"
            else:
                line += " "*2 + f"{lab[r]}" + " "*2 + "\n"

    line = line.rstrip()
    line += " " * 2

    # percentage spent is spent for each category over
    # total spents across all categories plotted
    spents = [category.spents for category in categories]
    total_spents = sum(spents)
    perc_spent = [(spent / total_spents * 100) // 10 * 10 for spent in spents]

    # find indexes in line
    # index of first label
    first_letter = new_labs[0][0]
    line_len = len(line.split("\n")[1]) + 1 # +1 to add the \n back
    first_letter_index = line.find(first_letter)
    
    # indices of the remaining labels
    label_indices = [first_letter_index + 3*r for r in range(n_categories)]

    # indices of points above the labels
    # substitute
    for a, amt in enumerate(perc_spent):
        for i, increment in enumerate(range(0,int(amt)+10,10)):
            index = label_indices[a] - line_len * (2 + i)
            line = line[:index] + "o" + line[index+1:]
    
    return(line)
