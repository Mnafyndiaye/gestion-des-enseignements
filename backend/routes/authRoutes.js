const express = require('express');
const router = express.Router();
const mysql = require('mysql'); // Assurez-vous d'importer mysql si vous l'utilisez ici

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

    // Stocker l'identifiant de l'utilisateur dans la session
    req.session.userId = results[0].id;

    // Récupérer le rôle de l'utilisateur
    const userRole = results[0].role;

    // Rediriger l'utilisateur en fonction de son rôle
    if (userRole === 'teacher') {
      // Si l'utilisateur est un enseignant, rediriger vers la page du tableau de bord de l'enseignant
      res.redirect('/dashboard/teacher');
    } else if (userRole === 'student') {
      // Si l'utilisateur est un étudiant, rediriger vers la page du tableau de bord de l'étudiant
      res.redirect('/dashboard/student');
    } else {
      // Gérer les autres cas (par exemple, si le rôle n'est pas défini correctement)
      res.status(403).send('Rôle d\'utilisateur non valide');
    }
  });
});

module.exports = router;
