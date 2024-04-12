const express = require('express');
const router = express.Router();
const mysql = require('mysql'); // Assurez-vous d'importer mysql si vous l'utilisez ici
const authController = require('../controllers/authController');

router.post('/login', authController.login);

module.exports = router;
