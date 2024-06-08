import socket

def receive_file(conn, addr):
    filename = 'received_file.txt'
    with open(filename, 'wb') as f:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            f.write(data)
    print(f'File diterima from {addr}')
    print(f'disimpan dengan nama {filename}')

if __name__ == '__main__':
    host = '127.0.0.1'
    port = 8101

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print('Loading...')

    conn, addr = server_socket.accept()
    print(f'koneksi oleh {addr}')
    receive_file(conn, addr)
    
    conn.close()
    server_socket.close()
