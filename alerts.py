from io import BytesIO
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email.mime.base import MIMEBase
from email.encoders import encode_base64


class EmailAlert(object):
    def __init__(self, server, mailto):
        """

        """
        self.server = server

        if isinstance(mailto, list):
            self.mailto = mailto
        else:
            self.mailto = [mailto]

    def send_alert(subject, message, fig=None):
        """

        """
        msg = MIMEMultipart()
        msg['From'] = self.server.address
        msg['To'] = COMMASPACE.join(self.mailto)
        msg['Date'] = formatdate(localtime=True)
        msg['Subject'] = subject

        msg.attach(MIMEText(message))
        
        if fig is not None:
            part = MIMEBase('application', "octet-stream")
            stream_bytes=BytesIO()
            fig.savefig(stream_bytes,format='png')
            stream_bytes.seek(0)
            part.set_payload(stream_bytes.read())
            encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename="%s"' % 'anything.png')
            msg.attach(part)

        mail_server = server.gmail_authentication()

        mail_server.sendmail(self.server.address, self.mailto, msg.as_string())
        mail_server.quit()