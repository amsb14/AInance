import cohere
import os
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

# Access the value of an environment variable
api_key = os.getenv("API_KEY")

co = cohere.Client(api_key) # This is your trial API key

def generate_prompt(prompt):
    response = co.generate(
      model='command',
      prompt=f'{prompt}\n',
      max_tokens=300,
      temperature=0.8,
      k=0,
      stop_sequences=[],
      return_likelihoods='NONE')
    return(response.generations[0].text)
    
