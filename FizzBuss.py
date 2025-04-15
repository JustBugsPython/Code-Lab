import time
import winsound
from colorama import init, Style, Fore
init()
for i in range (1, 51):
    time.sleep(0.5)
    if i % 3 == 0 and i % 5 == 0:
        print(Fore.MAGENTA + " 💥 FizzBuzz 💥" + Style.RESET_ALL)
        winsound.Beep(800, 300)
    elif i % 3 == 0:
        print("✨ Fizz ✨")
       
        winsound.Beep(600, 300)
    elif i % 5 == 0:
        print("🔊 Buzz 🔊")
       
        winsound.Beep(700, 300)
    else:
        print(f"{i} 🧠")
