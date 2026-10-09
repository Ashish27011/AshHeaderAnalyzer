from urllib.parse import urlparse

def show_validator():

  while True:
    try:

        url = input("Enter URL : ")
        validate_url = urlparse(url)
        response = True

        if validate_url.scheme not in ["http", "https"]:
            print("URL MUST CONTAIN SCHEMA! : http or https")
            response = False
        if not validate_url.hostname:
            print("ULR MUST CONTAIN DOMAIN NAME!")   
            response = False
        else:
           break

    except Exception as e:
       print("ERROR OCCURE!", e)       
                   
  return url  