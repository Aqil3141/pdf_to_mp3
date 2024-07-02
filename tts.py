import pdfplumber
import edge_tts
import asyncio


#CONVERTING PDF TO TEXT
def pdf_to_text(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + " "
    return text

def remove_blank_sentences(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Remove blank lines
    non_blank_lines = [line for line in lines if line.strip()]

    with open(file_path, 'w') as file:
        file.writelines(non_blank_lines)


# Example usage
pdf_path = "audio.pdf"
text = pdf_to_text(pdf_path)

# Save the text to a file
with open("output.txt", "w", encoding="utf-8") as text_file:
    text_file.write(text)


remove_blank_sentences('output.txt')

async def text_to_speech(text, output_file):
    communicate = edge_tts.Communicate(text, voice='en-US-AvaNeural')
    #Change "voice" variable. Try "edge-tts --list-voices" on cmd for voices
    await communicate.save(output_file)
    # Synthesize speech and save it to an MP3 file

# Function to read the content of a text file
def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Define the file paths
text_file = "output.txt"  # Path to the text file
output_file = "output.mp3"  # Path to the output MP3 file

# Read the text from the file
text = read_text_file(text_file)

# Run the TTS conversion
asyncio.run(text_to_speech(text, output_file))

#Need to add threading (quite slow for big files)