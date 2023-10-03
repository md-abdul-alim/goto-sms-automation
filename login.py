from requests_oauthlib import OAuth2Session


# Replace these with your own values
client_id = '5c4dbe11-0659-42b0-a94b-76da93843322'
client_secret = 'KpUeGJVjvtltW7MsE0z2AKj2'
redirect_uri = 'https://oauth.pstmn.io/v1/callback'
authorization_base_url = 'https://authentication.logmeininc.com/oauth/authorize'
token_url = 'https://authentication.logmeininc.com/oauth/token'

# # Create an OAuth2Session
# oauth2 = OAuth2Session(client_id, redirect_uri=redirect_uri)

# # Generate the authorization URL
# authorization_url, state = oauth2.authorization_url(authorization_base_url)

# # Redirect the user to the authorization URL
# print("Please go to this URL and authorize the application:", authorization_url)
# authorization_response = input("Enter the full callback URL: ")

# # Fetch the access token
# token = oauth2.fetch_token(token_url, authorization_response=authorization_response, client_secret=client_secret)

# print(token)

from rauth import OAuth2Service

service = OAuth2Service(
            name='foo',
            client_id='5c4dbe11-0659-42b0-a94b-76da93843322',
            client_secret='KpUeGJVjvtltW7MsE0z2AKj2',
            access_token_url="https://authentication.logmeininc.com/oauth/token",
            authorize_url="https://authentication.logmeininc.com/oauth/authorize",
            base_url="https://authentication.logmeininc.com",
        )

session = service.get_auth_session(data={'grant_type': 'authorization_code', 'redirect_uri': redirect_uri})
print(session)

# import requests


# def get_access_token(url, client_id, client_secret):
#     response = requests.post(
#         url,
#         data={"grant_type": "client_credentials"},
#         auth=(client_id, client_secret),
#     )
#     return response.json()["access_token"]


# get_access_token("https://api.example.com/access_token", "abcde", "12345")
