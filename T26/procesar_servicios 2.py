import subprocess
import csv
from openpyxl import Workbook
try:
    #Script de PS
    subprocess.run(["powershell", "-File", "C:\\Users\\Noel\\Documents\\PS\\monitor_servicios.ps1"])

    #Archivo CSV
    csv_file = "C:\\Users\\Noel\\Documents\\PS\\servicios.csv"
    excel_file = "C:\\Users\\Noel\\Documents\\PS\\servicios.xlsx"

    #Excel
    wb = Workbook()
    ws = wb.active
    ws.title = "Monitoreo de servicios"

    with open(csv_file, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            ws.append(row)

    wb.save(excel_file)

    print(f"Se exportó correctamente a {excel_file}")
    
except ModuleNotFoundError:
    print(f"El módulo utilizado no está instalado")
