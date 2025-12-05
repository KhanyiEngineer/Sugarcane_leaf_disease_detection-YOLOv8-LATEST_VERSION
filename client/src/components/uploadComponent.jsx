import React, { useState } from 'react';

const UploadComponent = () => {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleUpload = async () => {
    if (!file) return;
    
    const formData = new FormData();
    formData.append('file', file);
    
    try {
      const response = await fetch('/upload', {
        method: 'POST',
        body: formData
      });

      const data = await response.json();
      setResult(data);
    } catch (error) {
      console.error('Error uploading file:', error);
    }
  };

  return (
    <div style={{ padding: '20px' }}>
      <h1>Upload Image for YOLOv8 Inference</h1>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleUpload} style={{ marginLeft: '10px' }}>
        Upload
      </button>

      {result && (
        <div style={{ marginTop: '20px' }}>
          <h2>Inference Completed</h2>
          <img
            src={result.image_url}
            alt="YOLOv8 Inference Result"
            style={{ maxWidth: '100%', maxHeight: '500px' }}
          />
        </div>
      )}
    </div>
  );
};

export default UploadComponent;
