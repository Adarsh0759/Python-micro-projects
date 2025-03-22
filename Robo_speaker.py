import pyttsx3

engine = pyttsx3.init()

if __name__ == "__main__":
    print("Welcome to RoboSpeaker created by Adarsh")

    while True:
        x = input("Enter what you want me to say: ")
        if x.lower() == "q": 
            engine.say("'Bye Bye friend'") 
            engine.runAndWait()
            break
        engine.say(x)
        engine.runAndWait()
