from io import BytesIO
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email.mime.base import MIMEBase
from email.encoders import encode_base64
from email.mime.application import MIMEApplication


class Mailto(object):
    def __init__(self, server, recipients):
        """

        """
        self.server = server

        if isinstance(recipients, list):
            self.recipients = recipients
        else:
            self.recipients = [recipients]

    def send_mail(self, subject, message, figs=None, files=None):
        """

        """
        if not isinstance(files, list) and files:
            files = [files]
        if not isinstance(figs, list) and figs:
            figs = [figs]

        msg = MIMEMultipart()
        msg['From'] = self.server.address
        msg['To'] = COMMASPACE.join(self.recipients)
        msg['Date'] = formatdate(localtime=True)
        msg['Subject'] = subject

        msg.attach(MIMEText(message))
        
        if figs is not None:
            for n, fig in enumerate(figs):
                part = MIMEBase('application', "octet-stream")
                stream_bytes=BytesIO()
                fig.savefig(stream_bytes,format='png')
                stream_bytes.seek(0)
                part.set_payload(stream_bytes.read())
                encode_base64(part)
                part.add_header('Content-Disposition', 'attachment; filename="Figure_{}.png"'.format(n))
                msg.attach(part)

        if files is not None:
            for f in files or []:
                with open(f, "rb") as fil:
                    part = MIMEApplication(
                        fil.read(),
                        Name=basename(f)
                    )

                # After the file is closed
                part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
                msg.attach(part)

        mail_server = self.server.authenticate()
        try:
            mail_server.sendmail(self.server.address, self.recipients, msg.as_string())
        except:
            mail_server = self.server.authenticate(reauth=True)
            mail_server.sendmail(self.server.address, self.recipients, msg.as_string())
        mail_server.quit()