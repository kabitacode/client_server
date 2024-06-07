import socket

if __name__ == '__main__':
    host = '127.0.0.1'
    port = 8101

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))

    filename = input('Input nama file : ')
    try:
        with open(filename, "r") as fi:
            data = fi.read()
            while data:
                sock.send(str(data).encode())
                data = fi.read()
            print('File berhasil dikirim!')
    except IOError:
        print('nama file salah!')

    sock.close()
