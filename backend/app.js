// app.js

// Importer Express
const express = require('express');
const bodyparser = require('body-parser');
const mysql = require('mysql');

// Créer une instance de l'application
const app = express();

const connection = mysql.createConnection({
  host: 'localhost',
  user: 'apinafy',
  password: 'Passer123',
  database: 'enseignements_db'
});

connection.connect((err) => {
  if (err) {
    console.error('Erreur de connexion à la base de données MySQL :', err);
    return;
  }
  console.log('Connecté à la base de données MySQL');
});
// Middleware pour le parsing du corps de la requête JSON
app.use(express.json());

// Route GET
app.get('/api/hello', (req, res) => {
    res.json({ message: 'Hello, World!' });
});

// Route POST
app.post('/api/echo', (req, res) => {
    const message = req.body.message;
    res.json({ echo: message });
});

// Démarrer le serveur
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
