import smtplib


class Server(object):
    def __init__(self, address, password, etype='gmail'):
        """
        An authentication object for email servers.
        """
        self.address = address
        self.password = password
        self.username = address.split('@')[0]

        if etype == 'gmail':
            self.authenticate = self.gmail_authentication
        else:
            raise(ValueError)

    def gmail_authentication(self):
        """
        Returns a connection to Gmail.
        Two factor-authentication not supported.
        """
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(address, password)
        self._gmail_authentication = server

        return self._gmail_authentication