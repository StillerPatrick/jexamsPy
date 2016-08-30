import datetime
from urllib.request import urlopen
import webbrowser


now = datetime.datetime.now()
currentMinute = 0  # last successfull request
currentSize = 0

url = "http://feeds.feedburner.com/jExam"
while (True):
    now = datetime.datetime.now()
    if (((now.minute - currentMinute) >= 10) or ((now.minute - currentMinute) < 0)):
        print("New Intervall at " + str(now.hour) + ":" + str(now.minute) + " Uhr")

        html = urlopen(url).read().decode('utf-8')
        length = len(html)
        print(length)
        if (length > currentSize or length < currentSize):
            print("New Content")
            webbrowser.open("https://jexam.inf.tu-dresden.de/de.jexam.web.v4.5/spring/welcome")
            currentSize = length

        now = datetime.datetime.now()
        currentMinute = now.minute
