import requests
import json

TOKEN = 'e580d5b70e92710bbcef6ea5e700b728d6a7b06d284f88ba9fc37f47d852d803d395d03e94084ca27a628'
VERSION = '5.85'


class User:

    def __init__(self, vk_id):
        self.vk_id = vk_id

    def get_name(self):
        params_name = dict(access_token=TOKEN, user_ids=self.vk_id, v=VERSION)
        get_name_response = requests.get('https://api.vk.com/method/users.get', params_name)
        self.f_name = get_name_response.json()['response'][0]['first_name']
        self.l_name = get_name_response.json()['response'][0]['last_name']
        return self.f_name, self.l_name

    def get_domain(self):
        params_domain = dict(access_token=TOKEN, user_ids=self.vk_id, fields='domain', v=VERSION)
        get_name_response = requests.get('https://api.vk.com/method/users.get', params_domain)
        self.domain = get_name_response.json()['response'][0]['domain']
        return self.domain

    def mutual_friends(self, vk_id_2):
        self.vk_id_2 = vk_id_2
        params_mutual = dict(access_token=TOKEN, source_uid=self.vk_id, target_uid=vk_id_2, v=VERSION)
        mutual_friends_response = requests.get('https://api.vk.com/method/friends.getMutual', params_mutual).text
        self.mutual_friends_list = json.loads(mutual_friends_response)['response']
        mutual_friends_as_users = [User(item) for item in self.mutual_friends_list]
        return mutual_friends_as_users

    # метод __and__ дает аналогичный результат

    def __and__(self, other):
        params_and_self = dict(access_token=TOKEN, user_id=self.vk_id, v=VERSION)
        params_and_other = dict(access_token=TOKEN, user_id=other, v=VERSION)
        friends_self_response = requests.get('https://api.vk.com/method/friends.get', params_and_self).text
        friends_other_response = requests.get('https://api.vk.com/method/friends.get', params_and_other).text
        friends_self_set = set(json.loads(friends_self_response)['response']['items'])
        friends_other_set = set(json.loads(friends_other_response)['response']['items'])
        mutual_friends = friends_self_set & friends_other_set
        mutual_friends_as_users = [User(item) for item in mutual_friends]
        return mutual_friends_as_users

    def get_link(self):
        return f'https://vk.com/id{self.vk_id}'
