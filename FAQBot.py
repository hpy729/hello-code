import time
import random
from simpleeval import simple_eval
from termcolor import colored

class Bot:  #定义一个执行run的父类
    wait = 1
    
    def __init__(self,runtype='once'):  #初始化父类，初始化runtype为once
        self.runtype=runtype
        self.q = ''
        self.a = ''

    def _think(self, s):    #根据用户输入来计算程序回应的内容
        return s

    def _format(self, s):   #答案color上蓝色字
        return colored(s,'blue')

    def _run_once(self):    #假如runtype='once'，用于仅运行一次的bot
        time.sleep(Bot.wait)
        print(self._format(self.q))
        self.a = input()
        time.sleep(Bot.wait)
        print(self._format(self._think(self.a)))

    def _run_looped(self):  #假如runtype='looped'，用于要运行多次的bot
        time.sleep(Bot.wait)
        print(self._format(self.q))
        while True:
            self.a = input()
            if self.a.lower() in ['q', 'x', 'quit', 'exit']:
                break
            time.sleep(Bot.wait)
            print(self._format(self._think(self.a)))
            
    def run(self):  #run主程序，
        if self.runtype == 'once':
            self._run_once()
        elif self.runtype == 'looped':
            self._run_looped()

class HelloBot(Bot):    #问名字的bot
    def __init__(self, runtype='once'):
        super().__init__(runtype)
        self.q = "Hi, what's your name?"
        
    def _think(self, s):
        return f"hello {s}"

class GreetingBot(Bot): #问候bot
    def __init__(self, runtype='once'):
        super().__init__(runtype)
        self.q = "What's up?"
        
    def _think(self, s):
        if 'good' in s.lower() or 'ok' in s.lower() or 'fine' in s.lower():
            return "I'm feeling good too."
        else:
            return "Sorry to hear that,my friend."

class FavoriteColorBot(Bot):    #问喜欢的颜色bot
    def __init__(self, runtype='once'):
        super().__init__(runtype)
        self.q = "What's your favorite color?"
        
    def _think(self, s):
        colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']
        return f"You like {s.lower()}? My favorite color is {random.choice(colors)}"

class CalcBot(Bot): #计算器bot
    def __init__(self, runtype='once'):
        super().__init__(runtype)
        self.q = "Through recent upgrade I can do calculation now. Input some arithmetic expression to try. Input 'q' 'x' 'quit' or 'exit' to quit:"
    
    def _think(self, s):
        result = simple_eval(s)
        return f"Result={result}"


class FAQBot:   #对话系统的主类定义，即主流程
    def __init__(self, wait=1):
        Bot.wait = wait
        self.bots = []
        
    def add(self, bot): #定义add()方法往系统中加入bot，
        self.bots.append(bot)   #使用列表的append()方法实现加入；

    def _prompt(self, s):
        print(s)
        print()

    def framerun(self):
        self._prompt("This is Garfield dialog system. Let's talk.")
        for bot in self.bots:
            bot.run()

faqbot = FAQBot(1)

faqbot.add(HelloBot())
faqbot.add(GreetingBot())
faqbot.add(FavoriteColorBot())
faqbot.add(CalcBot('looped'))

faqbot.framerun()