from bs4 import BeautifulSoup
import requests
import pandas as pd
from tabulate import tabulate

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

def list_anime():
    url = 'https://www3.animeflv.net'
    list_animes = []
    list_chapters = []
    page = requests.get(url, headers = headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    animes = soup.find_all('strong', class_='Title')
    chapters = soup.find_all('span', class_='Capi')
    count = 0
    
    for anime in animes:
        if count == 8:
            count = 0
            break
        count += 1
        list_animes.append(anime.text)
    for chapter in chapters:
        if count == 8:
            break
        count += 1
        list_chapters.append(chapter.text)
    
    df = pd.DataFrame({'ANIME':list_animes, 'CHAPTER':list_chapters})
    df.index = df.index + 1
    print(tabulate(df, showindex=True, headers=df.columns))
    
def list_league(comp):
    url = None
    if comp == 'laliga':
        url = 'https://resultados.as.com/resultados/futbol/primera/clasificacion/'
        result_url = 'https://resultados.as.com/resultados/futbol/primera/jornada/'
    elif comp == 'premier':
        url = 'https://resultados.as.com/resultados/futbol/inglaterra/clasificacion/'
        result_url = 'https://resultados.as.com/resultados/futbol/inglaterra/jornada/'
        
    list_teams = []
    list_points = []
    list_tr = []
    list_results = []
    
    page = requests.get(url, headers = headers)
    result_page = requests.get(result_url, headers = headers)
    
    soup = BeautifulSoup(page.content, 'html.parser')
    result_soup = BeautifulSoup(result_page.content, 'html.parser')
    
    teams = soup.find_all('span', class_='nombre-equipo')
    points = soup.find_all('td', class_='destacado')
    year = soup.find('span', class_='tit-subtitle-info').text
    
    result_teams = result_soup.find_all('span', class_='nombre-equipo')
    results = result_soup.find_all('a', class_='resultado')
    results += result_soup.find_all('span', class_='resultado');
    date = result_soup.find('span', class_='fecha-evento').text
    
    if len(results) == 0:
        results = result_soup.find_all('span', class_='resultado')
    
    count = 0
    
    for team in teams:
        if count == 20:
            count = 0
            break
        count += 1
        list_teams.append(team.text)
    
    for point in points:
        if count == 20:
            count = 0
            break
        count += 1
        list_points.append(point.text)
        
    for result in results:
        if count == 10:
            count = 0
            break
        count += 1
        list_results.append(result.text.strip().replace(" ", "").replace("\n", ""))
    
    match = ""
    for team in result_teams:
        count += 1
        if count % 2 != 0:
            match = team.text + " vs "
        else:
            match += team.text
        if count % 2 == 0:
            list_tr.append(match)

    df = pd.DataFrame({'MATCH':list_tr, 'RESULT':list_results})

    print("CURRENT RESULTS <" + date.strip().replace(" ", "") + ">\n")
    print(tabulate(df, showindex=False, headers=df.columns))
    
    print("------------------------------------")
    
    print("CLASSIFICATION <"+year+">\n")
    df = pd.DataFrame({'TEAM':list_teams, 'POINTS':list_points})
    df.index = df.index + 1
    print(tabulate(df, showindex=True, headers=df.columns))