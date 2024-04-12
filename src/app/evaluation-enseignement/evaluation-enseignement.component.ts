import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-formulaire-evaluation',
  templateUrl: './formulaire-evaluation.component.html',
  styleUrls: ['./formulaire-evaluation.component.css']
})
export class FormulaireEvaluationComponent implements OnInit {
  evaluationForm: FormGroup;

  constructor(private formBuilder: FormBuilder) { }

  ngOnInit(): void {
    this.creerFormulaire();
  }

  creerFormulaire() {
    this.evaluationForm = this.formBuilder.group({
      syllabus: ['', Validators.required],
      objectifs: ['', Validators.required],
      conforme: ['', Validators.required],
      support: ['', Validators.required],
      salle: ['', Validators.required],
      'liens-ec': ['', Validators.required],
      commentaires: ['']
    });
  }

  validerEvaluation() {
    if (this.evaluationForm.valid) {
      // Envoyer le formulaire ou effectuer d'autres actions nécessaires
      console.log(this.evaluationForm.value);
    } else {
      // Afficher des messages d'erreur ou prendre d'autres mesures nécessaires
      console.log('Le formulaire est invalide.');
    }
  }
}
