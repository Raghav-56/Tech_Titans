import React, { useState } from 'react';
import './App.css';
import Center from './components/Center'; // Import the center section
import Navbar from './components/Navbar'; // Your existing Navbar component
import axios from 'axios';
import Footer from './Footer';

function App() {
  const [pdfFile, setPdfFile] = useState(null);
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);

  // Handle file selection and ensure only PDF files are allowed
  const handleFileChange = (e) => {
    const file = e.target.files[0];
    if (file && file.type === 'application/pdf') {
      setPdfFile(file);
    } else {
      alert('Please upload a valid PDF file.');
    }
  };

  // Handle file upload
  const handleUpload = async () => {
    if (!pdfFile) {
      alert('Please select a PDF file to upload.');
      return;
    }

    const formData = new FormData();
    formData.append('pdf', pdfFile);

    try {
      setLoading(true);
      const response = await axios.post('http://localhost:5000/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      alert('PDF uploaded and embeddings generated successfully.');
    } catch (error) {
      console.error('Error uploading PDF:', error);
      // Show error message with specific details
      alert(`Error uploading PDF: ${error.response?.data?.message || error.message}`);
    } finally {
      setLoading(false);
    }
  };

  // Handle query submission
  const handleQuery = async () => {
    if (!query) {
      alert('Please enter a query.');
      return;
    }

    try {
      setLoading(true);
      const response = await axios.post('http://localhost:5000/query', { query });
      setResults(response.data.results);  // Assume backend returns query results
    } catch (error) {
      console.error('Error querying PDF data:', error);
      alert('Error querying the document.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
  <div>
  <Navbar />
    <div/>
    <div className="App">
      {/* Navbar */}
      {/* Center Section */}
      {/* <Center /> */}
      <div className="center">

      
      {/* Upload Section Below the Title */}
      <div className="upload-section">
        <div>
          <h2>Upload PDF</h2>
          <input type="file" accept="application/pdf" onChange={handleFileChange} />
          <button onClick={handleUpload} disabled={loading}>
            {loading ? 'Uploading...' : 'Upload PDF'}
          </button>
        </div>
      </div>

      {/* Query Input Section */}
      <div className="query">
        <h2>Ask a Question</h2>
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Enter your query..."
        />
        <button onClick={handleQuery} disabled={loading}>
          {loading ? 'Querying...' : 'Submit Query'}
        </button>
      </div>
      
      {/* Results Display Section */}
      {results.length > 0 && (
        <div>
          <h2>Results</h2>
          <ul>
            {results.map((result, index) => (
              <li key={index}>
                <p>{result.text}</p>
                <small>Citation: {result.citation}</small>
              </li>
            ))}
          </ul>
        </div>
      )}
      </div>
    </div>
    </div>
    <Footer/>
    </div>
  );
}

export default App;