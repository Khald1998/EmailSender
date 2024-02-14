# from dotenv import load_dotenv
# import os
# import smtplib
# from email.message import EmailMessage

# # Load environment variables
# load_dotenv()
# email_address = os.getenv('EMAIL_ADDRESS')
# email_password = os.getenv('EMAIL_PASSWORD')
# attachment_path = "CV_Khaled Alzahrani.pdf"  
# content_path = "email_content.txt"  

# def send_email(recipient, subject, content_path, attachment_path):
#     msg = EmailMessage()
#     msg['Subject'] = subject
#     msg['From'] = email_address
#     msg['To'] = recipient
    
#     # Read the content from the file
#     with open(content_path, 'r') as file:
#         body = file.read()
#     msg.set_content(body)
#     print('The conten of the msg\n------------------------------------------------------------------',body,'\n------------------------------------------------------------------')

#     # Attach the PDF if the path is valid
#     if os.path.isfile(attachment_path):
#         print("We found an attachment!")
#         with open(attachment_path, 'rb') as f:
#             file_data = f.read()
#             file_name = os.path.basename(f.name)
#         msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
#     else:
#         print("Attachment file not found.")

#     with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
#         smtp.login(email_address, email_password)
#         smtp.send_message(msg)
#         print("Email sent successfully!")

# def main():
#     while True:
#         print("1. Send an email\n2. Close program")
#         choice = input("Enter your choice: ")
#         if choice == "1":
#             recipient = input("Enter recipient's email: ")
#             subject = "Job Opportunities Inquiry"
#             send_email(recipient, subject, content_path, attachment_path)
#         elif choice == "2":
#             print("Program closed.")
#             break
#         else:
#             print("Invalid choice. Please try again.")

# if __name__ == "__main__":
#     main()








# import sendgrid
# import os
# from sendgrid.helpers.mail import *

# sg = sendgrid.SendGridAPIClient('API KEY HERE')
# from_email = Email("me@khaledz.dev")
# to_email = To("arraaa1999@gmail.com")
# subject = "Sending with SendGrid is Fun"
# content = Content("text/plain", "and easy to do anywhere, even with Python")
# mail = Mail(from_email, to_email, subject, content)
# response = sg.client.mail.send.post(request_body=mail.get())
# print(response.status_code)
# print(response.body)
# print(response.headers)
