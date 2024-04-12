const express = require('express')
const router = express.Router()

// Route POST pour la soumission du formulaire de connexion
router.post('/login', (req, res) => {
  const { username, password } = req.body;

  // Vérifier les informations d'identification de l'utilisateur dans la base de données
  const query = 'SELECT * FROM users WHERE username = ? AND password = ?';
  connection.query(query, [username, password], (error, results) => {
    if (error) {
      console.error('Erreur lors de la vérification des informations de connexion :', error);
      res.status(500).send('Erreur du serveur');
      return;
    }

    // Vérifiez si l'utilisateur existe dans la base de données
    if (results.length === 0) {
      res.status(401).send('Nom d\'utilisateur ou mot de passe incorrect');
      return;
    }

    // L'utilisateur existe dans la base de données, ouvrir une session
    req.session.user = results[0]; // Stockez les informations de l'utilisateur dans la session
    res.redirect('/profile'); // Rediriger vers la page de profil de l'utilisateur
  });
});

module.exports = router