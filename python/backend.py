import clearbit, requests, json, re, pprint
from pprint import pprint

selectedMacros = ['carbohydrates', 'protein', 'fat']
defaultRestaurants = {'McDonald\'s':'513fbc1283aa2dc80c000053', 'Burger King':'513fbc1283aa2dc80c00000a', 'Wendy\'s':'513fbc1283aa2dc80c00000f', 'Chipotle':'513fbc1283aa2dc80c000002', 'Subway':'513fbc1283aa2dc80c000005', 'Panera Bread':'513fbc1283aa2dc80c00000c', 'Papa John\'s':'513fbc1283aa2dc80c00000e'}
brandIdDict = json.loads(open('brand_ids.json').read())

clearbitApiKey = open('.clearbit.api-key').read().strip('\n')
nutritionApiKey = open('.nutrition.api-key').read().strip('\n').split('\n')

def getMainPage():
    results = list()
    for restaurant in defaultRestaurants:
        print(restaurant)
        logo = getLogo(restaurant)
        name = restaurant
        numFoods = getNumFoods(restaurant, defaultRestaurants[restaurant])
    return {'logo': logo, 'name': name, 'numFoods': numFoods}

def getRestaurant(restaurant):
    logo = getLogo(restaurant)
    foods = getFoods(restaurant, brandIdDict[restaurant])
    return {'logo': logo, 'name': name, 'foods': foods}

def getFoods(brand, brandIds):
    _url = 'https://trackapi.nutritionix.com/v2/search/instant'
    _params = {'brand_ids':brandIds, 'query':brand, 'branded':'true', 'common':'false'}
    _headers = {'x-app-id':nutritionApiKey[0], 'x-app-key':nutritionApiKey[1], 'x-remote-user-id':'0'}
    data = requests.get(url = _url, params = _params, headers = _headers).json()
    return data['branded']

def getNumFoods(brand, brandIds):
    return len(getFoods(brand, brandIds))

def getLogo(restaurant):
    _url = 'https://company.clearbit.com/v1/domains/find?name=' + str(restaurant)
    data = requests.get(url = _url, auth = (clearbitApiKey, '')).json()
    return data['logo']

def search(search_term):
    _url = 'https://api.nal.usda.gov/fdc/v1/search'
    _params = {'api_key':clearbitApiKey, 'generalSearchInput':search_term}

    data = requests.get(url = _url, params = _params).json()
    foods = data['foods']

    id_list = list()
    for i in range(len(foods)):
        id_list.append(foods[0]['fdcId'])

    return id_list

def getNutrients(fdcid):
    _url = 'https://api.nal.usda.gov/fdc/v1/' + str(fdcid)
    _params = {'api_key':apiKey}

    r = requests.get(url = _url, params = _params)
    nutrients = r.json()['foodNutrients']

    return nutrients

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
    #test = 'chicken nuggets'
    # id_list = search(test)
    # for id in id_list:
    #     nutrients = getNutrients(id)
    #     macros = getMacros(nutrients)
    #     selectMacros(macros)
    #     return
    # getLogo('Burger King')
    getMainPage()

main()
