from urllib.parse import urlencode

APP_ID = 6703864
OAUTH_URL = 'https://oauth.vk.com/authorize'
oauth_data = {
    'client_id': APP_ID,
    'display': 'page',
    'scope': 'friends',
    'response_type': 'token',
    'v': '5.85'
}

print('?'.join((OAUTH_URL, urlencode(oauth_data))))

TOKEN = 'e580d5b70e92710bbcef6ea5e700b728d6a7b06d284f88ba9fc37f47d852d803d395d03e94084ca27a628'