import clearbit, requests, json, re, pprint
from pprint import pprint

selectedMacros = ['carbohydrates', 'protein', 'fat']
defaultRestaurants = {'McDonald\'s':'513fbc1283aa2dc80c000053', 'Burger King':'513fbc1283aa2dc80c00000a', 'Wendy\'s':'513fbc1283aa2dc80c00000f', 'Subway':'513fbc1283aa2dc80c000005', 'Panera Bread':'513fbc1283aa2dc80c00000c', 'Papa John\'s':'513fbc1283aa2dc80c00000e'}

def processJSON(file):
    raw = json.loads(open(file).read())
    result = dict()
    for item in raw:
        result[item['name']] = item['id']
    return result

brandIdDict = processJSON('brand_ids.json')

pprint(brandIdDict)

clearbitApiKey = open('.clearbit.api-key').read().strip('\n')
nutritionApiKey = open('.nutrition.api-key').read().strip('\n').split('\n')

def getMainPage():
    results = list()
    for restaurant in defaultRestaurants:
        print(restaurant)
        logo = getLogo(restaurant)
        name = restaurant
        numFoods = getNumFoods(restaurant, defaultRestaurants[restaurant])
        results.append({'logo': logo, 'name': name, 'numFoods': numFoods})
    pprint(results)
    return results

def getRestaurant(restaurant):
    logo = getLogo(restaurant)
    foods = getBrandFoods(restaurant, brandIdDict[restaurant])
    result = {'logo': logo, 'name': restaurant, 'foods': foods}
    pprint(result)
    return result

def getBrandFoods(brand, brandIds):
    _url = 'https://trackapi.nutritionix.com/v2/search/instant'
    _params = {'brand_ids':brandIds, 'query':brand, 'branded':'true', 'common':'false', 'detailed': 'true'}
    _headers = {'x-app-id':nutritionApiKey[0], 'x-app-key':nutritionApiKey[1], 'x-remote-user-id':'0'}
    data = requests.get(url = _url, params = _params, headers = _headers).json()
    return data['branded']

def getNumFoods(brand, brandIds):
    return len(getBrandFoods(brand, brandIds))

def search(query):
    _url = 'https://trackapi.nutritionix.com/v2/search/instant'
    _params = {'query': query, 'detailed': 'true'}
    _headers = {'x-app-id':nutritionApiKey[0], 'x-app-key':nutritionApiKey[1], 'x-remote-user-id':'0'}
    data = requests.get(url = _url, params = _params, headers = _headers).json()
    result = data['branded'] + data['common']
    return result

def getLogo(restaurant):
    _url = 'https://company.clearbit.com/v1/domains/find?name=' + str(restaurant)
    data = requests.get(url = _url, auth = (clearbitApiKey, '')).json()
    return data['logo']

def getMacros(nutrients):
    macros = dict()
    for entry in nutrients:
        try:
            macros[entry['nutrient']['name']] = str(entry['amount']) + entry['nutrient']['unitName']
        except:
            macros[entry['nutrient']['name']] = 'null'
    pprint(macros)
    return macros

def selectMacros(macros):
    result = dict()
    for macro in macros:
        if macro.lower() in selectedMacros:
            result[macro] = macros[macro]
    pprint(result)
    return result

def main():
    test = 'wendy\'s chicken nuggets'
    # search(test)

main()
