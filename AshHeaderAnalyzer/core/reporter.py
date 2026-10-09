def show_reporter(url, scanner_response, parser_response, general_headers, security_headers, cookie_info, obser_response):

   gen_message = ["Server", "Content-Type", "Content-Length", "Location"]
   sec_message = ["Strict-Transport-Security", "Content-Security-Policy", "X-Frame-Options", "X-Content-Type-Options", "Referrer-Policy", "Permissions-Policy"]
   cookie_message = ["Set-Cookie"]   
   try: 
    print("")
    print("Target URL".ljust(19),":",url)
    print("Final URL".ljust(19),":",scanner_response.get("URL"))
    print("Status Code".ljust(19),":",scanner_response.get("Status"))
    print("")
    print("GENERAL HEADERS")
    print("_"*130)
    print("")
    for loop1 in gen_message:
      final_gen_response = general_headers.get(loop1)
      print(loop1.ljust(19),":",final_gen_response)
    print("")  
    print("SECURITY HEADERS")
    print("_"*130)
    print("")
    for loop2 in sec_message:
       if loop2 in security_headers:
          print(loop2.ljust(19),":","Present")
       else:
          print(loop2.ljust(19),":","DENY")
    print("")
    print("COOKIE")
    print("_"*130)
    print("")
    for loop3 in cookie_info:
       if loop3 in cookie_info:
          print(loop3.ljust(19),":","Detected")
       else:
          print(loop3.ljust(19),":"," Not Detected")          
    print("")
    print("OBSERVATION")
    print("_"*130)
    print("")
    for loop4 in sec_message:
       final_obse_response = obser_response.get(loop4)
       print(final_obse_response)        
    print("")

   except Exception as e:
      print("ERROR OCCURE!", e)    