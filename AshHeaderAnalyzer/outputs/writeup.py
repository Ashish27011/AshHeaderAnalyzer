def show_writeup(url, scanner_response, parser_response, general_headers, security_headers, cookie_info, obser_response):

   gen_message = ["Server", "Content-Type", "Content-Length", "Location"]
   sec_message = ["Strict-Transport-Security", "Content-Security-Policy", "X-Frame-Options", "X-Content-Type-Options", "Referrer-Policy", "Permissions-Policy"]
   cookie_message = ["Set-Cookie"]   
   try: 
    with open("AshHeaderAnalyzer/outputs/report.txt", "w", encoding="utf-8") as file:
     file.write("\n")
     file.write("Target URL".ljust(19) + " : " + str(url) + "\n")
     file.write("Final URL".ljust(19) + " : " + str(scanner_response.get("URL")) + "\n")
     file.write("Status Code".ljust(19) + " : " + str(scanner_response.get("Status")) + "\n")
     file.write("\n")
     file.write("GENERAL HEADERS\n")
     file.write("_"*130 + "\n")
     file.write("\n")
     for loop1 in gen_message:
       final_gen_response = general_headers.get(loop1)
       file.write(loop1.ljust(19) + " : " + str(final_gen_response) + "\n")
     file.write("\n")
     file.write("SECURITY HEADERS\n")
     file.write("_"*130 + "\n")
     file.write("\n")
     for loop2 in sec_message:
        if loop2 in security_headers:
           file.write(loop2.ljust(19) + " : " + "Present" + "\n")
        else:
           file.write(loop2.ljust(19) + " : " + "DENY" + "\n")
     file.write("\n")
     file.write("COOKIE\n")
     file.write("_"*130 + "\n")
     file.write("\n")
     for loop3 in cookie_message:
        if loop3 in cookie_info:
           file.write(loop3.ljust(19) + " : " + "Detected" + "\n")
        else:
           file.write(loop3.ljust(19) + " : " + "Not Detected" + "\n")          
     file.write("\n")
     file.write("OBSERVATION\n")
     file.write("_"*130 + "\n")
     file.write("\n")
     for loop4 in sec_message:
        final_obse_response = obser_response.get(loop4)
        file.write(str(final_obse_response) + "\n")        
     file.write("\n")

   except Exception as e:
      print("ERROR OCCURE!", e)