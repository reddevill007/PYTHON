# imporing random module which genrates random number
import random
import pyttsx3
import speech_recognition as sr # module to recoganize voice


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening........")
        # speak("How can i help you")
        # speak("Listning")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("recognizing....")
        # speak("recognizing your query")
        query=r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Could'nt recoganise your voice, Speak again....")
        speak("Could not recoganise your voice")
        speak("Speak again")
        return "None"
    return query

# defining a function to check the result of the game

def game(comp, you):
    if comp == you:  # when you and computer choose same choices game returns None i.e DRAW
        return None
    elif comp == 'rock':
        if you == 'scissors':  # you choose secissors computer choosed rock function returns false i.e LOST
            return False
        elif you == 'paper':  # you choose paper computer choosed rock function returns false i.e WIN
            return True
    elif comp == 'paper':
        if you == 'rock':  # you choose secissors computer choosed paper function returns false i.e LOST
            return False
        elif you == 'scissors':  # you choose rock computer choosed paper function returns false i.e WIN
            return True
    elif comp == 'scissors':
        if you == 'paper':  # you choose rock computer choosed secissors function returns false i.e LOST
            return False
        elif you == 'rock':  # you choose paper computer choosed secissors function returns false i.e WIN
            return True

def result():
    print(f"You choosed '{you}' and computer choosed '{comp}'")
    speak(f"You choosed '{you}'")
    speak(f" and computer choosed '{comp}'")

# WELCOME MESSAGE

print(" \t\t\t\t\t\t**********************************************************\t\t\t")
print(" \t\t\t\t\t\t\t WELCOME TO 'ROCK, PAPER OR SCISSORS' GAME")
print(" \t\t\t\t\t\t**********************************************************\t\t\t\n")
speak("WELCOME TO 'ROCK, PAPER OR SCISSORS' GAME")
while True:
    
    # Creating a variable which chooses random number between 1 and 9 using random function
    randno = random.randint(1, 9)

    # If random number is between 1 and 3 computer choice will be 'r' i.e rock
    if randno >= 1 and randno <= 3:
        comp = 'rock'

    # If random number is between 4 and 6 computer choice will be 'p' i.e paper
    elif randno >= 4 and randno <= 6:
        comp = 'paper'

    # If random number is between 7 and 9  computer choice will be 's' i.e secisors
    elif randno >= 7 and randno <= 9:
        comp = 'scissors'

    # Taking input from the user in the form of string
    print("Your Turn: Speak your choices from")
    print("1> Rock")
    print("2> Paper")
    print("3> Scissors")
    print("4> Stop")
    speak("please speak your choice")
    you = takeCommand().lower()
    print(" \t\t\t\t\t\t****************************************************\t\t\t")

    # Output player enters wrong keyword

    if 'stop' in you:
        break

    elif you != 'rock' and you != 'paper' and you != 'scissors':
        print(" \t\t\t\t\t\t****************************************************\t\t\t")
        speak("Invalid choice.........")
        print("Invalid choice.........")
        print(" \t\t\t\t\t\t****************************************************\t\t\t\n")

    elif 'rock' or 'paper' or 'scissors' in you:
        a=game(comp,you)
        if a == None:
            result()
            print(" \t\t\t\t\t\t****************************************************\t\t\t")
            print("The game is drawn!!!!")
            print(" \t\t\t\t\t\t****************************************************\t\t\t\n")
            speak("The game is drawn!!!!")

        # Output when player looses
        if a == False:
            result()
            print(" \t\t\t\t\t\t****************************************************\t\t\t")
            print("You Lost Please try again !!!!")
            print(" \t\t\t\t\t\t****************************************************\t\t\t\n")
            speak("You Lost Please try again !!!!")

        # Output when player wins
        if a == True:
            result()
            print(" \t\t\t\t\t\t****************************************************\t\t\t")
            print("Congratulations!!!! You won..........")
            print(" \t\t\t\t\t\t****************************************************\t\t\t\n")
            speak("Congratulations!!!! You won..........")


    
