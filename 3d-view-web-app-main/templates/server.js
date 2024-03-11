const express = require('express');
const { exec } = require('child_process');
const path = require('path');

const app = express();
const port = 5000;

// Serve static files from the 'static' directory
app.use(express.static(path.join(__dirname, 'static')));

app.get('/', (req, res) => {
  res.send('Hello, this is the root path!');
});

app.get('/decode/:fileName', (req, res) => {
  const fileName = req.params.fileName;
  const pythonScriptPath = path.join(__dirname, 'venv', 'Scripts', 'Hidden_Extractor.py');

  const command = `python ${pythonScriptPath} ${fileName}`;
  exec(command, (error, stdout, stderr) => {
    if (error) {
      console.error(`Error executing Python script: ${error.message}`);
      return res.status(500).send('Internal Server Error');
    }

    console.log(`Hidden message decoded: ${stdout}`);
    res.send(stdout);
  });
});

// Serve other static files from the 'public' directory
app.use(express.static(path.join(__dirname, 'public')));

// Listen on the specified port
app.listen(port, () => {
  console.log(`Server listening at http://localhost:${port}`);
});
