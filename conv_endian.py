def conv_endian(data):
    data = list(data)

    for i in range(len(data)//2):
        data[i*2], data[i*2+1] = data[i*2+1], data[i*2]

    return bytes(data)
