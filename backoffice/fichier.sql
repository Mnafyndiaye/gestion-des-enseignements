DROP database IF EXISTS ETUDIANTS;
create database ETUDIANTS;
use ETUDIANTS;



create TABLE Etudiant(
    idEtudiant int auto_increment primary key,
    nom VARCHAR(25),
    prenom VARCHAR(30),
    mail VARCHAR(30)
);

create TABLE Enseignant(
    idEnseignant int auto_increment primary key,
    nom VARCHAR(25),
    prenom VARCHAR(30)
);


create TABLE RP(
    idRP int auto_increment primary key,
    nom VARCHAR(25),
    prenom VARCHAR(30)
);


create TABLE Remarque(
    idRemarque int auto_increment primary key,
    idEtudiant int,
    idEnseignant int,
    ContenuRendu TEXT,
    marque TEXT,
    CONSTRAINT FK_remarque_etudiant FOREIGN KEY(idEtudiant) REFERENCES Etudiant(idEtudiant),
    CONSTRAINT FK_remarque_enseignant FOREIGN KEY(idEnseignant) REFERENCES Enseignant(idEnseignant)
);

create TABLE Cahier_texte(
    idCahier int auto_increment primary key,
    idCours int,
    date varchar(30),
    Description TEXT
);


create TABLE Cours(
    idCours int auto_increment primary key,
    idEnseignant int,
    CONSTRAINT FK_cours_enseignant FOREIGN KEY(idEnseignant) REFERENCES Enseignant(idEnseignant)
);


create TABLE Classe(
    idClasse int auto_increment primary key,
    nomClasse VARCHAR(20),
    anneeScolaire DATE
);
