import os
import json
import requests
from urllib import parse
from authentication.models import address_model

class address_api:

    url_query = {'analyze_type': 'similar', 'size': '10', 'query': '', 'page': '1'}
    queryset = address_model.objects.all()
    object = None

    def __init__(self, address):
        self.object = self.create_points(address)

    def create_points(self, address):
        address_check = self.queryset.filter(address_string=address)
        if not address_check.exists():
            try:
                self.url_query['query'] = '+'.join(list(map(lambda x: parse.quote(x), address.split())))
                query_encoding = '&'.join(list(map('='.join, self.url_query.items())))
                headers = {'Authorization': os.environ['KAKAO_API_KEY']}
                r = requests.get("https://dapi.kakao.com/v2/local/search/address.json?" + query_encoding, headers=headers)
                data = json.loads(r.text)['documents'][0]
                address_create = self.queryset.create(
                    x=data['x'],
                    y=data['y'],
                    address_string=address,
                )
            except Exception as e:
                return e
            else:
                return address_create
        return address_check[0]
