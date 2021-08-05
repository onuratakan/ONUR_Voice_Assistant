import webbrowser

from say_me_something import say
from ask_me_something import ask


from selenium import webdriver




def open_on_google():
    say("What should i look for")
    webbrowser.open('https://www.google.com/search?q=' + ask())


def search_on_google():
    say("What should i look for")
    driver = webdriver.Chrome()
    driver.get('https://www.google.com/search?q=' + ask())
    search_result = driver.find_element_by_xpath('//*[@id="rhs_block"]/div/div[1]/div/div[1]/div[2]/div[2]/div/div[1]/div/div/div/div/span[1]').text
    say(search_result) 


def open_the_facebook():
    say("""I'am opening the facebok""")
    webbrowser.open('https://facebook.com')

def open_the_youtube():
    say("""I'am opening the youtube""")
    webbrowser.open('https://youtube.com')


OFFICAL_DATA = [
    ["open on google", "open_on_google()"],
    ["search on google", "search_on_google()"],
    ["open the facebook", "open_the_facebook()"],
    ["open the youtube", "open_the_youtube()"]
]