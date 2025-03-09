# 📩 **Sistema validador de CPFs em UDP/TCP** 📤

## 👩‍💻 **Membros do Grupo** 👩‍💻

| 👤 Nome                 | 🎫 Matrícula  |
|------------------------|--------------|
| Caio Teixeira da Silva  | 22112243     |
| Gustavo Henrique dos Santos Malaquias  | 22111978     |
| Noemy Torres Pereira    | 22112110     |

## 📃 **Descrição do Projeto** 

O objetivo do projeto é implementar um sistema cliente-servidor tanto em **UDP** como **TCP** para validar um **CPF**.

**Componentes**: 
1. Servidor TCP
2. Cliente TCP
3. Servidor UDP
4. Cliente UDP
5. Algoritmo para a validação do CPF*

**OBS**: O algoritmo para a validação do CPF foi adaptado para a linguagem de programação a partir das instruções encontradas em: [Algoritmo de Validação do CPF](https://www.macoratti.net/alg_cpf.htm)

## 📄 **Estrutura do Projeto** 

```
VALIDADOR-DE-CPF/
│── TCP/
│   ├── cliente_tcp.py
│   ├── servidor_tcp.py
│── UDP/
│   ├── cliente_udp.py
│   ├── servidor_udp.py
│── README.md
│── validar_cpf.py
```

## 🔄 **Como Executar** 

Execute o servidor e cliente de sua escolha a partir dos seguintes passos:

Em um primeiro terminal:

```bash
cd tcp
python servidor_tcp.py
```

- Troque **tcp** por **udp** para utilizar o sevidor UDP 

Então em outro teminal:

```bash
cd tcp
python cliente_tcp.py
```

- Troque **tcp** por **udp** para usar o cliente UDP

**OBS**: Verifique se você está no diretório correto, **VALIDADOR-DE-CPF**, antes de executar os comandos

## ⚙ **Funcionamento** 

1. **Cliente TCP/UDP**: O cliente solicita que o usuário digite um CPF e envia esse CPF para o servidor.
2. **Servidor TCP/UDP**: O servidor recebe o CPF enviado pelo cliente e valida sua estrutura, utilizando o algoritimo para a validação do CPF.
3. **Resposta**: O servidor envia a resposta ao cliente, que exibe se o CPF é **válido** ou **inválido**.

## ⚒ **Tecnologias Utilizadas** 

- **Python 3.x**: Linguagem de programação utilizada para a implementação.
- **Sockets TCP/UDP**: Usados para a comunicação entre cliente e servidor.