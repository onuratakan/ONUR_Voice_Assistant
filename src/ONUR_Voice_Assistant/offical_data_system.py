import webbrowser

from say_me_something import say
from ask_me_something import ask

from lcg import LCG


def how_are_you():
    answers = [
        """I'am fine""",
        "Not bad",
    ]
    say(LCG.choice(answers))

def open_on_google():
    say("What should i look for")
    webbrowser.open('https://www.google.com/search?q=' + ask())

def open_facebook():
    say("""I'am opening the facebok""")
    webbrowser.open('https://facebook.com')

def open_youtube():
    say("""I'am opening the youtube""")
    webbrowser.open('https://youtube.com')


OFFICAL_DATA = [
    [
        [
            "how are you",
        ], 
        "how_are_you()"
    ],
    [
        [
            "open google",
            "open search engine",
        ], 
        "open_on_google()"
    ],   
    [
        [
            "open facebook",
            "open the facebook",
        ], 
        "open_facebook()"
    ], 
    [
        [
            "open youtube",
            "open the youtube",
        ], 
        "open_youtube()"
    ], 
]