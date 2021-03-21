from flask import Flask
from flask import jsonify
from flask import request
from zeep import Client
from flask_cors import CORS

import graphene
import json

urlSOAP = "https://webmarketsoap.azurewebsites.net/?wsdl"

# Creation de l'instance
app = Flask(__name__)
CORS(app)

class Produit(graphene.ObjectType):
    nomProduit = graphene.String()
    prixProduit = graphene.String()
    poidsProduit = graphene.String()

class Query(graphene.ObjectType):
    produit = graphene.List(Produit)
    # Obtention des produits
    def resolve_produit(self, info):
        return[
                Produit(nomProduit = "L'Épée de la providence", prixProduit = "7", poidsProduit = "1"),
                Produit(nomProduit = "Le Dernier Voeu", prixProduit = "7", poidsProduit = "1"),
                Produit(nomProduit = "Le Sang des elfes", prixProduit = "7", poidsProduit = "1"),
                Produit(nomProduit = "Le Temps du mérpis", prixProduit = "7", poidsProduit = "1"),
                Produit(nomProduit = "Le Baptême du feu", prixProduit = "7", poidsProduit = "1"),
                Produit(nomProduit = "La Tour de l'hirondelle", prixProduit = "8", poidsProduit = "2"),
                Produit(nomProduit = "La Dame du lac", prixProduit = "9", poidsProduit = "2"),
                Produit(nomProduit = "La Saison des orages", prixProduit = "6", poidsProduit = "1"),        
            ]

@app.route("/", methods=['GET'])
def test():
    return "Hello World !"

@app.route("/soap/<prixProduit>/<poidsProduit>/<distance>/<nombre>", methods=['GET'])
def getPrixFrinal(prixProduit, poidsProduit, distance, nombre):
    client = Client(urlSOAP)
    prixFinal = client.service.fdp(prixProduit, distance, poidsProduit, nombre)
    print(prixFinal)
    res = [prixFinal]
    return str(res)

@app.route("/verification/<numCarte>", methods = ['GET'])
def verifCarteBancaire(numCarte):
    res = False
    if(len(numCarte) == 16):
        res = True
    #    c=0
    #    summ=0
    #    second=False
    #    length=len(numCarte);
    #    for i in range (length-1,-1,-1):
    #        c=int(numCarte[i])
    #        if second==True:
    #            c=c*2	
    #        summ=summ+c/10
    #        summ=summ+c%10
    #        second= not second
    #    if summ%10==0:	
    #        return jsonify({'result' : True})
    return jsonify({'result' : res})

@app.route("/produit", methods = ['GET'])
def getProduits():
    #Déclaration du schéma pour récuppérer les produits sous la bonne forme
    schema = graphene.Schema(query=Query)
    query_produit = '{ produit{nomProduit prixProduit poidsProduit} }'
    res = schema.execute(query_produit)
    items = dict(res.data.items())
    print(items)
    return json.dumps(items, indent=4)


if(__name__=="__main__"):
    app.run()