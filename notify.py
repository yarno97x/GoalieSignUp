import smtplib
from email.message import EmailMessage
from data import mock
from parser import htmlparser

email_address = 'yarnogrenier@gmail.com'
email_password = 'bdda njwx izjq dzuk'  # Use your App Password

def notify(games, testing = True) :
    msg = EmailMessage()
    msg['Subject'] = "New Upcoming Games"
    msg['From'] = email_address
    msg['To'] = 'mikacrevier@hotmail.com' if not testing else "yarno@hotmail.ca"
    content = 'Your games this week:\n' + "\n".join([str(game) for game in games])
    msg.set_content(content)  # fallback
    alt = f"""
        <html>
        <body style='background-color: skyblue'>
            {"".join([game.to_html() for game in games])}
            <b>MAKE SURE TO CONFIRM ATTENDANCE</b>
        </body>
        </html>
        """
    msg.add_alternative(alt, subtype='html')
    print(alt)

    # Connect and send
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_address, email_password)
        smtp.send_message(msg)

    print("Email sent!")

if __name__ == "__main__" :
    games = htmlparser(mock)
    notify(games)


