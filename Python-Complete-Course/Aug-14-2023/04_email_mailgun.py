import requests


def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandbox53fa112de33540f4936f22e952412733.mailgun.org/messages",
        auth=("api", "<PRIVATE_API_KEY>"),
        data={
            "from": "Mailgun Sandbox <postmaster@sandbox53fa112de33540f4936f22e952412733.mailgun.org>",
            "to": "Anurag <anurag@anurag.com>",
            "subject": "Hello Anurag",
            "text": "Congratulations Anurag, you just sent an email with Mailgun!  You are truly awesome!",
        },
    )
