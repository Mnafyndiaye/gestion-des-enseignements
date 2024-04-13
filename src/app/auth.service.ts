import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { catchError, tap } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  private apiUrl = 'http://localhost:3000'; // URL de votre API backend

  constructor(private http: HttpClient) { }

  login(username: string, password: string): Observable<any> {
    return this.http.post<any>(`${this.apiUrl}/login`, { username, password })
      .pipe(
        tap(response => {
          // Gérer la réponse de connexion
          localStorage.setItem('token', response.token);
          localStorage.setItem('role', response.role); // Stocker le rôle de l'utilisateur
        }),
        catchError(this.handleError<any>('login'))
      );
  }

  logout(): Observable<any> {
    // Supprimer le token JWT et le rôle du localStorage
    localStorage.removeItem('token');
    localStorage.removeItem('role');
    return of(null); // Retourner un observable vide
  }

  isAuthenticated(): boolean {
    // Vérifier si l'utilisateur est authentifié en vérifiant la présence du token JWT dans le localStorage
    return !!localStorage.getItem('token');
  }

  getUserRole(): string {
    // Récupérer le rôle de l'utilisateur depuis le localStorage
    return localStorage.getItem('role') ?? '';
  }

  private handleError<T>(operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {
      console.error(error);
      return of(result as T);
    };
  }
}
