import requests
import time

def show_scanner(url):

    try:
        scanner_response = {}
        start_time = time.time()
        response_fetcher = requests.get(url, timeout=5)
        end_time = time.time()
        response_time = end_time - start_time

        response_bringer = ("Status", "Headers", "Body", "URL", "Time")
        scanner_response.update({
           "Status" : response_fetcher.status_code,
            "Headers" : response_fetcher.headers,
            "Body" : response_fetcher.text,
            "URL" : url,
            "Time" : f"{response_time:.3f}s"
        })

    except Exception as e:
        print("ERROR OCCURE!", e)        

    return scanner_response

