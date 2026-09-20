import requests
import boto3
from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest

url = "https://nqi697ppp7.execute-api.us-east-1.amazonaws.com/dev/documentos/manual.pdf"
region = "us-east-1"
service = "execute-api"

session = boto3.Session()
credentials = session.get_credentials()

if credentials is None:
    print("No se encontraron credenciales de AWS.")
    exit()

credentials = credentials.get_frozen_credentials()

request = AWSRequest(
    method="GET",
    url=url
)

SigV4Auth(credentials, service, region).add_auth(request)
headers = dict(request.headers)

respuesta = requests.get(url, headers=headers)

if respuesta.status_code == 200:
    with open("manual.pdf", "wb") as archivo:
        archivo.write(respuesta.content)

    print("Documento descargado correctamente.")
    print("Código HTTP:", respuesta.status_code)

else:
    print("Error:", respuesta.status_code)
    print(respuesta.text)