from get_time import get_time


# Selects Detector 0 ~ 3 data from given data
def detector(data):
    detector_data = [[], [], [], []]
    for i in range(len(detector_data)):
        detector_data[i] = data[:, 13 + 68*i:77 + 68*i]

    return detector_data

