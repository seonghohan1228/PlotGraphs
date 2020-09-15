from datetime import datetime


# Selects timestamps in dataset data and converts to datetime object
def get_time(data):
    timestamp = data[:, 7] #10 for MEPD_SCI, 7 for HEPD_DIV
    date_time = [datetime.fromtimestamp(t) for t in timestamp]

    return date_time
