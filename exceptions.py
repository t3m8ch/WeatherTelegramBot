class CityNotFoundError(Exception):
    pass


class ServerError(Exception):
    pass


class OWMApiKeyIsNotCorrectError(ServerError):
    pass

