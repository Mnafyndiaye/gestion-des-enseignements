DROP DATABASE IF EXISTS enseignements_db;
CREATE DATABASE enseignements_db;
USE enseignements_db;

-- Table des étudiants
CREATE TABLE Etudiant (
    idEtudiant INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(25),
    prenom VARCHAR(30),
    mail VARCHAR(30),
    role ENUM('etudiant', 'responsable_classe') DEFAULT 'etudiant',
    idclasse int(11)
);

-- Table des enseignants
CREATE TABLE Enseignant (
    idEnseignant INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(25),
    prenom VARCHAR(30),
    role ENUM('enseignant', 'responsable_pedagogique') DEFAULT 'enseignant'
);

-- Table des remarques/évaluations
CREATE TABLE Remarque (
    idRemarque INT AUTO_INCREMENT PRIMARY KEY,
    idCours INT,
    syllabusFourni ENUM('oui', 'non'),
    objectifsClairs ENUM('oui', 'non'),
    contenuConforme ENUM('oui', 'non'),
    supportFourni ENUM('oui', 'non'),
    capaciteSalle VARCHAR(20),
    liensEc VARCHAR(20),
    commentaires TEXT,
    FOREIGN KEY (idCours) REFERENCES Cours(idCours)
);

-- Table des cours
CREATE TABLE Cours (
    idCours INT AUTO_INCREMENT PRIMARY KEY,
    idEnseignant INT,
    nomCours VARCHAR(50),
    FOREIGN KEY (idEnseignant) REFERENCES Enseignant(idEnseignant)
);

-- Table des classes
CREATE TABLE Classe (
    idClasse INT AUTO_INCREMENT PRIMARY KEY,
    nomClasse VARCHAR(20),
    anneeScolaire varchar(20)
);

-- Table des évaluations
CREATE TABLE Evaluation (
    idEvaluation INT AUTO_INCREMENT PRIMARY KEY,
    idEtudiant INT,
    idCours INT,
    note DECIMAL(5,2),
    commentaire TEXT,
    FOREIGN KEY (idEtudiant) REFERENCES Etudiant(idEtudiant),
    FOREIGN KEY (idCours) REFERENCES Cours(idCours)
);

-- Table des responsables de classe
CREATE TABLE ResponsableClasse (
    idResponsable INT AUTO_INCREMENT PRIMARY KEY,
    idEtudiant INT,
    idClasse INT,
    FOREIGN KEY (idEtudiant) REFERENCES Etudiant(idEtudiant),
    FOREIGN KEY (idClasse) REFERENCES Classe(idClasse)
);

-- Table des responsables pédagogiques
CREATE TABLE ResponsablePedagogique (
    idResponsable INT AUTO_INCREMENT PRIMARY KEY,
    idEnseignant INT,
    niveau VARCHAR(30),
    FOREIGN KEY (idEnseignant) REFERENCES Enseignant(idEnseignant)
);

-- Table des syllabus
CREATE TABLE Syllabus (
    idSyllabus INT AUTO_INCREMENT PRIMARY KEY,
    idCours INT,
    nomFichier VARCHAR(255), -- Nom du fichier syllabus
    cheminFichier VARCHAR(255), -- Chemin du fichier syllabus sur le serveur
    FOREIGN KEY (idCours) REFERENCES Cours(idCours)
);

-- Table des entrées du cahier de texte
CREATE TABLE CahierTexte (
    idEntrée INT AUTO_INCREMENT PRIMARY KEY,
    idCours INT,
    dateEntree varchar(30),
    description TEXT,
    FOREIGN KEY (idCours) REFERENCES Cours(idCours)
);
