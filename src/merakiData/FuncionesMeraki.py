from dotenv import dotenv_values
import meraki as mrk
class FuncionesMeraki:


    config = {
    **dotenv_values(".env"),  # load shared development variables
    } 
    
    dashboard = mrk.DashboardAPI( config['API'] ,output_log=False,print_console=False)
 
    @classmethod
    def getAllNetworks(cls) -> list:
        response = cls.dashboard.organizations.getOrganizationNetworks(cls.config['ORGJUNJI'],total_pages='all',perPage='1300')
        lista = []
        for nombres in response:
            nombre = nombres["name"]
            lista.append({
                "label": nombre
            })
        return lista 
  

    @classmethod
    def updatePassword(cls,nombreNetwork: str, password: str) -> str:
        response = cls.dashboard.organizations.getOrganizationNetworks(cls.config['ORGJUNJI'],perPage='1300',total_pages="all")
        for datos in response:
            if nombreNetwork in datos["name"]:
                id_network = datos["id"]

        ssidTotal = cls.dashboard.wireless.getNetworkWirelessSsids(
            id_network
        )
       
        for ssid in ssidTotal:
            lista_nueva={"number": str(ssid["number"])   if "defaultVlanId" in dict.keys(ssid) else ""}
            if lista_nueva['number'] != "" and ssid['defaultVlanId'] == 30:
                number=int(lista_nueva['number'])
            
        response = cls.dashboard.wireless.updateNetworkWirelessSsid(
             id_network, number, 
             psk=password
        )
        return response 


