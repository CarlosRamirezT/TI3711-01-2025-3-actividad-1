# distributed_example.py
"""
Demostración de computación distribuida simple usando xmlrpc.
"""
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.client import ServerProxy
import threading

def start_server():
    server = SimpleXMLRPCServer(("localhost", 8000), logRequests=False)
    def square(x):
        print(f"Servidor procesando {x}")
        return x * x
    server.register_function(square, "square")
    server.serve_forever()

def main():
    # Iniciar el servidor en un hilo
    server_thread = threading.Thread(target=start_server, daemon=True)
    server_thread.start()

    # Cliente que consume el servicio remoto
    client = ServerProxy("http://localhost:8000/")
    datos = [2, 4, 6, 8]
    print("Cliente solicitando cálculo remoto...")
    resultados = [client.square(x) for x in datos]
    print("Resultados remotos:", resultados)

if __name__ == "__main__":
    main()
