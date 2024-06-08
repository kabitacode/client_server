import socket

def send_file(filename, sock):
    with open(filename, 'rb') as f:
        while (data := f.read(1024)):
            sock.sendall(data)
    print('File berhasil dikirim!')

if __name__ == '__main__':
    host = '127.0.0.1'
    port = 8101

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    filename = input('Input nama file: ')
    try:
        send_file(filename, client_socket)
    except FileNotFoundError:
        print('File tidak ditemukan!')

    client_socket.close()
