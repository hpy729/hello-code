from FAQBot import *

class nFAQBot:
    
    def __init__(self):
        self.bots = []
        
    def add(self, bot):
        self.bots.append(bot)

    def run(self):
        print("Welcome to Guitarism dialog system. Let\'s Talk now.")
        print()
        for bot in self.bots:
            bot.run()

if __name__ == '__main__':
    nfaqbot = nFAQBot()
    nfaqbot.add(HelloBot())
    nfaqbot.add(GreetingBot())
    nfaqbot.add(FavoriteColorBot())
    nfaqbot.add(CalcBot('looped'))
    nfaqbot.run()