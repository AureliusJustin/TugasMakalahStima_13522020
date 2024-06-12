import os

def readInput(path):
    # Validasi File
    if(os.path.isfile(path)):
        try:
            with open(path) as file:
                lines = []
                for line in file:
                    lines.append(line.rstrip())
        except IOError as e:
            print("File tidak berhasil dibuka!")
            exit()
    else:
        print(path, "Tidak ditemukan! Cek nama file")
        exit()

    # Proses File
    matrix = []
    try:
        for line in lines:
            temp = []
            for char in line:
                temp.append(char)
            matrix.append(temp)
    except:
        print("Isi file tidak valid!")
        exit()

    return matrix