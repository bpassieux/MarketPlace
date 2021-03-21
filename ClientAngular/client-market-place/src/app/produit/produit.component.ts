import { Component, OnInit, Input} from '@angular/core';
import { Observable, throwError } from 'rxjs';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-produit',
  templateUrl: './produit.component.html',
  styleUrls: ['./produit.component.css']
})
export class ProduitComponent implements OnInit {

  @Input() nomProduit = 0;
  @Input() prixProduit = 0;
  @Input() poidsProduit = 0;
  @Input() nombreProduit = 0;
  distance = 0;
  prixFinal = 0;

  posts: Observable<any>|undefined

  urlAPI = "https://webmarketrestgraphql.azurewebsites.net/";

  constructor(private http: HttpClient) {}

  onClickFinal(){
    console.log("CALCUL PRIX FINAL");
    var url = this.urlAPI;
    url = url.concat('soap/' + this.prixProduit?.toString() + "/" + this.poidsProduit?.toString() + "/" + this.distance.toString()+ "/" +  this.nombreProduit?.toString());
    this.posts = this.http.get(url);
    this.posts.forEach(async (value) => {
      this.prixFinal = await value[0];
      console.log(this.prixFinal);
    });
  }

  ngOnInit(): void {}

}
