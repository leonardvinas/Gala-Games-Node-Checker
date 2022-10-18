import requests
import json
from termcolor import colored, cprint  # pip install termcolor

firstGalaNodeAuth = ''


def retrieve_messages(auth_code):
    headers = {
        'authorization': auth_code
    }
    r = requests.get(
        f'https://node-dashboard-api.gala.games/stats/dashboard', headers=headers)
    jsonn = json.loads(r.text)
    # print(jsonn)

    moduleStats = jsonn['moduleStats']
    modStatsLen = len(moduleStats)

    for i in range(0, modStatsLen):
        moduleStatsremove = moduleStats[i]
        userlicenses = moduleStatsremove['userLicenses']
        userOnline = moduleStatsremove['userOnline']
        definition = moduleStatsremove['definition']
        nodeName = definition['name']

        if (userOnline == userlicenses):
            cprint(nodeName, "green")
        else:
            cprint(nodeName, 'red')
        print('name:', nodeName, 'licenses:', userlicenses, 'online:', userOnline)
        i += i


print("My First Gala Node")
retrieve_messages(firstGalaNodeAuth)
