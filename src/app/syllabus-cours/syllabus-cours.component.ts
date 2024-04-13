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

  openModalAjouter() {
    this.modalAjouter.nativeElement.style.display = 'block';
  }

  closeModalAjouter() {
    this.modalAjouter.nativeElement.style.display = 'none';
  }

  validerAjout() {
    const selectCours = (document.getElementById('select-cours') as HTMLSelectElement).value;
    const date = (document.getElementById('date') as HTMLInputElement).value;
    const description = (document.getElementById('description') as HTMLTextAreaElement).value;

    const nouvelleEntree = document.createElement('li');
    nouvelleEntree.textContent = `${selectCours} - ${date}: ${description}`;

    this.cahierTexte.nativeElement.appendChild(nouvelleEntree);

    this.btnModifier.nativeElement.style.display = 'inline';
    this.btnSupprimer.nativeElement.style.display = 'inline';

    this.closeModalAjouter();
  }

  supprimerEntree() {
    this.cahierTexte.nativeElement.innerHTML = '';
    this.btnModifier.nativeElement.style.display = 'none';
    this.btnSupprimer.nativeElement.style.display = 'none';
  }
}
