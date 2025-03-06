import socket

def validar_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))

    if len(cpf) != 11:
        return False
    
    if cpf == cpf[0] * 11:
        return False
    
    # Primeiro digito
    total = 0
    for i in range(9):
        total += int(cpf[i]) * (10 - i)
    resto = total % 11
    d1 = 0 if resto < 2 else 11 - resto

    # Segundo digito
    total = 0
    for i in range(10):
        total += int(cpf[i]) * (11 - i)
    resto = total % 11
    d2 = 0 if resto < 2 else 11 - resto

    return cpf[-2:] == f"{d1}{d2}"

def servidor(host='127.0.0.1', port=8080):
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(f"Servidor conectado em {host} : {port}")
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
    servidor()