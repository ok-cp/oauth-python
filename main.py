## global var
resource_server = oauth.google.com
redirect_uri = www.



#### Resource Owner 승인
## Resource Server Login
url = https://{resource_server}/?client_id={}&scope={}&redirect_uri={redirect_uri}


## redirect URL



### Resource Server 승인
## Send Authorization code, client_id, client_secret
## Request AccessToken
send_auth = https://{resource_server}/token?grant_type=auhorization_code&code={auth_code}&redirect_uri={redirect_uri}&client_id={client_id}&client_secret={client_secret}




### AccessToken & RefreshToken 발급
## Delete Authorization code

## Receive AccessToken





## Request API 
## Bearer
## access_token

