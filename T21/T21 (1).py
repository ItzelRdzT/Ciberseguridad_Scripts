import requests 
import json
import logging
import getpass
try:
    key=getpass.getpass(prompt= 'Introduce  aquí la APiKey: ')
    headers = {}
    headers['content-type']= 'application/json'
    headers['api-version']= '3'
    headers['User-Agent']='python'
    print(f'Ha ocurrido un error inesperado')


    headers['hibp-api-key']=key
    email = input("Ingrese el correo a investigar")

    url = 'https://haveibeenpwned.com/api/v3/breachedaccount/'+\
        email+'?truncateResponse=false'
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        data = r.json()
        encontrados = len(data)
        if encontrados > 0:
            print("Los sitios en los que se ha filtrado el correo",email,"son:")
        else:
            print("El correo",email,"no ha sido filtrado")
        for filtracion in data:
            print(filtracion["Name"])
            print(filtracion["Domain"])
            print(filtracion["BreachDate"])
            print(filtracion["Description"])
                  
        msg = email+" Filtraciones encontradas: "+str(encontrados)
        print(msg)
        logging.basicConfig(filename='hibpINFO.log',
                            format="%(asctime)s %(message)s",
                            datefmt="%m/%d/%Y %I:%M:%S %p",
                            level=logging.INFO)
        logging.info(msg)
    else:
        msg = r.text
        print(msg)
        logging.basicConfig(filename='hibpERROR.log',
                            format="%(asctime)s %(message)s",
                            datefmt="%m/%d/%Y %H:%M:%S",
                            level=logging.ERROR)
        logging.error(msg)
        with open ('reporte_filtracion.txt', 'w') as file:
                file.write(f"Reporte de filtraciones para el correo: {email}\n")
                file.write("=" * 40 + "\n")
except:
    print(f'Ha ocurrido un error inesperado, intentelo de nuevo')
