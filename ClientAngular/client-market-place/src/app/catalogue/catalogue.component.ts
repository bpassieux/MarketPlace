import { Component, OnInit } from '@angular/core';
import { Observable, throwError } from 'rxjs';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-catalogue',
  templateUrl: './catalogue.component.html',
  styleUrls: ['./catalogue.component.css']
})
export class CatalogueComponent implements OnInit {

  posts: Observable<any>|undefined

  urlAPI = "https://webmarketrestgraphql.azurewebsites.net/";

  isLoading = true;

  produits: any[]|undefined;

  constructor(private http: HttpClient) {}

  numeroCarte: number|undefined;
  etatCarte = "Attente"

  ngOnInit(): void {
    console.log("GET PRODUITS");
    var url = this.urlAPI;
    url = url.concat('produit');
    this.posts = this.http.get(url);
    this.posts.forEach(async (value) => {
       this.produits = await value["produit"];
       this.isLoading = false;
    });
  }

  onClickVerifCard(){
    console.log("VERIFICATION CARTE");
    var numAValider = this.numeroCarte?.toString();
    var url = this.urlAPI;
    url = url.concat('verification' + "/" + this.numeroCarte?.toString());
    this.posts = this.http.get(url);
    this.posts.forEach(async (value) => {
      var res = await value["result"];
      console.log(res);
      if(res == false){
        this.etatCarte = "Refuse";
      }else{
        this.etatCarte = "Accepte";
      }
    })
  }

}
