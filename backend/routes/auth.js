  const connection = require('../db');
  const express = require('express');

  const router = express.Router();

  // Fonction pour gérer la connexion de l'utilisateur
router.post('/login', (req, res) => {
    const { email, password } = req.body;

  // Vérifier les informations d'identification de l'utilisateur dans la table des enseignants
  const queryEnseignants = 'SELECT * FROM enseignants WHERE email = ? AND password = ?';
  connection.query(queryEnseignants, [email, password], (errorEnseignants, resultsEnseignants) => {
      if (errorEnseignants) {
          console.error('Erreur lors de la vérification des informations de connexion des enseignants :', errorEnseignants);
          res.status(500).send('Erreur du serveur');
          return;
      }

      if (resultsEnseignants.length === 1) {
          // L'utilisateur est un enseignant
          req.session.userId = resultsEnseignants[0].id;
          res.redirect('/profil-enseignant');
      } else {
          // Si l'utilisateur n'est pas un enseignant, vérifier s'il est un étudiant
          const queryEtudiants = 'SELECT * FROM etudiants WHERE email = ? AND password = ?';
          connection.query(queryEtudiants, [email, password], (errorEtudiants, resultsEtudiants) => {
              if (errorEtudiants) {
                  console.error('Erreur lors de la vérification des informations de connexion des étudiants :', errorEtudiants);
                  res.status(500).send('Erreur du serveur');
                  return;
              }

              if (resultsEtudiants.length === 1) {
                  // L'utilisateur est un étudiant
                  req.session.userId = resultsEtudiants[0].id;
                  res.redirect('/profil-etudiant');
              } else {
                  // Aucun utilisateur trouvé avec ces informations d'identification
                  res.status(401).send('Nom d\'utilisateur ou mot de passe incorrect');
              }
          });
      }
  });
})

module.exports = router