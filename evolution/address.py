import os
import json
import requests
from urllib import parse
from authentication.models import address_model

class address_api:

    url_query = {'analyze_type': 'similar', 'size': '10', 'query': '', 'page': '1'}
    queryset = address_model.objects.all()

    def __init__(self, address):
        self.create_points(address)

    def create_points(self, address):
        try:
            self.url_query['query'] = '+'.join(list(map(lambda x: parse.quote(x), address.split())))
            query_encoding = '&'.join(list(map('='.join, self.url_query.items())))
            headers = {'Authorization': os.environ['KAKAO_API_KEY']}
            r = requests.get("https://dapi.kakao.com/v2/local/search/address.json?" + query_encoding, headers=headers)
            data = json.loads(r.text)['documents'][0]
            address_create = self.queryset.create(
                x=data['x'],
                y=data['y'],
                total_address=address,
            )
        except Exception as e:
            print(e)
            return None
        else:
            return address_create
