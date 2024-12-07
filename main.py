import requests 
import logging
import sys
from PyPDF2 import PdfReader

ARTICLETEXT = ""
baseurl = "https://g9557wysl2.execute-api.us-east-2.amazonaws.com/prod"

def process():
    try:
        print("Enter PDF filename: ")
        localfile = input()
        reader = PdfReader(localfile)
        text = ""
        for page in reader.pages:
            text+=page.extract_text()
        
        text = " ".join(text.splitlines())

        print("Finished uploading the article")
        return text

    except Exception as e:
        print("We ran into this error while processing: ", e)

def sentimentAnalysis(text):
    try:
        if len(text) == 0 :
            print("no article has been uploaded yet")
            return 
        url = baseurl + "/sentiment"
        dataPayload = text
        res = requests.post(url, json=dataPayload)

        if res.status_code== 200:
            return res.json()['Sentiment']
        else:
            print("We ran into an issue")
        return "There was an error with the analysis"
    except Exception as e:
        print("We ran into this error in sentiment analysis: ", e)
    
def summarize(text):
    try:
        url = baseurl + "/summarize"
        dataPayload = {
            "body": text
        }
        res = requests.post(url, json=dataPayload)
        if res.status_code == 200:
            print('status code was 200 for summarization')
            return res.json()['body']
        else:
            print("We ran into an issue in the summarization")
        return "There was an error with the summarization"
    except Exception as e:
        print("We ran into this error during summarization: ", e)


def translate(text):
    try:
        url = baseurl + "/translate"
        language = input("Enter the language you want to translate to: ")
        url = url + "/" + language
        dataPayload = text
        res = requests.post(url, json=dataPayload)
        print("this is the json object: "   , res.json())
        if res.status_code == 200:
            return res.json()['TranslatedText']
        else:
            print("We ran into an in the translation")
        return "There was an error with the translation"
    except Exception as e:
        print("We ran into this error during translation: ", e)


def prompt():
    try:
        print()
        print(">> Enter a command:")
        print("   0 => Exit")
        print("   1 => Upload article")
        print("   2 => Sentiment analysis")
        print("   3 => Summarize article")
        print("   4 => Translate article")

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

    cmd = prompt()

    while cmd != 0:
        if cmd == 1:
            ARTICLETEXT = process()
        elif cmd == 2:
            analysis = sentimentAnalysis(ARTICLETEXT)
            if not analysis:
                analysis = ""
            print("Here is our analysis\n***********************************************\n" + analysis + "\n***********************************************")

        elif cmd == 3:
            summary = summarize(ARTICLETEXT)
            if not summary:
                summary = ""
            print("Here is our summary\n***********************************************\n" + summary + "\n***********************************************")
        elif cmd == 4:
            translation = translate(ARTICLETEXT)
            if not translation:
                translation = ""
            print("Here is our translation\n***********************************************\n" + translation + "\n***********************************************")
        else:
            print("** Unknown command, try again...")
        cmd = prompt()

except Exception as e:
    logging.error("ERROR MAIN() FAILED")
    logging.error(e)
    sys.exit(0)