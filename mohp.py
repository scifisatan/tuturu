# Importing required python modules
import requests

def number(num):
    result = f"{int(num):,d}"
    return result

# Getting data/numbers
def stats():
    link = "https://covid19.mohp.gov.np/covid/api/confirmedcases"
    data = requests.get(link).json()
    tested = data.get('nepal').get('samples_tested')
    negative = data.get('nepal').get('negative')
    positive = data.get('nepal').get('positive')
    deaths = data.get('nepal').get('deaths')
    recovered = data.get('nepal').get('extra1')
    date = data.get('nepal').get('date')
    today_death = data.get('nepal').get('today_death')
    today_newcase = data.get('nepal').get('today_newcase')
    today_recovered = data.get('nepal').get('today_recovered')
    today_rdt = data.get('nepal').get('today_rdt')
    today_pcr = data.get('nepal').get('today_pcr')
    new_data = f"{tested} {negative} {positive} {deaths} {recovered} {date} {today_death} {today_newcase} {today_recovered} {today_rdt} {today_pcr}"
    new_datal = new_data.split(' ')
    return new_datal
