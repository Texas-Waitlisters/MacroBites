import requests, json, re, pprint
from pprint import pprint

macros = ['carbohydrates', 'protein', 'fat']
api_key = open('.api-key').read().strip('\n')

def getInfo(fdcid):
    _url = 'https://api.nal.usda.gov/fdc/v1/' + str(fdcid)
    _params = {'api_key':api_key}
    r = requests.get(url = _url, params = _params)
    pprint(r.json())
    return r.json()

def search(q):
    _url = 'https://api.nal.usda.gov/fdc/v1/search'
    _params = {'api_key':api_key, 'generalSearchInput':q}

    data = requests.get(url = _url, params = _params).json()
    pprint(data['foods'][1])
    foods = data['foods']

    fdcid = data['foods'][1]['fdcId']
    getInfo(fdcid)

def main():
    test = 'chicken nuggets'
    search(test)

main()
