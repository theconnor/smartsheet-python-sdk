# Smartsheet Webhooks API Python Client
# Wed  8 Jun 17:04:16 2016

import json
import requests
import smartsheet
smartsheet = smartsheet.Smartsheet('21m49si6qmhhiyim7m59m34w9a')

# TODO:
# i/ list, delete methods

"""

    Smartsheet Webhook API Client
    -----------------------------
    exposes CRUD functionality for
    smartsheet webhooks

"""


class Smartsheet_Webhooks(object):
    api_key = '21m49si6qmhhiyim7m59m34w9a'
    client_id = 'eyss2dcasri2p7isw'
    client_secret = '20u6o6gbtcd4yc486v'
    base_url = 'https://api.smartsheet.com/2.0/webhooks'
    headers = {
        'Authorization': 'Bearer ' + api_key,
        'Content-Type': 'application/json'
    }

    @classmethod
    def create(cls, obj):
        resp = requests.post(cls.base_url, headers=cls.headers, data=json.dumps(obj))
        return resp.json()

    @classmethod
    def list(cls):
        pass

    @classmethod
    def enable(cls, id):
        url = cls.base_url + '/' + str(id)
        body = json.dumps({
            'enabled': True
        })
        new = requests.put(url, headers=cls.headers, data=body)
        print new.json()

    @classmethod
    def delete(cls, id):
        pass

    @classmethod
    def delete_all(cls):
        resp = requests.get(cls.base_url, headers=cls.headers)
        hooks =  resp.json().get('data')

        for hook in hooks:
            url = cls.base_url + '/' + str(hook['id'])
            new = requests.delete(url, headers=cls.headers)
            print new.json()
