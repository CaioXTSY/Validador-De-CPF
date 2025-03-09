import socket
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from validar_cpf import validar_cpf

def servidor_udp(host='127.0.0.1', port=8080):
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_socket.bind((host, port))
        print(f"Servidor UDP rodando em {host}:{port}")

        while True:
            cpf, client_address = server_socket.recvfrom(1024)
            cpf = cpf.decode("utf-8")
            if cpf.lower() == "exit":
                print(f"{client_address} encerrou a conexão.")
                continue
            print("-------------------------------------------------------")
            print(f"\nCPF recebido de {client_address}: {cpf}")
            validacao = validar_cpf(cpf)
            response = "CPF válido" if validacao else "CPF inválido"
            print("O CPF inserido é valido\n") if validacao else print("O CPF inserido é inválido\n")
            server_socket.sendto(response.encode("utf-8"), client_address)

    except Exception as e:
        print(f"\nErro no servidor: {e}")
    
    finally:
        server_socket.close()
        print("\nServidor encerrado.")

if __name__ == "__main__":
    servidor_udp()