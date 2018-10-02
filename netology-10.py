import requests
import json

TOKEN = 'e580d5b70e92710bbcef6ea5e700b728d6a7b06d284f88ba9fc37f47d852d803d395d03e94084ca27a628'
VERSION = '5.85'


class User:

    def __init__(self, vk_id):
        self.vk_id = vk_id

    def __str__(self):
        return f'https://vk.com/id{self.vk_id}'

    def __and__(self, other):
        params_and_self = dict(access_token=TOKEN, user_id=self.vk_id, v=VERSION)
        params_and_other = dict(access_token=TOKEN, user_id=other.vk_id, v=VERSION)
        friends_self_response = requests.get('https://api.vk.com/method/friends.get', params_and_self).text
        friends_other_response = requests.get('https://api.vk.com/method/friends.get', params_and_other).text
        friends_self_set = set(json.loads(friends_self_response)['response']['items'])
        friends_other_set = set(json.loads(friends_other_response)['response']['items'])
        mutual_friends = friends_self_set & friends_other_set
        mutual_friends_as_users = [User(item) for item in mutual_friends]
        return mutual_friends_as_users

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

    def get_link(self):
        return f'https://vk.com/id{self.vk_id}'


def core():
    vk_id_1 = int(input('Введите первый ID: '))
    vk_id_2 = input(('Введите второй ID: '))
    user_1 = User(vk_id_1)
    user_2 = User(vk_id_2)
    mutual_friends_list = user_1 & user_2
    if len(mutual_friends_list) > 0:
        print(f'Количество общих друзей пользователей: {len(mutual_friends_list)}')
        for item in mutual_friends_list:
            print(item)
    else:
        print(f'У пользователей с ID {vk_id_1} и {vk_id_2} нет общих друзей.')


if __name__ == '__main__':
    core()
