import requests
from datetime import datetime
import os


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
	'Timor-Leste' : '🇹🇱'
}

date_format = '%d-%m-%Y %H:%M'
now = datetime.now()
date_str = now.strftime(date_format)

another = True
go_again = 'y'



while another:

	os.system('clear')	
#	console.clear()

	country = input('Enter country: ').title()

	if country == '':
		country = 'Portugal'
	
	if country == 'Usa':
		country = 'USA'
		
	if country == 'Uk':
		country = 'UK'
		
#	console.clear()
		
	flag = flags.get(str(country), '🇺🇳🏳️‍🌈')

	r = requests.get('https://corona.lmao.ninja/countries')
	info = r.json()
	my_info = [c for c in info if c['country'] == country]
	if my_info:
		print('\n>> '+'🦠'+ flag + ' ' + f'Covid-19 {country} Report\n>> {date_str}\n')
		print(f'📈 Cases so far in {country}: {my_info[0] ["cases"]}')
		print(f'📈 Cases today in {country}: {my_info[0] ["todayCases"]}')
		print(f'📊 Cases per million in {country}: {my_info[0] ["casesPerOneMillion"]}\n')
		print(f'😱 Critical in {country}: {my_info[0] ["critical"]}')
		print(f'😎 Recovered so far in {country}: {my_info[0] ["recovered"]}\n')
		print(f'💀 Deaths so far in {country}: {my_info[0] ["deaths"]}')
		print(f'💀 Deaths today in {country}: {my_info[0] ["todayDeaths"]}')
		print(f'💀 Deaths per million in {country}: {my_info[0] ["deathsPerOneMillion"]}')
		
		percent = (int(my_info[0] ["deaths"]) / int(my_info[0] ["cases"])) * 100

		print(R + '💀 Percent: ' + str("%.2f" % percent) + '%\n' + W)
	else:
		print(f'No data for {country}')
	
	go_again = input('Wanna go again? (y/n)')
	if go_again == 'y':
		another = True
	else:
		another = False
		os.system('clear')
#		console.clear()
		print('See you soon.\nStay Safe.\n\n#stayTheFuckHome\n'+'🦠🇺🇳🏳️‍🌈\n\n')
