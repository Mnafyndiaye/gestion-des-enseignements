import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor(private http: HttpClient) { }

  login(credentials: any): Observable<any>{
    return this.http.post<any>('', credentials);
  }

  logout(): Observable<any> {
    return this.http.post<any>('', {});
  }
}
