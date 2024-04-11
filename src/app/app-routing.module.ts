import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { LoginComponent } from './login/login.component';
import { ProfilEtudiantComponent } from './profil-etudiant/profil-etudiant.component';
import { ProfilEnseignantComponent } from './profil-enseignant/profil-enseignant.component';
import { CahierDeTexteComponent } from './cahier-de-texte/cahier-de-texte.component';
import { SyllabusCoursComponent } from './syllabus-cours/syllabus-cours.component';
import { EvaluationEnseignementComponent } from './evaluation-enseignement/evaluation-enseignement.component';

const routes: Routes = [
  {
    path: '',
    redirectTo: '/home',
    pathMatch:'full'
  },
  {
    path: 'home',
    component: HomeComponent
  },
  {
    path: 'login',
    component: LoginComponent
  },
  {
    path: 'profil-etudiant',
    component: ProfilEtudiantComponent,
    children:[
      {
        path: 'home',
        component: HomeComponent
      },
      {
        path: 'cahier-de-texte',
        component: CahierDeTexteComponent
      },
      {
        path: 'evaluation-enseignement',
        component: EvaluationEnseignementComponent
      }
    ]
  },
  {
    path: 'profil-enseignant',
    component: ProfilEnseignantComponent
  },
  {
    path: 'syllabus-cours',
    component: SyllabusCoursComponent
  }

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
