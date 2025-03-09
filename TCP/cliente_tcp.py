import socket

def cliente_tcp(host='127.0.0.1', port=8080):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        print("Conexão ao servidor bem sucedida, digite 'exit' para encerrar.\n")

        while True:
            cpf = input("Digite um CPF para validação (sem pontuação): ")
            client_socket.sendall(cpf.encode("utf-8"))
            if cpf.lower() == "exit":
                break
            response = client_socket.recv(1024).decode("utf-8")
            print(f"Resposta do servidor: {response}\n")
    
    except Exception as e:
        print(f"\nErro no cliente: {e}")
    
    finally:
        client_socket.close()
        print("\nConexão encerrada.")

if __name__ == "__main__":
    cliente_tcp()