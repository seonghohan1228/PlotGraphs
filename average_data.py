
def average_data(data):
    x = len(data)
    y = len(data[0])
    for i in range(int(x/3)):
        for j in range(y):
            if (data[3*i][j] != 0) or (data[3*i+1][j] != 0) or (data[3*i+2][j] != 0):
                avg = (data[3*i][j] + data[3*i+1][j] + data[3*i+2][j])/3.0
                data[3*i][j] = avg
                data[3*i+1][j] = avg
                data[3*i+2][j] = avg
    return data
