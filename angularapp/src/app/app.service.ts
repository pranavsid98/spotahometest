import { Injectable } from '@angular/core';
import { Headers, Http } from "@angular/http";
import { CanActivate, Router } from '@angular/router';

import { Data } from './app.model';

import 'rxjs/add/operator/toPromise';

@Injectable()
export class DataService {
  private url ='/api';

  constructor(private http: Http, private router: Router) { }

  fetchData(): Promise<any> {
    var dataUrl = `${this.url}/fetch_data/?format=json`;
    return this.http.get(dataUrl)
      .toPromise()
      .then(response => {
        return response.json() as Data[];
      });
  }

  refreshData(): Promise<any> {
    var dataUrl = `${this.url}/refresh_data/?format=json`;
    return this.http.get(dataUrl)
      .toPromise()
      .then(response => {
        return response.json() as Data[];
      });
  }
}
