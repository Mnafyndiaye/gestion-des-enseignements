const express = require('express');
const router = express.Router();

// Importez les contrôleurs ou les fonctions nécessaires pour gérer l'authentification
const authController = require('../controllers/authController');

// Route pour la soumission du formulaire de connexion
router.post('/login', authController.login);

// Route pour la déconnexion
router.post('/logout', authController.logout);

// Autres routes d'authentification...

module.exports = router;
