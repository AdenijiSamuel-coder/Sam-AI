from googlesearch import search
from guess import *
import sys
import boto3
import speech_recognition as sr
import os
from playsound import playsound
import webbrowser
import random
import time

speech = sr.Recognizer()  ## this is the part that receives the sound
baby_mode = {'switch to baby mode':'switch to baby mode','baby mode':'baby mode'}  ## key word to switch to baby mode
greeting_dict = {'sarah':'sarah','alexa':'alexa'}  ## name of the program  
open_launch_dict = {'open':'open','launch':'launch'}##keywords to open applications
greetings_dict = {'hello':'how are you','hey':'hey','how are you doing':'how are you doing'}
google_searches_dict = {'what': 'what', 'why': 'why', 'who': 'who', 'which':'which', 'define':'define', 'when': 'when','the': 'the','state':'state','check':'check','how ':'how'}
social_media_dict = {'internet speed':'https://www.fast.com','facebook':'https://www.facebook.com','football':'https://www.goal.com','youtube':'https://www.youtube.com','anchor':'https://www.aul.edu.ng','bank':'https://www.piggybank.com',}

mp3_baby_response = ['/Users/user/Music/baby response.mp3','/Users/user/Music/baby response2.mp3']## baby response
mp3_thank_you_list = ['/Users/user/Music/zira welcome1.mp3','/Users/user/Music/zira welcome2.mp3']## thank you list
mp3_strugging_list = ['/Users/user/Music/zira_struggling_1.mp3', '/Users/user/Music/zira_struggling_2.mp3']##struggling to hear you list
mp3_listening_problem_list = ['/Users/user/Music/zira listening 1.mp3','/Users/user/Music/zira listening 2.mp3']## the listening problem list list
mp3_greeting_list = ['/Users/user/Music/bingo greeting.mp3','/Users/user/Music/zira greeting.mp3']## the greeting list 
mp3_launch_list = ['/Users/user/Music/ziraopen1.mp3','/Users/user/Music/zira open 2.mp3']## the lunch list
mp3_barking = ['/Users/user/Music/bark1.mp3','/Users/user/Music/bark2.mp3','/Users/user/Music/bark1.mp3']
mp3_response = ['/Users/user/Music/calling 1.mp3','/Users/user/Music/calling2.mp3']
mp3_cat =['/Users/user/Music/cat1.mp3','/Users/user/Music/cat2.mp3']
mp3_baby_song = ['/Users/user/Music/baby song1.mp3']
error_occurrence = 0

##polly = boto3.client('polly', region_name='us-east-1')
##
##def play_sound_from_polly(result):
##    mp3_name = 'output.mp3'
##    obj = polly.synthesize_speech(Text=result, OutputFormat='mp3', VoiceId='joanna')
##    with open(mp3_name,'wb') as file:
##        file.write(obj['AudioStream'].read())
##        file.close()
##    playsound(mp3_name)
##    os.remove(mp3)
##    
##def google_search_result(query):
##    search_result= google.search(query)
##    print(search_result)
##    for result in search_result:
##        print(result.description)
##        play_sound_from_polly(result.description)
##    
##
##google_search_result('what is earth')
##exit()

def shutdown():
    playsound('/Users/user/Music/shutdown.mp3')
    os.system('shutdown -s')

def restart():
    playsound('/Users/user/Music/shutdown.mp3')
    os.system('shutdown -r')

def hibernate():
    playsound('/Users/user/Music/shutdown.mp3')
    os.system('shutdown -h')
    
def cmp213note():
    playsound('/Users/user/Music/cmp 213 note.mp3')
    
def is_valid_google_search(phrase):
    if(google_searches_dict.get(phrase.split(' ')[0]) == phrase.split(' ')[0]):
        return True
    
def play_sound(mp3_list):
    mp3 = random.choice(mp3_list)
    playsound(mp3)


def read_voice_cmd():
    voice_text = ''
    print('listening...')

    global error_occurrence
    
    try:
        with sr.Microphone() as source:
            speech.adjust_for_ambient_noise(source)
            audio = speech.listen(source=source,timeout=5,phrase_time_limit=5)
            voice_text = speech.recognize_google(audio)
    except sr.UnknownValueError:
        
        if error_occurrence == 0:
            play_sound(mp3_listening_problem_list)
            error_occurrence += 1
        elif error_occurrence == 1:
            play_sound(mp3_strugging_list)
            error_occurrence += 1

            
    except sr.RequestError as e:
        print('Network error')
        playsound('/Users/user/Music/bingo network error.mp3')

    except sr.WaitTimeoutError:
        if error_occurrence == 0:
            play_sound(mp3_listening_problem_list)
            error_occurrence += 1
        elif error_occurrence == 1:
            play_sound(mp3_strugging_list)
            error_occurrence += 1
    return voice_text
def game():    
    import random
    import time
    import pyttsx3

    import speech_recognition as sr

    def recognize_speech_from_mic(recognizer, microphone):
        """Transcribe speech from recorded from `microphone`.

        Returns a dictionary with three keys:
        "success": a boolean indicating whether or not the API request was
                   successful
        "error":   `None` if no error occured, otherwise a string containing
                   an error message if the API could not be reached or
                   speech was unrecognizable
        "transcription": `None` if speech could not be transcribed,
                   otherwise a string containing the transcribed text
        """
        # check that recognizer and microphone arguments are appropriate type
        if not isinstance(recognizer, sr.Recognizer):
            raise TypeError("`recognizer` must be `Recognizer` instance")

        if not isinstance(microphone, sr.Microphone):
            raise TypeError("`microphone` must be `Microphone` instance")

        # adjust the recognizer sensitivity to ambient noise and record audio
        # from the microphone
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        # set up the response object
        response = {
            "success": True,
            "error": None,
            "transcription": None
        }

        # try recognizing the speech in the recording
        # if a RequestError or UnknownValueError exception is caught,
        #     update the response object accordingly
        try:
            response["transcription"] = recognizer.recognize_google(audio)
        except sr.RequestError:
            # API was unreachable or unresponsive
            response["success"] = False
            response["error"] = "API unavailable"
        except sr.UnknownValueError:
            # speech was unintelligible
            response["error"] = "Unable to recognize speech"

        return response


    if __name__ == "__main__":
        # set the list of words, maxnumber of guesses, and prompt limit
        WORDS = ["apple", "banana", "grape", "orange", "mango", "lemon","tomato","pea"]
        NUM_GUESSES = 3
        PROMPT_LIMIT = 5

        # create recognizer and mic instances
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()

        # get a random word from the list
        word = random.choice(WORDS)

        # format the instructions string
        instructions = (
            "I'm thinking of one of these words:\n"
            "{words}\n"
            "You have {n} tries to guess which one.\n"
        ).format(words=', '.join(WORDS), n=NUM_GUESSES)

        # show instructions and wait 3 seconds before starting the game
        print(instructions)
        time.sleep(3)

        for i in range(NUM_GUESSES):
            # get the guess from the user
            # if a transcription is returned, break out of the loop and
            #     continue
            # if no transcription returned and API request failed, break
            #     loop and continue
            # if API request succeeded but no transcription was returned,
            #     re-prompt the user to say their guess again. Do this up
            #     to PROMPT_LIMIT times
            for j in range(PROMPT_LIMIT):
                print('Guess {}. Speak!'.format(i+1))
                guess = recognize_speech_from_mic(recognizer, microphone)
                if guess["transcription"]:
                    break
                if not guess["success"]:
                    break
                print("I didn't catch that. What did you say?\n")

            # if there was an error, stop the game
            if guess["error"]:
                print("ERROR: {}".format(guess["error"]))
                break

            # show the user the transcription
            print("You said: {}".format(guess["transcription"]))

            # determine if guess is correct and if any attempts remain
            guess_is_correct = guess["transcription"].lower() == word.lower()
            user_has_more_attempts = i < NUM_GUESSES - 1

            # determine if the user has won the game
            # if not, repeat the loop if user has more attempts
            # if no attempts left, the user loses the game
            if guess_is_correct:
                playsound('/Users/ADENIJI SAMUEL/Music/correct.mp3')
                print("Correct! You win!".format(word))
                break
            elif user_has_more_attempts:
                playsound('/Users/user/Music/incorrect.mp3')
                print("Incorrect. Try again.\n")
            else:
                print("Sorry, you lose!\nI was thinking of '{}'.".format(word))
                break


def is_valid_note(greeting_dict,voice_note):
    for key, value in greeting_dict.items():
        #'Hello zira'
        try:
            if value == voice_note.split(' ')[0]:
                return True
                break
            if key == voice_note.split(' ')[1]:
                return True
                break 
        except IndexError:
            pass

    return False


if __name__ == '__main__':

    playsound('/Users/user/Music/bingo my ai.mp3')

    while True:

        voice_note = read_voice_cmd().lower()
        print('user input  >>   {}'.format(voice_note))

        if is_valid_note(greeting_dict,voice_note):
            print('in greeting...')
            play_sound(mp3_greeting_list)
            continue
        elif is_valid_note(open_launch_dict,voice_note):
            print('in open...')
            play_sound(mp3_launch_list)
            #__launch applications__
            if (is_valid_note(social_media_dict,voice_note)):
                key = voice_note.split(' ')[1]
                webbrowser.open(social_media_dict.get(key))
            else:
                os.system('explorer C:\\"{}"'.format(voice_note.replace('open ', '').replace('launch ', '')))
            continue
        elif is_valid_google_search(voice_note):
            print('in google search...')
            webbrowser.open('https://www.google.co.in/search?q={}'.format(voice_note))
            playsound('/Users/user/Music/zira google search.mp3')
            continue
        elif is_valid_note(greeting_dict,voice_note):
            print('in calling...')
            playsound(mp3_response)
            continue
        elif 'baby mode' in voice_note:
            play_sound(mp3_baby_response)
            print('in baby mode...')
            play_sound(mp3_baby_song)
            continue
        elif 'bark like a dog' in voice_note:
            play_sound(mp3_barking)
            continue
        elif 'sound like a cat' in voice_note:
            play_sound(mp3_cat)
            continue
        elif 'play game' in voice_note:
            playsound('/Users/user/Music/game welcome.mp3')
            game()
            continue
        elif 'thank you' in voice_note:
            play_sound(mp3_thank_you_list)
            continue
        elif 'read cmp' in voice_note:
            playsound('/Users/user/Music/confirmation.mp3')
            cmp213note()
            continue
        elif 'goodbye' in voice_note:
            playsound('/Users/user/Music/bye.mp3')
            break
        elif 'shutdown' in voice_note:
            shutdown()
            break
        elif 'restart' in voice_note:
            restart()
            break
        elif 'hibernate' in voice_note:
            hibernate()
            break
