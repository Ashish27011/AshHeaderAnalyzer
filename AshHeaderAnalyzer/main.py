
from banners import banner
from core import validator
from core import scanner
from core import parser
from core import analyzer
from core import reporter
from outputs import writeup


url = validator.show_validator()
banner.s_banner()
scanner_response = scanner.show_scanner(url)
parser_response = parser.show_parser(scanner_response)
general_headers, security_headers, cookie_info, obser_response = analyzer.show_analyzer(parser_response)
reporter.show_reporter(url, scanner_response, parser_response, general_headers, security_headers, cookie_info, obser_response)
writeup.show_writeup(url, scanner_response, parser_response, general_headers, security_headers, cookie_info, obser_response)
banner.e_banner()