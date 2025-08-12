import requests

#response = requests.get("https://reqres.in/api/users?page=2")
p={"page":2}
response = requests.get("https://reqres.in/api/users",params=p,timeout=1)

json_response = response.json()
response_code = response.status_code
assert response_code == 200,"Code doesnt match"

print(json_response['total'])
assert json_response['total'] == 12
assert json_response['total_pages'] == 2
assert (json_response['data'][0]['email']).endswith('regres.in'), "email format not matching"
assert json_response['data'][2]['last_name'] != None


print(response.text)

print(response.content)

print(response.json())

print(response.headers)

print(response.encoding)
print(response)
print(type(response))
print(dir(response))

