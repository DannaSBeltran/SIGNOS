import re
import json


pattern = (
    r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[(\d{1,2}\/\w{1,3}\/\d{1,4}:\d{1,2}:\d{1,2}:\d{1,2}) \+\d{1,4}\] "(GET|POST|PUT|DELETE|HEAD|OPTIONS|PATCH) (.*?) HTTP\/\d\.\d" (\d{3}) (\d+) "(.*?)" "(.*?)"')

with open('apache_logs.txt', 'r') as lines:
    jsonExtract = []
    for line in lines:
        values = re.finditer(pattern, line)
        for match in values:
            jsonData = {
                "IP": match.group(1),  
                "date": match.group(2),
                "Method": match.group(3),
                "URL": match.group(4),
                "status": match.group(5),
                "size": match.group(6),
                "referer": match.group(7),
                "nav": match.group(8)
            }
            jsonExtract.append(jsonData)

    print(json.dumps(jsonExtract, indent=4))
































