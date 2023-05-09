import re

with open("server.log", "r") as f:
    for line in f:
        match = re.match(r'(\S+) (\S+) (\S+) \[(.*?)\] "(.*?)" (\S+) (\S+) "(.*?)" "(.*?)"', line)
        if match is not None:
            ip_address = match.group(1)
            date_time = match.group(4)
            request_type, url, http_version = match.group(5).split()
            response_code = match.group(6)
            user_agent = match.group(9)

            # Do something with the extracted information
            print(f'{date_time} {ip_address} {request_type} {url} {response_code} {user_agent}')

