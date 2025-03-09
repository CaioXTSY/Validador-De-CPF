import socket
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from validar_cpf import validar_cpf

def servidor_tcp(host='127.0.0.1', port=8080):
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(f"Servidor rodando em {host} : {port}")
        server_socket.bind((host, port))
        server_socket.listen()
        print("Aguardando conexões...")
    
        while True:
            client_socket, client_adress = server_socket.accept()
            with client_socket:
                print("-------------------------------------------------------")
                print(f"Conexão com {client_adress}\n")
                while True:
                    cpf = client_socket.recv(1024).decode("utf-8")
                    if cpf.lower() == "exit":
                        print(f"{client_adress} encerrou a conexão.")
                        break
                    print(f"CPF recebido: {cpf}")
                    print("Validando...")
                    validacao = validar_cpf(cpf)
                    response = "CPF válido" if validacao else "CPF inválido"
                    print("O CPF inserido é valido\n") if validacao else print("O CPF inserido é inválido\n")
                    client_socket.sendall(response.encode("utf-8"))

    except Exception as e:
        print(f"\nErro no servidor: {e}")
    
    finally:
        server_socket.close()
        print("\nServidor encerrado.")

if __name__ == "__main__":
    servidor_tcp()