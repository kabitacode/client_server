# Created by: Dede Brahma Arianto S.Kom., M.Kom

# import library socket
import socket

# membuat fungsi server
def server_program():
    # menentukan alamat server
    server_address = ('localhost', 4999)

    # memanggil fungsi library socket
    server_socket = socket.socket()

    # binding ke alamat server
    server_socket.bind(server_address)

    # mengatur jumlah antrian koneksi dari client
    server_socket.listen(2)

    # menerima koneksi dari client
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))

    while True:
        # menerima pesan dari client dengan batasan pesan maksimal 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # jika tidak ada pesan lakukan break
            break
        
        # menampilkan pesan dari client
        print("from connected user: " + str(data))

        # merespon pesan dari client
        data = input(' -> ')
        conn.send(data.encode())

    # menutup koneksi
    conn.close()


if __name__ == '__main__':
    server_program()