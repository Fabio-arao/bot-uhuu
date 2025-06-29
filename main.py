from bot.settings import *
from bot.bot import Ticket360
from tools.tools import Setup
from datetime import datetime
import os
import undetected_chromedriver as uc



class Application():
    def __init__(self, path): 
        self.path = path   
        self.steps = gen_steps()  
        self.start, self.max = TRYS.get('start'), TRYS.get('max')    
        self.start_time = datetime.today() 
        self.run_app()        

    def setup_bot(self):   
        self.setup = Setup(self.path)       
        self.webdriver = uc.Chrome()
        self.bot = Ticket360(self.webdriver, self.path, INFOS_BOT['url'])
     
    def run_app(self):
        while self.start <= self.max:    
            try:
                print_log(f'INI BOT - {self.start}ª Tentativa')
                self.setup_bot()           
                for step, done in self.steps.items():
                    if not done:           
                        self.bot.make_collect(step)                        
                        self.steps[step] = True
                        
                self.finish_bot()
                break
            except Exception as err:      
                print(err)         
                self.webdriver.quit()                                            
                self.start += 1 
                self.bot.exceptions(self.start, self.max, err)  
           
    def finish_bot(self):
        self.bot.send_email(True)
             
 
 
if __name__ == "__main__":
    path = os.getcwd() + '\\sheets'      
    setup_log('\\'.join(path.split('\\')[:-1]))
    Application(path) 
    