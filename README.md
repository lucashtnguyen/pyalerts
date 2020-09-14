# pyalerts
An email based python alert system.

```python

import pyalerts

with open('gmail.cred', 'r') as f:
    password = f.read()

# setup and authenticate a mail server
server = pyalerts.Server('sender@gmail.com', password, 'smtp.gmail.com')

# setup a Matilto class to dispatch emails
mailer = pyalerts.Mailto(server, 'recipient@email.com')

mailer.send_mail(f'My Subject', 'My message',
                 files=['Report.pdf'])
```