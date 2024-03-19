import React, { useState } from 'react';
import './App.css';
import axios from 'axios';

function App() {
  const [textInput, setTextInput] = useState('');
  const [embeddings, setEmbeddings] = useState(null);

  const handleInputChange = (e) => {
    setTextInput(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://127.0.0.1:5000/embedding', { text: textInput });
      setEmbeddings(response.data);
    } catch (error) {
      console.error('There was an error!', error);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h2>Get Text Embeddings</h2>
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            value={textInput}
            onChange={handleInputChange}
            placeholder="Enter text"
          />
          <button type="submit">Submit</button>
        </form>
        {embeddings && (
          <div>
            <h3>Embedding:</h3>
            <pre>{JSON.stringify(embeddings, null, 2)}</pre>
          </div>
        )}
      </header>
    </div>
  );
}

export default App;
