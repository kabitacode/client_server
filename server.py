import socket

if __name__ == '__main__':
    host = '127.0.0.1'
    port = 8101
    totalclient = int(input('masukan nomor client => '))

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    sock.listen(totalclient)
    
    connections = []
    print('Loading.....')
    for i in range(totalclient):
        conn, addr = sock.accept()
        connections.append((conn, addr))
        print('Koneksi dengan Client =>', i + 1)

    fileno = 0
    for conn, addr in connections:
        idx = connections.index((conn, addr)) + 1
        data = conn.recv(1024).decode()

        if not data:
            continue

        filename = 'output-file' + str(fileno) + '.txt'
        fileno += 1
        with open(filename, "w") as fo:
            while data:
                fo.write(data)
                data = conn.recv(1024).decode()

        print('\nMenerima File dari client =>', idx)
        print('File berhasil dikirim! nama file =>', filename)

    for conn, _ in connections:
        conn.close()
