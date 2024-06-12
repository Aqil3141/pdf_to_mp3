import win32com.client 
#import pdfplumber
#
#def pdf_to_text(pdf_path):
#    text = ""
#    with pdfplumber.open(pdf_path) as pdf:
#        for page in pdf.pages:
#            text += page.extract_text() + "\n"
#    return text
#
## Example usage
#pdf_path = "Kafka.pdf"
#text = pdf_to_text(pdf_path)
#
## Save the text to a file
#with open("output.txt", "w", encoding="utf-8") as text_file:
#    text_file.write(text)

speaker = win32com.client.Dispatch("SAPI.SpVoice")
voices = speaker.GetVoices()
speaker.Voice = voices.Item(2) 
text = open("output.txt", "r")

while 1:
    s = text.readline() 
    speaker.Speak(s) 