from pymongo import MongoClient 
import certifi 

MONGO = 'mongodb+srv://Mariana:Ucundinamarca@cluster0.bfrzm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'

certificado = certifi.where()
def Conexion():
    try: 
        client = MongoClient(MONGO, tlsCAFile=certificado)
        bd = client["bd_BienestarAnimal"]
    except ConnectionError:
        print('Error de conexión')
    return bd