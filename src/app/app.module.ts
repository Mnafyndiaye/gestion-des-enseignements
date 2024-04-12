import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './login/login.component';
import { HomeComponent } from './home/home.component';
import { ProfilEtudiantComponent } from './profil-etudiant/profil-etudiant.component';
import { EvaluationEnseignementComponent } from './evaluation-enseignement/evaluation-enseignement.component';
import { CahierDeTexteComponent } from './cahier-de-texte/cahier-de-texte.component';
import { SyllabusCoursComponent } from './syllabus-cours/syllabus-cours.component';
import { ProfilEnseignantComponent } from './profil-enseignant/profil-enseignant.component';
import { StudentSidebarComponent } from './student-sidebar/student-sidebar.component';
import { TeacherSidebarComponent } from './teacher-sidebar/teacher-sidebar.component';
import { AffichageSyllabusComponent } from './affichage-syllabus/affichage-syllabus.component';
import { AffichageEvaluationComponent } from './affichage-evaluation/affichage-evaluation.component';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    HomeComponent,
    ProfilEtudiantComponent,
    EvaluationEnseignementComponent,
    CahierDeTexteComponent,
    SyllabusCoursComponent,
    ProfilEnseignantComponent,
    StudentSidebarComponent,
    TeacherSidebarComponent,
    AffichageSyllabusComponent,
    AffichageEvaluationComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
