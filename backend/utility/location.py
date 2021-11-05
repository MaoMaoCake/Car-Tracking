def get_locations(device_id):
    """
    This function returns a list of all the logged locations for a device
    The function will return a json sorted by timestamp
    """
    return {'location': [{'latitude': '-37.814199', 'longitude': '144.96328', 'timestamp': '1469441845'},
                        {'latitude': '-37.814199', 'longitude': '144.96328', 'timestamp': '1469451845'}]}