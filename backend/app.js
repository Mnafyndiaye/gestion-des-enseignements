// Importation d'Express
const express = require('express');
const bodyParser = require('body-parser')
const authRoute = require('./routes/auth')
const session = require('express-session')

// Initialisation de l'application Express
const app = express();

app.use(bodyParser.json());

app.use((req, res, next) => {
  console.log('Données JSON reçues :', req.body);
  next();
});
// Montage des routes d'authentification
app.use('/auth', authRoute);

app.get('/', (req, res) => {
  res.send('Bienvenue sur l\'API de gestion des enseignements');
});

const port = 3000;
app.listen(port, () => {
  console.log(`Serveur démarré sur le port ${port}`);
});
