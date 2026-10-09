def show_parser(scanner_response):
    message = ["Server", "Content-Type", "Content-Length", "Location", "Strict-Transport-Security", "Content-Security-Policy", "X-Frame-Options", "X-Content-Type-Options", "Referrer-Policy", "Permissions-Policy", "Set-Cookie"]

    try: 
     parser_response = {}
     for messages in message:
        Headers = scanner_response.get("Headers", "Not Present")
        if messages in Headers:
         final_response = Headers.get(messages, "NOT DETECTED")
         parser_response[messages] = f"{final_response}"      


    except Exception as e:
       print("Error Ocuure!", e)   

    return parser_response   
