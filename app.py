from flask import Flask,request,jsonify
from flask_cors import CORS
import os 
from dotenv import load_dotenv
from openai import OpenAI
from pinecone_datasets import load_dataset

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=OPENAI_API_KEY)

app = Flask(__name__)
CORS(app)

@app.route('/embedding', methods=['POST'])
def embedding(): 
    MODEL = "text-embedding-3-small"

# Prompting the user to enter their texts
# You can use a loop or any method you prefer to collect multiple inputs
    user_input1 = input("Enter the first text: ")


    # Assuming you want to collect these texts in a list
    texts = [user_input1]

    # Now, you use these texts to create embeddings
    res = client.embeddings.create(
        input=texts,
        model=MODEL
    )
    return res

if __name__ == '__main__':
    app.run(debug=True)
# Printing the result





