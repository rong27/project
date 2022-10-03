from django.http import JsonResponse
from django.shortcuts import render
import pandas as pd


def load_data_pk():
    # Read data from csv file
    df_pk = pd.read_csv('app_leaderboard/dataset/pk_nation.csv', sep = '|')
    
    global twUsCh
    twUsCh = dict(list(df_pk.values))

    df_pk = pd.read_csv('app_leaderboard/dataset/pk_political_party.csv', sep = '|')

    global tuc
    tuc = dict(list(df_pk.values))
    del df_pk

# load pk data
load_data_pk()

def pk_nation(request):
    return render(request,
                  'app_leaderboard/home.html', twUsCh)

def pk_political_party(request):
    return render(request,
                  'app_leaderboard/home.html', tuc)

print('app_leaderboard -- 國家聲量載入成功!')
print('app_leaderboard -- 政黨聲量載入成功!')