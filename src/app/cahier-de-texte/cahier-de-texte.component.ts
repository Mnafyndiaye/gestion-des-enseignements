import { Component, ElementRef, ViewChild } from '@angular/core';

@Component({
  selector: 'app-cahier-de-texte',
  templateUrl: './cahier-de-texte.component.html',
  styleUrls: ['./cahier-de-texte.component.css']
})
export class CahierDeTexteComponent {
  @ViewChild('modalAjouter') modalAjouter!: ElementRef;
  @ViewChild('btnAjouter') btnAjouter!: ElementRef;
  @ViewChild('btnValiderAjout') btnValiderAjout!: ElementRef;
  @ViewChild('btnModifier') btnModifier!: ElementRef;
  @ViewChild('btnSupprimer') btnSupprimer!: ElementRef;
  @ViewChild('closeBtn') closeBtn!: ElementRef;
  @ViewChild('cahierTexte') cahierTexte!: ElementRef;

  // Ouvrir le modal d'ajout
  openModalAjouter() {
    this.modalAjouter.nativeElement.style.display = 'block';
  }

  // Fermer le modal d'ajout en cliquant sur le bouton 'x' ou en dehors du modal
  closeModalAjouter() {
    this.modalAjouter.nativeElement.style.display = 'none';
  }

  // Ajouter une nouvelle entrée dans le cahier de texte
  validerAjout() {
    const selectCours = (document.getElementById('select-cours') as HTMLSelectElement).value;
    const date = (document.getElementById('date') as HTMLInputElement).value;
    const description = (document.getElementById('description') as HTMLTextAreaElement).value;

    // Créer un nouvel élément li
    const nouvelleEntree = document.createElement('li');
    nouvelleEntree.textContent = `${selectCours} - ${date}: ${description}`;

    // Ajouter la nouvelle entrée à la liste du cahier de texte
    this.cahierTexte.nativeElement.appendChild(nouvelleEntree);

    // Afficher les boutons "Modifier" et "Supprimer"
    this.btnModifier.nativeElement.style.display = 'inline';
    this.btnSupprimer.nativeElement.style.display = 'inline';

    // Fermer le modal d'ajout
    this.closeModalAjouter();
  }

  // Supprimer une entrée du cahier de texte
  supprimerEntree() {
    this.cahierTexte.nativeElement.innerHTML = ''; // Effacer toutes les entrées
    this.btnModifier.nativeElement.style.display = 'none'; // Masquer le bouton "Modifier"
    this.btnSupprimer.nativeElement.style.display = 'none'; // Masquer le bouton "Supprimer"
  }
}
