import requests
from datetime import datetime
import os

def banner():
	os.system('clear')
#	console.clear()
	print('                 _     _       __  ___   ')
	print('                (_)   | |     /_ |/ _ \  ')
	print('   ___ _____   ___  __| |______| | (_) | ')
	print('  / __/ _ \ \ / / |/ _` |______| |\__, | ')
	print(' | (__ (_) \ V /| | (_| |      | |  / /  ')
	print('  \___\___/ \_/ |_|\__,_|      |_| /_/   \n')

#define colors
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red


flag = ''

flags = {
	'Portugal' : '🇵🇹',
	'Italy' : '🇮🇹',
	'Spain' : '🇪🇸',
	'USA' : '🇺🇸',
	'UK' : '🇬🇧',
	'Germany' : '🇩🇪',
	'Sweden' : '🇸🇪',
	'China' : '🇨🇳',
	'Israel' : '🇮🇱',
	'Iran' : '🇮🇷',
	'France' : '🇫🇷',
	'Switzerland' : '🇨🇭',
	'S. Korea' : '🇰🇷',
	'Netherlands' : '🇳🇱',
	'Austria' : '🇦🇹',
	'Belgium' : '🇧🇪',
	'Norway' : '🇳🇴',
	'Brazil' : '🇧🇷',
	'Thailand' : '🇹🇭',
	'Japan' : '🇯🇵',
	'Canada' : '🇨🇦',
	'Australia' : '🇦🇺',
	'Malaysia' : '🇲🇾',
	'Ireland' : '🇮🇪',
	'Luxembourg' : '🇱🇺',
	'Ecuador' : '🇪🇨',
	'Chile' : '🇨🇱',
	'Pakistan' : '🇵🇰',
	'Poland' : '🇵🇱',
	'Romania' : '🇷🇴',
	'Saudi Arabia' : '🇸🇦',
	'Finland' : '🇫🇮',
	'Greece' : '🇬🇷',
	'Iceland' : '🇮🇸',
	'South Africa' : '🇿🇦',
	'Russia' : '🇷🇺',
	'Singapore' : '🇸🇬',
	'Qatar' : '🇶🇦',
	'Peru' : '🇵🇪',
	'Hong Kong' : '🇭🇰',
	'Estonia' : '🇪🇪',
	'Serbia' : '🇷🇸',
	'Iraq' : '🇮🇶',
	'Lebanon' : '🇱🇧',
	'Algeria' : '🇩🇿',
	'Angola' : '🇦🇴',
	'Taiwan' : '🇹🇼',
	'Morocco' : '🇲🇦',
	'Vietnam' : '🇻🇳',
	'Cambodia' : '🇰🇭',
	'Cuba' : '🇨🇺',
	'Macao' : '🇲🇴',
	'Mozambique' : '🇲🇿',
	'Myanmar' : '🇲🇲',
	'Timor-Leste' : '🇹🇱',
	'Sao Tome and Principe' : '🇸🇹',
	'Mexico' : '🇲🇽'
}

date_format = '%d-%m-%Y %H:%M'
now = datetime.now()
date_str = now.strftime(date_format)

another = True
go_again = 'y'

while another:

	banner()

	country = input('Enter country: ').title()

	if country == '':
		country = 'Portugal'
	
	if country == 'Usa':
		country = 'USA'
		
	if country == 'Uk':
		country = 'UK'

	if country == 'Stp':
		country = 'Sao Tome and Principe'

	if country == 'Hk':
		country = 'Hong Kong'	
		
	banner()		
	flag = flags.get(str(country), ' 🇺🇳  🏳️‍🌈')

	r = requests.get('https://corona.lmao.ninja/countries')
	info = r.json()
	my_info = [c for c in info if c['country'] == country]
	if my_info:
		print('\n>> '+'🦠 '+ flag + '  ' + f'Covid-19 {country} Report\n>> {date_str}\n')
		print(R + '>> Today:' + W)
		print(f'>> Cases today in {country}: ' + R + f'{my_info[0] ["todayCases"]}' + W)
		print(f'>> Deaths today in {country}: ' + R + f'{my_info[0] ["todayDeaths"]}\n' + W)

		print(R + '>>Totals' + W)
		print(f'>> Cases so far in {country}: ' + R + f'{my_info[0] ["cases"]}' + W)
		print(f'>> Deaths so far in {country}: ' + R + f'{my_info[0] ["deaths"]}\n' + W)
		
		print(f'>> Active in {country}: ' + R + f'{my_info[0] ["active"]}' + W)
		print(f'>> Critical in {country}: ' + R + f'{my_info[0] ["critical"]}' + W)
		print(f'>> Recovered so far in {country}: ' + R + f'{my_info[0] ["recovered"]}\n' + W)

		print(f'>> Tests in {country}: ' + R + f'{my_info[0] ["tests"]}\n' + W)

		print(f'>> Cases per million in {country}: ' + R + f'{my_info[0] ["casesPerOneMillion"]}' + W)
		print(f'>> Deaths per million in {country}: ' + R + f'{my_info[0] ["deathsPerOneMillion"]}' + W)
		print(f'>> Tests per million in {country}: ' + R + f'{my_info[0] ["testsPerOneMillion"]}\n' + W)
		
		percent = (int(my_info[0] ["deaths"]) / int(my_info[0] ["cases"])) * 100

		print(R + '>> Percent: ' + str("%.2f" % percent) + '%\n' + W)
	else:
		print(f'No data for {country}')
	
	go_again = input('Wanna go again? (y/n)').title()
	if go_again != 'N':
		another = True
	else:
		another = False
		banner()
		print('See you soon.\nStay Safe.\n\n#stayTheFuckHome\n'+'🦠 🇺🇳  🏳️‍🌈\n\n')
