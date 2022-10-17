from recaptchav3py.constants import CONSTANTS
import requests
import re


class RecaptchaV3Solver:
    """ Google Recaptcha V3 solver class """

    def __init__(self, anchor_url: str = None):
        """
        Google Recaptcha V3 solver

        :param anchor_url: Anchor URL for Google Recaptcha V3 captured in the network tab (Use one for higher accuracy)
        """

        self.anchor_url = anchor_url

        if self.anchor_url is None:
            self.anchor_url = CONSTANTS.ANCHOR_URL

    def solve(self) -> str:
        """
        :return: Returns token from solving Google Recaptcha V3
        """

        query_params = self.anchor_url.split('api2/anchor?')[1]

        content_headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        base_uri = f'https://www.google.com/recaptcha/api2'

        anchor_response = requests.get(
            url=f'{base_uri}/anchor',
            params=query_params,
            headers=content_headers,
        )

        token = re.findall(r'"recaptcha-token" value="(.*?)"', anchor_response.text)

        k, co, v = dict(
            qp.split('=') for qp in query_params.split('&') if qp.split('=')[0] in {'k', 'v', 'co'}  # type: ignore
        ).values()

        reload_payload = {
            'k': k,
            'co': co,
            'v': v,
            'c': token,
            'reason': 'q',
        }

        reload_response = requests.post(
            f'{base_uri}/reload',
            params={'k': k},
            data=reload_payload,
            headers=content_headers,
        ).text

        recaptcha_token = re.findall(r'"rresp","(.*?)"', reload_response)[0]

        return recaptcha_token
