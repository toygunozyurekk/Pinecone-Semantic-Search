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
    data = request.json
    user_input = data.get('text')

    if not user_input:
        return jsonify({"error": "No text provided"}), 400

    try:
        # Call the OpenAI API with the user's input text
        res = client.embeddings.create(
            input=[user_input],
            model=MODEL
        )
        # Convert the response to a dictionary (assuming `res` has a `.to_dict()` method)
        res_dict = res.to_dict() if hasattr(res, 'to_dict') else res.json()
        # Return the API response
        return jsonify(res_dict)
    except Exception as e:
        # If an error occurs, return the error message
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)






