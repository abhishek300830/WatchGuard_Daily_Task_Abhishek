import requests


class Mailgun:
    MAILGUN_API_URL = "https://api.mailgun.net/v3/sandbox53fa112de33540f4936f22e952412733.mailgun.org/messages"
    MAILGUN_API_KEY = "<PRIVATE_API_KEY>"
    FROM_NAME = "Abhishek"
    FROM_EMAIL = "Abhishek@gmail.com"

    @classmethod
    def send_email(cls, to_email, subject, content):
        return requests.post(
            cls.MAILGUN_API_URL,
            auth=("api", cls.MAILGUN_API_KEY),
            data={
                "from": f"{cls.FROM_NAME}<{cls.FROM_EMAIL}>",
                "to": to_email,
                "subject": subject,
                "text": content,
            },
            timeout=1.5,
        )
