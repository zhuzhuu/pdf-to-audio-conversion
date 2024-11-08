import PyPDF2
import pyttsx3

def extract_text_from_pdf(pdf_path):
    # Open PDF File
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""

        for page in reader.pages:
            text += page.extract_text()

    return text


def text_to_speech(text):
    engine = pyttsx3.init()

    # Change voice, rate, and volume
    engine.setProperty('rate', 150)  # Speed of Speech
    engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)

    # Convert text to speech
    engine.say(text)
    engine.runAndWait()


def main():
    pdf_path = r'INSERT FILE PATH'

    text = extract_text_from_pdf(pdf_path)


    # Convert text to speech
    if text:
        print("Starting text to speech conversion....")
        text_to_speech(text)
    else:
        print("No text found in the PDF")


if __name__ == "__main__":
    main()


