from requests_oauthlib import OAuth2Session

"""
Sample Google OAuth
pip install requests requests_oauthlib
"""

# Credentials you get from registering a new application
client_id = '<the id you get from google>.apps.googleusercontent.com'
client_secret = '<the secret you get from google>'
redirect_uri = 'https://your.registered/callback'
# authorization_code = ""
# access_token = ""


# # OAuth endpoints given in the Google API documentation
authorization_base_url = "https://accounts.google.com/o/oauth2/v2/auth"
token_url = "https://www.googleapis.com/oauth2/v4/token"
scope = [
     "https://www.googleapis.com/auth/userinfo.email",
     "https://www.googleapis.com/auth/userinfo.profile"
     ]


def main():
     #########################
     # 1.Resource Owner(User) 승인
     #########################     
     ## Resource Server(Google) Login
     # url = "https://{resource_server}/?client_id={}&scope={}&redirect_uri={redirect_uri}"
     google = OAuth2Session(client_id, scope=scope, redirect_uri=redirect_uri)

     # Redirect user to Google for authorization
     authorization_url, state = google.authorization_url(authorization_base_url,
          access_type="offline", prompt="select_account")


     #########################
     #  2. Resource Server(Google) 승인
     ##########################
     ## Send Authorization code, client_id, client_secret
     # authorization_url = "https://{resource_server}/token?grant_type=auhorization_code&code={auth_code}&redirect_uri={redirect_uri}&client_id={client_id}&client_secret={client_secret}"
     print('Please go here and authorize,', authorization_url)

     # Get the authorization verifier code from the callback url
     redirect_response = input(r'Paste the full redirect URL here:')


     #########################
     # 3. AccessToken & RefreshToken 발급
     #########################
     ## Delete Authorization code(생략)
     # Fetch the Access token
     google.fetch_token(token_url, client_secret=client_secret, authorization_response=redirect_response)

     #########################
     # 4. Request API  - Bearer or access_token
     #########################     
     # Fetch a protected resource, i.e. user profile
     r = google.get('https://www.googleapis.com/oauth2/v1/userinfo')
     print(r.content)






# Run Interpreter
if __name__ == "__main__":
    main()
