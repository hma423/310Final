import requests 
import logging
import sys
from PyPDF2 import PdfReader


def process():
    reader = PdfReader(r"C:\Users\mhenr\Documents\Github\310Final\newsArticle.pdf")
    text =""
    for page in reader.pages:
        text+=page.extract_text()
    
    text = " ".join(text.splitlines())
    return text



def sentimentAnalysis(text):
    pass


def summarize(text):
    pass


def translate(text):
    pass

def prompt():
    try:
        print()
        print(">> Enter a command:")
        print("   0 => end")
        print("   1 => upload article")
        print("   2 => sentiment analysis")
        print("   3 => summarize article")
        print("   4 => translate article")

        cmd = input()

        if cmd == "":
            cmd = -1
        elif not cmd.isnumeric():
            cmd = -1
        else:
            cmd = int(cmd)

        return cmd
    except Exception as e:
        print("An error occured: ", e)



try:
    print("Welcome to our 310 Final Project\n")

    article = process()
    print(article)
    # cmd = prompt()

    # while cmd != 0:
    # #
    #     if cmd == 1:
    #         print("cmd 1!")
    #     elif cmd == 2:
    #         print("cmd 2")
    #     elif cmd == 3:
    #         print("cmd3")
    #     elif cmd == 4:
    #         print("cmd4")
    #     else:
    #         print("** Unknown command, try again...")
    #     cmd = prompt()




    


except Exception as e:
    logging.error("ERROR MAIN() FAILED")
    logging.error(e)
    sys.exit(0)