// Importer Express
const express = require('express');
const bodyParser = require('body-parser');
const mysql = require('mysql');
const session = require('express-session')

// Créer une instance de l'application
const app = express();
const api = require('./routes/api');

// Middleware pour le parsing du corps de la requête JSON
app.use(bodyParser.json());

// Middleware pour la gestion des sessions
app.use(session({
  secret: 'Mazeyasimon',
  resave: false,
  saveUninitialized: true
}));
// Connexion à la base de données MySQL
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

// Utilisez la connexion MySQL dans votre API
app.use('/api', api(connection));

// Démarrer le serveur
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
