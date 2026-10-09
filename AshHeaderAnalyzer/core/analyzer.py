def show_analyzer(parser_response):

   try:


    general_headers = {}
    security_headers = {}
    cookie_info = {}
    obser_response = {}
    gen_message = ["Server", "Content-Type", "Content-Length", "Location"]
    sec_message = ["Strict-Transport-Security", "Content-Security-Policy", "X-Frame-Options", "X-Content-Type-Options", "Referrer-Policy", "Permissions-Policy"]
    cookie_message = ["Set-Cookie"]
    all_list = {
        "general_headers" : gen_message,
        "security_headers" : sec_message,
        "cookie_info" : cookie_message
    }
    result = {
    "general_headers" : general_headers,
    "security_headers" : security_headers,
    "cookie_info" : cookie_info
    }

    for key , value in all_list.items():
        for loop in value: 
         if loop in parser_response:
          final_response = parser_response.get(loop, "Not Present")
          result[key][loop] = f"{final_response}" 

    for loop3 in sec_message:
      if loop3 in parser_response:
         obser_response[loop3] = f"[+] {loop3} detected" 
      else:
         obser_response[loop3] = f"[!] {loop3} not detected"              

   except Exception as e:
      print("ERROR OCCURE!", e)

   return general_headers, security_headers, cookie_info, obser_response