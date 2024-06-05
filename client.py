# Created by: Dede Brahma Arianto S.Kom., M.Kom

# import library socket
import socket

# membuat fungsi client
def client_program():
    # menentukan alamat server
    server_address = ('localhost',4999)

    # memanggil fungsi library socket
    client_socket = socket.socket()

    # melakukan koneksi ke server
    client_socket.connect(server_address)

    # mengirim pesan ke server
    message = input(" -> ")

    # membuat perulangan pesan
    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())

        # menerima respon dari server
        data = client_socket.recv(1024).decode()  # receive response

        # menampilkan pesan dari server
        print('Received from server: ' + data)

        # mengirim pesan ke server
        message = input(" -> ")

    # menutup koneksi
    client_socket.close()


if __name__ == '__main__':
    client_program()