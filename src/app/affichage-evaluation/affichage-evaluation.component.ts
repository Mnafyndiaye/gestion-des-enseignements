import { Component, OnInit } from '@angular/core';

interface Evaluation {
    etudiant: string;
    presentation: {
        syllabus: string;
        objectifs: string;
    };
    deroulement: {
        conforme: string;
        support: string;
    };
    conditions: {
        salle: string;
    };
    suggestions: {
        liens: string;
        commentaires: string;
    };
}

@Component({
  selector: 'app-affichage-evaluation',
  templateUrl: './affichage-evaluation.component.html',
  styleUrls: ['./affichage-evaluation.component.css']
})
export class AffichageEvaluationComponent implements OnInit {
    evaluations: Evaluation[];

    ngOnInit() {
        this.afficherEvaluations();
    }

    afficherEvaluations() {
        this.evaluations = [
            {
                etudiant: "Anonymous",
                presentation: {
                    syllabus: "oui",
                    objectifs: "oui"
                },
                deroulement: {
                    conforme: "oui",
                    support: "non"
                },
                conditions: {
                    salle: "moyenne"
                },
                suggestions: {
                    liens: "tres-lies",
                    commentaires: "Très bon cours, mais pourrait bénéficier d'un meilleur support de cours."
                }
            }
        ];
    }
}

