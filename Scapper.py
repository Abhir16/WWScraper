
# Scrapper.py
# by Abhishek Ravi
#
# file will go to UW Works website and scrape key components needed by master file
# it will be sent user id and password to enter in
#



from lxml import html
import requests
import urllib


# #This will create a list of buyers:
# buyers = tree.xpath('//div[@title="buyer-name"]/text()')
# #This will create a list of prices

# prices = tree.xpath('//span[@style="font-size:12px;"]/text()')
page = ""

with requests.Session() as c:
    url = 'https://cas.uwaterloo.ca/cas/login?service=https://waterlooworks.uwaterloo.ca/waterloo.htm'
    # url = 'https://waterlooworks.uwaterloo.ca/myAccount/co-op/interviews-co-op.htm' # for interview section
    # TYPE IN USERNAME AND PASSWORD MUST FIND WAY TO ENCRYPT THIS FOR SECURITY
    print("Enter username: ")
    USERNAME = input()
    print("Enter password: ")
    PASSWORD = input()

    #now find all active applications
    c.get(url)
    login_data = dict(username=USERNAME, password=PASSWORD, lt="e1s1", _eventId="submit", submit="LOGIN")
    c.post(url, data=login_data, headers={"Referer": "https://waterlooworks.uwaterloo.ca/myAccount/dashboard.htm"})
    appPage = c.get(url)
    print("logged in: ", appPage.content)
    appPage = c.get("https://waterlooworks.uwaterloo.ca/myAccount/co-op/coop-postings.htm")
    print("apps page: ", appPage.content)
#     replicate post now

    active_apps_headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                           "Accept-Encoding": "gzip, deflate, br",
                           "Accept-Language": "en-US,en;q=0.8",
                           "Cache-Control": "max-age=0",
                           "Connection": "keep-alive",
                           "Content-Length": "415",
                           "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundarycfVdpBnNEEhc4H4N",
                           # "Cookie": "__utma=131842571.1917778921.1443572359.1443577856.1443581132.2; __gads=ID=25c58eaf244b1dce:T=1455083717:S=ALNI_MbI7g5lYFyXQLVqI0XJMDIiZ23Fqg; BIGipServerCECA_443.app~CECA_443_pool=rd2o00000000000000000000ffffac108938o23118; _ga=GA1.2.1917778921.1443572359; JSESSIONID=15771C03B7438A33AA9FE0E86D03159D",
                           "Host": "waterlooworks.uwaterloo.ca",
                           "Origin": "https://waterlooworks.uwaterloo.ca",
                           "Referer": "https://waterlooworks.uwaterloo.ca/myAccount/co-op/coop-postings.htm",
                           "Upgrade-Insecure-Requests": "1",
                           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}
    print(c.cookies.get_dict())
    login_data["action"] = "_-_-10fUElHSF4B5ldojehlr3c3GbApHLjMWVOmE91T5eYhvq8lpVqGvmsyAThhQoY9GQC5cgL5gWZ96KZRF-9ZY7HQjJo8jUBzsg9Z_NajkchSlCYREK0x3mHx5e6RYg9g2_3Tp4qlue5Heuu382rrBWSCszL41dW5SHCXqU8hQLOPXSxXWJg"
    c.post("https://waterlooworks.uwaterloo.ca/myAccount/co-op/coop-postings.htm", data=login_data, headers=active_apps_headers)
    appPage = c.get("https://waterlooworks.uwaterloo.ca/myAccount/co-op/coop-postings.htm")
    print("apps page: ", appPage.content)
    print(c.cookies.get_dict())


tree = html.fromstring(appPage.content)
prices = tree.xpath('//tr')
# find_text = tree.xpath("//text()")

print(prices)
# it seems that the site submits a key value when the button is clicked
a = "_-_-10fUElHSF4B5ldojehlr3c3GbApHLjMWVOmE91T5eYhvq8lpVqGvmsyAThhQoY9GQC5cgL5gWZ96KZRF-9ZY7HQjJo8jUBzsg9Z_NajkchSlCYREK0x3mHx5e6RYg9g2_3Tp4qlue5Heuu382rrBWSCszL41dW5SHCXqU8hQLOPXSxXWJg"
b = "_-_-10fUElHSF4B5ldojehlr3c3GbApHLjMWVOmE91T5eYhvq8lpVqGvmsyAThhQoY9GQC5cgL5gWZ96KZRF-9ZY7HQjJo8jUBzsg9Z_NajkchSlCYREK0x3mHx5e6RYg9g2_3Tp4qlue5Heuu382rrBWSCszL41dW5SHCXqU8hQLOPXSxXWJg"

if a == b:
    print("same")