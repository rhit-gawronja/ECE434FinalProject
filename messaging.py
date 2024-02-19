#ssign sender and receiver, X represents the digits of the phone number
from email.message import EmailMessage
import smtplib
import imghdr
from smtplib import SMTP
sender = 'jagswe2024@gmail.com'

receiver = '7084762211@vtext.com'

#Next we create the message:

header = 'To: ' + receiver + '\n' + 'From: ' + sender

body = 'person detected'

signature = '- Sent From BBB'
def sendText():
    # mail.ehlo()
    # mail.starttls()
    # mail.ehlo()
    # mail.login('jagswe2024@gmail.com', 'vofl sdfh pdjq kidt')
    # mail.sendmail(sender, receiver, '\n\n' + body + '\n\n' + signature)
    # mail.close()
#Load the gmail server and port into the class “mail”

    mail = SMTP('smtp.gmail.com',587)

#run a subroutine with your email login and password for your gmail.
    newMessage = EmailMessage()                         
    newMessage['Subject'] = "Check out the new logo" 
    newMessage['From'] =  sender                  
    newMessage['To'] = receiver
    newMessage.set_content('person Detected in the area') 

    with open('newbox.png', 'rb') as f:
        image_data = f.read()
        image_type = imghdr.what(f.name)
        image_name = f.name

    newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    
        smtp.login(sender, 'vofl sdfh pdjq kidt')              
        smtp.send_message(newMessage)


