import requests

request_data = {
    "name": "morpheus",
    "job": "leader"
}
response = requests.post("https://reqres.in/api/users",data=request_data)
print(response.json())