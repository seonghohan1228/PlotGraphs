from get_time import get_time


# Selects Telescope 0 ~ 2 data from given data
def telescope(data):
    telescope_data = [[], [], []]
    for i in range(len(telescope_data)):
        telescope_data[i] = data[:, 9 + 41*i:49 + 41*i]

    return telescope_data

