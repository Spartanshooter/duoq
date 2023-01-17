from django.http import HttpResponse
from riotwatcher import LolWatcher, ApiError
from django.shortcuts import render
import json

api_key = "RGAPI-d66393d0-7e41-491b-9b13-804eee952369"
watcher = LolWatcher(api_key)
my_region = 'euw1'

def test(request):
    Players = ['pqukk', 'hpswb', 'rybsldg', 'rqgrizl', 'gpthrqvte', 'xtuqszdhv', 'gatjry', 'Pantufla', 'wgvxz', 'L9Capybara420', 'L9Capybara69', 'sllviw']
    Names = ['GinerOwo', 'Anabel :o', 'lorena zzz', 'luisuwu', 'Adrián', 'Perralola', 'Nicolás', 'Teemo', 'Bertiño', 'Dembow', 'Yansito', 'Carlitos']
    dict = {}
    list = []
    cont = 0
    for Player in Players:
        cont += 1
        TotalLP = 0
        soloq = 0
        me = watcher.summoner.by_name(my_region, Player)
        my_ranked_stats = watcher.league.by_summoner(my_region, me['id'])
        #print(my_ranked_stats)
        #print('hola')
        #print('me')
        op = "https://www.op.gg/summoners/euw/"
        op += Player
        for queue in my_ranked_stats:
            z = queue
            #rank_text = ''.join(str(x) for x in queue)
            #rank_text2 = rank_text.replace("'", '"')
            #rank_text3 = rank_text2.replace('True', '"True"')
            #rank_text_4 = rank_text3.replace('False', '"False"')
            #print('comprobamos')
            #print(rank_text4)
            #z = json.loads(rank_text4)
            if z['queueType'] == "RANKED_SOLO_5x5":
                if z['tier'] == "IRON":
                    TotalLP += 0
                elif z['tier'] == "BRONZE":
                    TotalLP += 300
                elif z['tier'] == "BRONZE":
                    TotalLP += 600
                elif z['tier'] == "SILVER":
                    TotalLP += 900
                elif z['tier'] == "PLATINUM":
                    TotalLP += 1200
                elif z['tier'] == "DIAMOND":
                    TotalLP += 1500
                if z['rank'] == 'I':
                    TotalLP += 0
                elif z['rank'] == 'II':
                    TotalLP += 100
                elif z['rank'] == 'III':
                    TotalLP += 200
                TotalLP += z['leaguePoints']
                soloq=1
                thislist = [TotalLP, Names[cont-1], z['summonerName'], z['tier'], z['rank'], z['leaguePoints'], z['wins'], z['losses'], op]
                list.append(thislist)
            else:
                print('va a ser que no')
        #print('Bertogamer?')
        #print(soloq)
        if soloq==0:
            thislist = [0, Names[cont-1], Player, 'Unranked', '', '', '', '', op]
            list.append(thislist)
    dict['frutas'] = list
    return render(request, 'tabla.html', dict)

def test2(request):
    return render(request, 'tabla.html')
