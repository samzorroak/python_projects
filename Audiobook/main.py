import pyttsx3
import PyPDF2
from tkinter.filedialog import *

#Open a file dialog to select a PDF file
book = askopenfilename()

# Create a PDF reader object (Initialize it)
pdfreader = PyPDF2.PdfReader(book)

# Get the number of pages in the PDF file
pages = len(pdfreader.pages)

# Create a text-to-speech engine
for num in range(0, pages):
    # Extract text from the current page
    page = pdfreader.pages[num]
    text = page.extract_text()

    # Initialize the text-to-speech engine and read the extracted text aloud
    player = pyttsx3.init()
    player.say(text)
    player.runAndWait()
