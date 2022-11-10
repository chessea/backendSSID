from app import app
from flask import jsonify,request
import meraki as mrk
from dotenv import dotenv_values
from merakiData.FuncionesMeraki import FuncionesMeraki

#
@app.route('/meraki', methods=['GET'])
def getJardinesConfig():
   
    return jsonify ( { "networks": FuncionesMeraki.getAllNetworks()}),201


@app.route('/meraki', methods=['POST'])
def updateJardinesPass( ):
    req = request.get_json()

    print(req)


    data=FuncionesMeraki.updatePassword(req['network'], req['password'])

   
    return jsonify ( { "ok": data}),201
