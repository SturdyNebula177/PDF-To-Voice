import pyttsx3
import PyPDF2
book = open('name.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
#speaker.say('Hey I am reading')
page = pdfReader.getPage(0)
text = page.extractText()
speaker.say(text)
speaker.runAndWait()
