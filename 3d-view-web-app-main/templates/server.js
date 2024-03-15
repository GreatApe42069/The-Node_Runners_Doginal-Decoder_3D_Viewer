const express = require('express');
const fetch = require('node-fetch');

const app = express();
const port = 5001; // Assuming this is the port where your Express.js server is running

app.use(express.json()); // Middleware to parse JSON bodies

app.post('/decode/:fileName', async (req, res) => {
  try {
    const fileName = req.params.fileName;
    const imageData = req.body.imageData; // Assuming the image data is sent in the request body

    // Make a POST request to the Python server
    const response = await fetch('http://localhost:5000/decode', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ image: imageData })
    });

    if (!response.ok) {
      throw new Error(`Error ${response.status}: ${response.statusText}`);
    }

    const data = await response.json();
    console.log(data);
    res.json(data);
  } catch (error) {
    console.error('Error:', error);
    res.status(500).send('Internal Server Error');
  }
});

app.listen(port, () => {
  console.log(`Server listening at http://localhost:${port}`);
});
