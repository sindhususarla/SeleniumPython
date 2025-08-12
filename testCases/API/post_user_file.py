import requests
import json

token_request_body = {

}
token = requests.post("https://reqres.in/api/users/token",data=token_request_body)
valid_token = token.json()["access_token"]

request_body = open("data.json", "r").read()

headers = {
    "x-api-key": "reqres-free-v1",
    "Content-Type": "application/json"
}
response = requests.post(
    "https://reqres.in/api/users",
    data=request_body,
    headers=headers
)
print(response.json())
assert response.status_code == 201, "Status code does not match"
assert response.json()["job"] == "leader", "Data does not match"
assert response.headers["Content-Type"] == "application/json"
