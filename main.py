import requests 
import logging
import sys
from PyPDF2 import PdfReader

ARTICLETEXT=""
baseurl = "https://g9557wysl2.execute-api.us-east-2.amazonaws.com/prod"
def process():
    try:
        print("Enter Pdf filename")
        localfile = input()
        reader = PdfReader(localfile)
        text =""
        for page in reader.pages:
            text+=page.extract_text()
        
        text = " ".join(text.splitlines())

        print("finished uploading the article")
        return text

    except Exception as e:
        print("ran into this error while processing: ", e)






def sentimentAnalysis(text):
    try:
        if len(ARTICLETEXT) ==0 :
            print("no article has been updated yet")
            return 
        url = baseurl + "/sentiment"
        dataPayload = ARTICLETEXT
        res = requests.post(url, json=dataPayload)

        if res.status_code== 200:
            return res.json()['Sentiment']
        else:
            print("we ran into an issue")
        return "there was an error with the analysis"
    except Exception as e:
        print("ran into this error in sentiment analysis: ", e)
    



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

    cmd = prompt()

    while cmd != 0:
        if cmd == 1:
            ARTICLETEXT = process()
        elif cmd == 2:
            analysis = sentimentAnalysis(ARTICLETEXT)
            if not analysis:
                analysis = ""
            print("here is our analysis\n***********************************************\n" + analysis + "\n***********************************************")

        elif cmd == 3:
            print("cmd3")
        elif cmd == 4:
            print("cmd4")
        else:
            print("** Unknown command, try again...")
        cmd = prompt()




    


except Exception as e:
    logging.error("ERROR MAIN() FAILED")
    logging.error(e)
    sys.exit(0)