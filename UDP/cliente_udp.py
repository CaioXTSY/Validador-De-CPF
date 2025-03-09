import socket

def cliente_udp(host='127.0.0.1', port=8080):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print("Cliente UDP pronto, digite 'exit' para encerrar.\n")

        while True:
            cpf = input("Digite um CPF para validação (sem pontuação): ")
            if cpf.lower() == "exit":
                break
            client_socket.sendto(cpf.encode("utf-8"), (host, port))
            response, _ = client_socket.recvfrom(1024)
            print(f"Resposta do servidor: {response.decode('utf-8')}\n")

    except Exception as e:
        print(f"\nErro no cliente: {e}")
    
    finally:
        client_socket.close()
        print("\nConexão encerrada.")

if __name__ == "__main__":
    cliente_udp()