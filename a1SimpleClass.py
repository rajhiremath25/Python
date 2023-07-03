class Phone:        #generaly class names have first letter capital
    def make_calls(self):
        print("making calls")

    def play_games(self):
        print("playing games")

    def setColor(self, color):
        self.color = color

    def setCost(self, cost):
        self.cost = cost

    def showColor(self):
        return self.color

    def showCost(self):
        return self.cost

phone = Phone()
phone.play_games()
phone.make_calls()

phone.setColor("red")
phone.setCost(100)

print(phone.showColor())
print(phone.showCost())
