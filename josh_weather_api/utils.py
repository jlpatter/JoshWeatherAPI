from requests import Response


def check_status_code(resp: Response):
    if resp.status_code != 200:
        return (
            f"HTTP Status 500: Received unexpected status from {resp.request.url}, status was {resp.status_code}",
            500,
        )
    return None