from urllib import request, parse

values = {"username":"zhao632@tom.com","password":"cz19831006"}
data = parse.urlencode(values)
res = request.Request("http://www.csdn.net/login",data)
response = request.urlopen(res)
print(response.read())
