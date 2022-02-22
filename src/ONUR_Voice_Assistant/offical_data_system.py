import webbrowser

from lcg import LCG


def how_are_you():
    answers = [
        """I'am fine""",
        "Not bad",
    ]
    return LCG.choice(answers)

def open_facebook():
    return """I'am opening the facebok"""
    webbrowser.open('https://facebook.com')

def open_youtube():
    return """I'am opening the youtube"""
    webbrowser.open('https://youtube.com')


OFFICAL_DATA = [
    [
        [
            "how are you",
        ], 
        how_are_you
    ],  
    [
        [
            "open facebook",
            "open the facebook",
        ], 
        open_facebook
    ], 
    [
        [
            "open youtube",
            "open the youtube",
        ], 
        open_youtube
    ], 
]