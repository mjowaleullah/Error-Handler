import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api = os.getenv("GEMINI_API_KEY")
model = os.getenv("GEMINI_API_MODEL")

client = genai.Client(api_key=api)


def bug_explatation(image):

    prompt = """Summerize the error picture and analysis this Error and Expain the reason for Error. Otherwise, return a message that type "This Picture not for programming Error". Make sure to add necessary markdown to output. """

    response = client.models.generate_content(
        model= model,
        contents=[image, prompt]
    )

    return response.text

def debug(image, solution):
    prompt = f"Summerize the error picture based on {solution}. Make sure to add necessary markdown to output. "

    response = client.models.generate_content(
        model=model,
        contents=[image, prompt]
    )
    return response.text
