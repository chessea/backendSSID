import requests
import json
from flask import jsonify

class Api:

    url = "https://api.meraki.com/api/v1/organizations"
    payload = None


    @classmethod
    def getNameOrganization (cls, api : str ) -> dict:

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "X-Cisco-Meraki-API-Key": api
        }

        response = requests.request('GET', cls.url, headers=headers, data = cls.payload)
        # print(response.text.encode('utf8'))
        statusCode= response.status_code
        #print( response.headers)

        if statusCode == 200 :
            listaOrganizacion= []
            data= response.json()
            for datos in data:
                listaOrganizacion.append(datos['name']) 
      
            return   listaOrganizacion
        
        else :
            respuesta = ''
            return  respuesta

     
    