import smtplib

dhana=smtplib.SMTP('smtp.gmail.com',587)

dhana.starttls()

dhana.login('kohlikane6@gmail.com','dhana@DHANA12')

dhana.sendmail('kohlikane6@gmail.com','dhanaraman779@gmail.com','Hello boy')

print('Mail sent')