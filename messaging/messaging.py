#ssign sender and receiver, X represents the digits of the phone number

from smtplib import SMTP
sender = 'jagswe2024@gmail.com'

receiver = '3175127809@vtext.com'

#Next we create the message:

header = 'To: ' + receiver + '\n' + 'From: ' + sender

body = 'person detected'

signature = '- Sent From BBB'

#Load the gmail server and port into the class “mail”

mail = SMTP('smtp.gmail.com',587)

#run a subroutine with your email login and password for your gmail.


def sendText():
    mail.ehlo()
    mail.starttls()
    mail.ehlo()
    mail.login('jagswe2024@gmail.com', 'vofl sdfh pdjq kidt')
    mail.sendmail(sender, receiver, '\n\n' + body + '\n\n' + signature)
    mail.close()
sendText()
