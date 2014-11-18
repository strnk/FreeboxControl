class NetworkError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class FreeboxError(Exception):
    _data = None
    
    def __init__(self, value, data):
        self.value = value
        self._data = data
        print self.value

    def __str__(self):
        return repr(self.value)
    
    def data(self):
        return self._data


class AppTokenError(Exception):
    appTokenUnknown = 'The app_token is invalid or has been revoked'
    appTokenTimeout = 'The user did not confirmed the authorization within the given time'
    appTokenDenied = 'The user denied the authorization request'

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
