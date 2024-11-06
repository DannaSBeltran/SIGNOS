import re,json

pattern = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[(\d{1,2}\/\w{1,3}\/\d{1,4}):(\d{1,2}:\d{1,2}:\d{1,2}) \+\d{1,4}\] \"(GET|POST|PUT|DELETE|PATCH|HEAD|OPTIONS) (.*)\?(.*) HTTP\/\d.\d\" (\d{3,3})" "/http:(.*)'

with open('apache_logs.txt','r') as lines:
    jsonExtract= []
    for line in lines:
        values = re.finditer(pattern,line)
        for match in values:
            jsonData = {"IP": match.group(1),"Date": match.group(2),'Time':match.group(3), "Method":match.group(4),"Path":match.group(5),"Parameters":match.group(6), "errorcode": match.group(7),"muestra":match.group(8)}
            jsonExtract.append(jsonData)
    print(json.dumps(jsonExtract, indent = 4))































