import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { DomSanitizer } from '@angular/platform-browser';

import { Data } from './app.model';

import { DataService } from './app.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'app';
  data: Data[];
  receivedData: boolean;
  orderByField: string;
  reverseSort: boolean;
  downloadJsonHref: any;
  noData: boolean;

  constructor(
    private router: Router,
    private dataService: DataService,
    private sanitizer: DomSanitizer
  ) {};

  ngOnInit(): void{
    this.noData = false;
    this.orderByField = 'id_num';
    this.reverseSort = false;
    this.receivedData = false;
    this.dataService.fetchData().then(resp => {
      this.data = resp;
      if(this.data.length <= 0) {
        this.noData = true;
      }
      this.receivedData = true;
    });
  }

  refreshData(): any{
    this.receivedData = false;
    this.dataService.refreshData().then(resp => {
      this.data = resp;
      this.receivedData = true;
    });
  }

  updateOrderField(column: string): void{
    this.orderByField = column;
    this.reverseSort = !this.reverseSort;
  }

  sortData(column: string): Data[]{
    const dataSort = this.data.sort((a, b) => a[column] > b[column] ? 1: a[column] === b[column] ? 0: -1);
    if (this.reverseSort) { dataSort.reverse(); }
    this.generateJson(dataSort);
    return dataSort;
  }

  generateJson(inpData: any): void{
    var currData = JSON.stringify(inpData);
    var uri = "data:text/json;charset=UTF-8,"  + encodeURIComponent(currData);
    this.downloadJsonHref = uri;
  }

  downloadJson(): void{
     var link = document.createElement("a");
     link.download = "data.json";
     link.href = this.downloadJsonHref
     link.click();
  }
}
