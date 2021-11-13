'''
author: Siddharth Jain
email: nahtasiddharth@gmail.com
purpose: Cybrilla Assignment round 1
language: Python

URL Shortener
Use any language / framework you are comfortable to work with :
- Implement a URL shortener service.
- It should pick up any URL
- Convert the URL into a shorter form
- When the user keys in the shorter URL, service should redirect to the original URL
- Expose an API for the service
Note:
--------
- Ensure that the code is as modular as possible.
- Specs are must
- Do not use Google or any other APIs
- Share the GitHub link of the assignment.
'''

import random
import webbrowser

def convertToShortURL(id):
    '''
    converts the id from base 10 into a base 62 (a-z, A-Z, 0-9) number system
    :param id: unique six digit number
    :return: base 62 number equivalent for id as a shorter url
    '''

    # sequence is changed to not to be predictable
    map = "abcdefghijklmnopqrstuvwxyz01234ABCDEFGHIJKLMNOPQRSTUVWXYZ56789"
    shortenURL = ""

    # converting id to base 62
    while(id):
        shortenURL += map[id % 62]
        id //= 62

    return shortenURL

def redirectToURL(shortURL, urlDict):
    '''
    searches key from the given value in the dictionary and opens the url in the new tab of the browser
    :param shortURL: storter url which is stored as a value in the dictionary
    :param urlDict: dictionary to search key(original URL) for the value(shortURL)
    :return: None
    '''

    key = [k for k, v in urlDict.items() if v == shortURL][0]
    webbrowser.open_new_tab(key)

def addURL(urlDict, idList):
    '''
    takes the input for the url to shorten
    generates a random unique 6 digit id corressponding to url
    call method convertToShortURL with id as parameter and stores the return value as value in the dictionary
    :param urlDict: dictionary (of original_url-short_url pair) to update
    :param idList: a list (of id) to update
    :return: None
    '''

    try:
        url = input("Enter a url you want to shorten:\n")
        if url in urlDict:
            print("This url is already shortened! Try again...")
            addURL(urlDict, idList)
    except:
        print("Something went wrong! Try again...")
    
    # generating unique id for the given url
    id = random.randint(100000, 999999)
    while(id in idList):
        id = random.randint(100000, 999999)
    else:
        idList.append(id)

    # converting to shorter url and storing it against the url in the dictionary
    urlDict[url] = convertToShortURL(id)
    print("Short URL:", urlDict[url])


if __name__ == "__main__":
    idList = []
    urlDict = {}

    # addURL is called upon to get url from the user
    addURL(urlDict, idList)

    while True:
        try:
            user_response = input("\nEnter your choice:\n"
                                  "1. Press '1' if you want to shorten another URL\n"
                                  "2. Press '2' if you want to redirect to URL from Short URL\n"
                                  "3. Press any key to exit\n")
        except:
            print("Something went wrong")


        if user_response == '1':
            print("")
            # calling addURL function to add new url and passing parameters to update them
            addURL(urlDict, idList)

        elif user_response == '2':
            user_shortURL = input("\nEnter short URL to redirect to original URL:\n")

            # to check if user entered a value which is not present in the dictionary
            if user_shortURL in urlDict.values():
                redirectToURL(user_shortURL, urlDict)
            else:
                print("Short URL entered is not found against any URL")
            
        else:
            exit()
        