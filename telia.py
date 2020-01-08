import requests

class TeliaAPI():

    def __init__(self, username, password, user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0"):
        self.username = username
        self.password = password

        self.session = requests.Session()
        self.session.headers.update({"User-Agent": user_agent})

        self.auth = self.do_auth().json()

    def do_auth(self):
        url = "https://min-side.telia.no/re/api/mssa-proxy/no/rs/auth/basic"

        data = {
            "Username": self.username,
            "Password": self.password,
        }

        return self.do_request(url, data=data)

    def get_balance(self):
        url = "https://min-side.telia.no/re/api/mssa-proxy/no/rs/messaging/sms/balance"

        return self.do_request(url)

    def send_sms(self, message, contacts, save=True):
        url = "https://min-side.telia.no/re/api/mssa-proxy/no/rs/messaging/sms/send"

        data = {
            "Message": message,
            "Contacts": contacts,
            "Save": save,
        }

        return self.do_request(url, data=data)

    def do_request(self, url, data=None, headers={}, auth=False):
        if data:
            return self.session.post(url, headers=headers, json=data)
        else:
            return self.session.get(url, headers=headers)
