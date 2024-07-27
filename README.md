# AutomateWithPython
AutomateWithPython is a collection of Python scripts designed to simplify and automate everyday tasks. From email management and data processing to file organization and web scraping, these scripts help reduce manual effort and enhance productivity. Discover efficient solutions for a smoother workflow.


This Python script connects to your Gmail account and deletes emails from specified domains. Utilizing the IMAPClient and pyzmail libraries, it securely logs into your email, searches for messages from unwanted domains, and deletes them. This helps in automatically cleaning up your inbox by removing spam or unwanted emails based on the specified criteria.


Key Features:
Secure Login: Uses IMAP over SSL for secure authentication.
Domain-Based Filtering: Searches for emails from specified domains.
Automated Deletion: Deletes the found emails and permanently removes them from the mailbox.

Requirements:
You need to download these two libraries:
pip install imapclient
pip install pyzmail36

Note:
Replace the gmail address with your own gmail. 
Password is not your Gmail password. 


For the App password, You have to create one by following the steps:
  Go to your Google Account: https://myaccount.google.com/
  Navigate to "Security".
  Search for App password.
  Give a name and you will get a password with 16 letters in this format : xxxx xxxx xxxx xxxx. 
  Copy that.


Caution:
This python script deletes all the emails permanently.So Make sure that you haven't added any important ones.
