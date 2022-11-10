from app import app
from flask import jsonify,request
import meraki as mrk
from dotenv import dotenv_values
from merakiData.FuncionesMeraki import FuncionesMeraki
from merakiData.Api import Api


@app.route('/meraki', methods=['GET'])
def getJardinesConfig(): 
    return jsonify ( { "networks": FuncionesMeraki.getAllNetworks()}),200


@app.route('/meraki', methods=['POST'])
def updateJardinesPass( ):
    req = request.get_json()
    print(req)
    data=FuncionesMeraki.updatePassword(req['network'], req['password'])
    return jsonify ( { "ok": data}),201


@app.route('/meraki/api', methods=['POST'])
def getOrg():
    req = request.get_json()
    respuesta= Api.getNameOrganization( req['api-key'])
    
    if respuesta == '':
        return jsonify({ 'error': 'Api no encontrada '  }), 400 
    else:
        return jsonify({ 'organizacion':respuesta }),200 

        

