import sys
import time
def animated(text):
  for x in text:
   sys.stdout.write(x)
   sys.stdout.flush()
   time.sleep(0.005)
logo = '''
 "\u001b[32m._____       _ _ _     
  / ____|     (_|_) |    
 | (___   __ _ _ _| |__  
  \___ \ / _` | | | '_ \ 
  ____) | (_| | | | |_) |
 |_____/ \__,_| |_|_.__/ 
             _/ |        
            |__/         


'''
line = "------------------"
animated(logo)
animated(line)