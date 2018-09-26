import requests
from pprint import pprint
import json

TOKEN = 'e580d5b70e92710bbcef6ea5e700b728d6a7b06d284f88ba9fc37f47d852d803d395d03e94084ca27a628'

id_1 = 609017
id_2 = 685162


class User:

    def __init__(self, token, vk_id):
        self.token = token
        self.vk_id = vk_id

    def get_name(self, vk_id):
        params_users = dict(access_token=TOKEN, user_ids=vk_id, v='5.85')
        get_name_response = requests.get('https://api.vk.com/method/users.get', params_users)
        self.f_name = get_name_response.json()['response'][0]['first_name']
        self.l_name = get_name_response.json()['response'][0]['last_name']
        return print(self.f_name, self.l_name)

    def mutual_friends(self, vk_id_1, vk_id_2):
        params_mutual = dict(access_token=TOKEN, source_uid=vk_id_1, target_uid=vk_id_2, v='5.85')
        mutual_friends_response = requests.get('https://api.vk.com/method/friends.getMutual', params_mutual).text
        self.mutual_friends_list = json.loads(mutual_friends_response)['response']
        return print(self.mutual_friends_list)


    # for i in mutual_friends_list[7:9]:
    #    get_name(i)
    # for item in mutual_friends_list:
    #    print(item, get_name(item))


mutual_friends(609017, 8118808)

# friends.get
# friends.getMutual
# 609017 - Anastasia Glagoleva
# 685162 - Ksenia Rozhkova

a_glagoleva = 