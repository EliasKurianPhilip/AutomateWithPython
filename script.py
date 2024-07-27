import imapclient
import pyzmail

# Your Gmail credentials
EMAIL = 'abcd9@gmail.com'
PASSWORD = 'xxxx xxxx xxxx xxxx'  # Use an App Password if you have 2FA enabled

# Domains to delete emails from
UNWANTED_DOMAINS = ['flipkart.com', 'notification@priority.facebookmail.com', 'no-reply@accounts.google.com']

def delete_unwanted_emails():
    with imapclient.IMAPClient('imap.gmail.com', ssl=True) as client:
        client.login(EMAIL, PASSWORD)
        client.select_folder('INBOX')

        for domain in UNWANTED_DOMAINS:
            # Search for emails from the specified domain
            messages = client.search(['FROM', f'@{domain}'])

            if not messages:
                print(f'No unwanted emails found from {domain}.')
                continue

            # Delete each message
            for uid in messages:
                client.delete_messages(uid)
                print(f'Deleted email with UID: {uid} from domain: {domain}')

        client.expunge()  # Permanently remove the deleted emails from the mailbox

if __name__ == '__main__':
    delete_unwanted_emails()
