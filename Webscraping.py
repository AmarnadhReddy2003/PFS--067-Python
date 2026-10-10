# Web Scraping: It is the process of automaticaaly collectiong information from websites using aprogram.
# Where we can use web scraping? 
# 1.Extracting article headlines
# 2. Collecting products data
# 3. Gather job listings
# 4. Collecting publicly availalble research data.

# 2. Request Module
# The request library allows python to send HTTP requests to websites and receive thier responses.

# # Sending a request to website
# import requests
# url= 'https://www.linkedin.com/feed/'
# response=requests.get(url)
# print(response.status_code)
# print(response.text)

# Status Codes
# 200 - Request Sucessfull
# 201 - Created 
# 301 - Redirecting
# 403 - Access fordiden
# 404 - Page not found
# 500 - Sever Error
 
# # Add Basic error Handling
# import requests
# url= 'https://www.linkedin.com/feed/'
# try:
#     response=requests.get(url,timeout=10)
#     response.raise_for_status()
#     print(response.text)
#     print(response.status_code)
# except requests.RequestException as error:
#     print('Request Failed: ',error)


    
# # BeautifulSoup: Requests download the HTML, but we need a convenient way to find a particular elements inside it. That's where Beautifulsoup helps.
# from bs4 import BeautifulSoup
# html =""" 
# <html>
# <head>
# <title>My First Website</title>
# </head>
# <body>
#     <h1>Welcome to Python</h1>
#     <p>Learn Web Scraping</p>
# </body>
# </html>    
# """ 
# soup=BeautifulSoup(html,'html.parser') # Here BeautifulSoup is a HTML parser,where we can access individual elements in HTML
# print(soup.title)
# print(soup.title.get_text()) # Here get_text() is a built in module which helps us to access the text we specified in it.
# print(soup.h1.get_text())
# print(soup.p.get_text())

# # Import BeautifulSoup Methods
# # 1. find() - Finds the first matching element 
# soup.find('p')
# # 2. find_all() - Finds all matching elements 
# soup.find_all('p')
# # 3. get_text() - Extract Text
# # 4. get() - Extracts an attribute
# # link=soup.find('a')
# # print(link.get('href'))


# # Extracting Website Data
# import requests
# from bs4 import BeautifulSoup
# url='https://www.linkedin.com/feed/'
# response=requests.get(url,timeout=10)
# response.raise_for_status()
# soup=BeautifulSoup(response.text,'html.parser')
# title=soup.title.get_text(strip=True)
# heading=soup.find('h1').get_text(strip=True)
# print('Page Title: ',title)
# print('Hading: ',heading)

# # Extracting the links
# import requests
# from bs4 import BeautifulSoup
# url='https://www.linkedin.com/feed/'
# response=requests.get(url,timeout=10)
# response.raise_for_status()
# soup=BeautifulSoup(response.text,'html.parser')
# links=soup.find_all('a')
# for link in links:
#     text=link.get_text(strip=True)
#     url=link.get_text('href')
#     print('Link Text:',text)
#     print('URL',url)

# # Email Automation
# import smtplib
# from email.message import EmailMessage
# # EmailMessage() - Creates an email message
# sender='amaranadhareddythallapureddy@gamil.com'
# password="zqjq qxdc dcvt ifaz"
# receiver="amarnadh84650@gamil.com"

# msg=EmailMessage()
# msg['Subject']="Preparation Email"
# msg['From']=sender
# msg['To']=receiver
# msg.set_content('Hello. This is a preparation email using python')
# file_path=r'D:\Documentation'
# with open(file_path,'rb')as file:
#     file_data=file.read()
# msg.add_attachment(
#     file_data,
#     maintype='application',
#     sutype='pdf',
#     filename='Email Inbox'
# )
# with smtplib.SMTP_SSL('smtp.gmail.com',465) as server:
# # SMTP_SSL - Connects to Gmail's SMTP srver using port 465
#     server.login(sender,password)
#     # login() - log in your mail and app data
#     server.send_message(msg)
#     # send_message=sends the email
# print('Email Sent Sucessfully')


# Virtual Assistant Program
import datetime
import webbrowser

print("Hello!, I'm your virtual assistant.")
while True:
    command=input("\n How may I help you? ").lower()

    if "hello" in command or 'hi' in command:
        print("Hello Amar! how are you")

    elif "time" in command:
        time=datetime.datetime.now().strftime("%I:%M %p")
        print("current time is:",time)
    elif "date" in command:
        date=datetime.datetime.now().strftime("%d-%m-%Y")
        print("Today's date is:",date)
    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        print("opening Google...")
    elif "your name" in command:
        print("iam your python vitrtual Assistant ")
    elif "exit" in command or "bye" in command:
        print("Good bye! Have a nice day")
        break
    else:
        print("Sorry, I don't understand that command")
