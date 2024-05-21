import requests
import constant
# re = requests.post(
#     "https://discord.com/api/v10/oauth2/token",
#     data={
#         "grant_type": "client_credentials",
#         "scope": "applications.commands.update"
#     },
#     headers={"Content-Type": "application/x-www-form-urlencoded"},
#     auth=(constant.clientid,constant.secret)
# )
# print(re.json())

re = requests.get(
    "https://discord.com/api/v10/users/@me/guilds",
    headers={"Authorization": "Bot MTE4MDcxNTgyNzIwOTcxMTY0Ng.Gl7w_P.ROpcK3RzaU2kH7Qdut3M5vZHEgAHPOr7g2keqI"}
)
print(re.json())