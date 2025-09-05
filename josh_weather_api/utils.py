from requests import Response


class StatusCodeException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def check_status_code(resp: Response):
    if resp.status_code != 200:
        raise StatusCodeException(f"Received unexpected status from {resp.request.url}, status was {resp.status_code}")
