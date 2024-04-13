import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-cahier-de-texte',
  templateUrl: './cahier-de-texte.component.html',
  styleUrls: ['./cahier-de-texte.component.css']
})
export class CahierDeTexteComponent {
  modalVisible: boolean = false;
  cahierForm: FormGroup;

  constructor(private formBuilder: FormBuilder) {
    this.creerFormulaire();
  }

  creerFormulaire() {
    this.cahierForm = this.formBuilder.group({
      cours: ['', Validators.required],
      date: ['', Validators.required],
      description: ['', Validators.required]
    });
  }

  ouvrirModal() {
    this.modalVisible = true;
  }

  fermerModal() {
    this.modalVisible = false;
  }

  validerAjout() {
    if (this.cahierForm.valid) {
      const nouvelleEntree = `${this.cahierForm.value.cours} - ${this.cahierForm.value.date}: ${this.cahierForm.value.description}`;
      // Ajouter la nouvelle entrée à votre liste de cahier de texte
      this.fermerModal();
      this.cahierForm.reset();
    } else {
      // Gérer les erreurs de validation du formulaire
    }
  }
}
