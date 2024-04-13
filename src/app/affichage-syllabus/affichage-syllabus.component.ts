import { Component } from '@angular/core';
import { Component, OnInit, HttpClient } from '@angular/core';

@Component({
  selector: 'app-affichage-syllabus',
  templateUrl: './affichage-syllabus.component.html',
  styleUrls: ['./affichage-syllabus.component.css']
})
export class AffichageSyllabusComponent {

  syllabusData: Array<{ cours: string, document: string}>;
  httpClient: any;

  constructor() {
    this.syllabusData = [
      { cours: "Java", document: "javasyllabus.pdf" },
      { cours: "MSI", document: "msi_syllabus.docx" },
      { cours: "HTML", document: "html_syllabus.pdf" }
    ];
  }

  ngOnInit(): void {

    this.httpClient.get('url-du-service')
      .suscribe((data: { cours: string; document: string; }[]) => {
        this.syllabusData = data;
      },(error: any) => {
        console.error('Erreur lors de la récupération des données du syllabus:', error);
      });
    
  }
}
