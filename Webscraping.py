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

# Import BeautifulSoup Methods
