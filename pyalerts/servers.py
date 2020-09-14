import smtplib

protocols = [
            'smtp.gmail.com',
            'smtp.office365.com',
            'smtp-mail.outlook.com'
        ]

class Server(object):
    def __init__(self, address, password, protocol, port=587, certfile=None):
        """
        An authentication object for email servers.
        """
        self.address = address
        self.password = password
        self.username = address.split('@')[0]
        self.protocol = protocol
        self.port = port
        self.certfile = certfile

        self._server = None

    def authenticate(self, reauth=False):
        """
        Returns a connection to Gmail.
        Two factor-authentication not supported.
        """
        if self._server is None or reauth:
            server = smtplib.SMTP(self.protocol, self.port)
            server.ehlo()
            if self.certfile:
                # Requires a certificate?
                # https://stackoverflow.com/questions/46160886/how-to-send-smtp-email-for-office365-with-python-using-tls-ssl
                server.starttls(certfile=self.certfile)
            else:
                server.starttls()
            server.login(self.address, self.password)
            self._server = server

        return self._server
