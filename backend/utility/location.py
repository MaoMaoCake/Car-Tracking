def get_locations(device_id):
    """
    This function returns a list of all the logged locations for a device
    The function will return a json sorted by timestamp
    """
    if device_id == None:
        return None
    elif device_id == "share_tracker_1":
        return {'location': [{'latitude': '13.732571', 'longitude': '100.509177', 'timestamp': '1469441845'},
                             {'latitude': '13.732571', 'longitude': '100.510177', 'timestamp': '1469451845'}]}
    elif device_id == "share_tracker_2":
        return {'location': [{'latitude': '13.732571', 'longitude': '100.511177', 'timestamp': '1469451845'},
                             {'latitude': '13.732571', 'longitude': '100.512177', 'timestamp': '1469451845'},
                             {'latitude': '13.732571', 'longitude': '100.513177', 'timestamp': '1469451845'}]}