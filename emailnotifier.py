import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailNotifier:

    """
    A class to send email notifications using a SMTP server.

    Attributes
    ----------
    smtp_server : str; the address of the SMTP server.
    smtp_port : int; the port number to use for the SMTP server (standard in SMTP protocol: 587).
    email_user : str; the email address used to send emails.
    email_password : str, the password for the email account.

    Methods
    -------
    send_email(recipient, subject, body) : sends an email to the specified recipient with the given subject and body.

    """

    def __init__ (self, smtp_server, smtp_port, email_user, email_password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.email_user = email_user
        self.email_password = email_password

    def send_email(self, recipient, subject, body):

        alert = MIMEMultipart()
        recipient = recipient
        alert['From'] = self.email_user
        alert['To'] = recipient
        alert['Subject'] = subject
        alert.attach(MIMEText(body, 'plain'))

        try:
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.email_user, self.email_password)
            text = alert.as_string()
            server.sendmail(self.email_user, recipient, text)
            server.quit()
            print(f"Email sent")
        except Exception as e:
            print(f"Error: {e}")

        return None


if __name__ == '__main__':

    condition = True # Specify the condition that will trigger the email alert

    if condition:

        # Parameters

        SMTP_SERVER = 'smtp.gmail.com' # Example for gmail
        SMTP_PORT = 587 # SMTP protocol
        EMAIL_USER = 'your/email/adress/here@gmail.com'
        EMAIL_PASSWORD = 'your/app/password/here' #https://support.google.com/mail/answer/185833?hl=en

        # Email recipient and content

        recipient_email_list = ['recipient1@email.com', 'recipient2@email.com'] # /!\ This method is not suitable for mass emailing
        subject = 'Enter/an/email/subject/here'
        body = 'Enter/an/email/content/here'

        alert = EmailNotifier(SMTP_SERVER, SMTP_PORT, EMAIL_USER, EMAIL_PASSWORD)

        for email in recipient_email_list:
            alert.send_email(email, subject, body)
