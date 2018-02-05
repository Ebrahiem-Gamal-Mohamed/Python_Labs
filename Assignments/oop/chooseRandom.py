
#Write a program that choose a random website name from list and open it in your browser :
from random import choice
import webbrowser

webSits = [ "http://google.com", 
            "http://facebook.com", 
            "http://youtube.com", 
            "http://linkedin.com", 
            "http://github.com"]

webbrowser.open_new_tab(choice(webSits))
