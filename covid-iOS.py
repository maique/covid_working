import requests
from datetime import datetime
import console

def red():
	console.set_color(1, 0, 0)

def white():
	console.set_color(1, 1, 1)	

def banner():
#	os.system('clear')
	console.clear()
	print('                 _     _       __  ___   ')
	print('                (_)   | |     /_ |/ _ \  ')
	print('   ___ _____   ___  __| |______| | (_) | ')
	print('  / __/ _ \ \ / / |/ _` |______| |\__, | ')
	print(' | (__ (_) \ V /| | (_| |      | |  / /  ')
	print('  \___\___/ \_/ |_|\__,_|      |_| /_/   \n')	

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
	'Denmark' : '🇩🇰',
	'Sao Tome and Principe' : '🇸🇹'
}

date_format = '%d-%m-%Y %H:%M'
now = datetime.now()
date_str = now.strftime(date_format)

another = True
go_again = 'y'

while another:
	
	#console.clear()
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
		
	#console.clear()
	banner()

	flag = flags.get(str(country), '🇺🇳🏳️‍🌈')

	r = requests.get('https://corona.lmao.ninja/countries')
	info = r.json()
	my_info = [c for c in info if c['country'] == country]
	if my_info:
		print('\n>> '+'🦠'+flag + f' Covid-19 {country} Report\n>> {date_str}\n')

		red()
		print('>> Today:')
		white()
		print(f'>> Cases today in {country}: {my_info[0] ["todayCases"]}')
		print(f'>> Deaths today in {country}: {my_info[0] ["todayDeaths"]}')

		red()
		print('\n>> Totals:')
		white()
		print(f'>> Cases so far in {country}: {my_info[0] ["cases"]}')
		print(f'>> Deaths so far in {country}: {my_info[0] ["deaths"]}\n')
		print(f'>> Active in {country}: {my_info[0] ["active"]}')
		print(f'>> Critical in {country}: {my_info[0] ["critical"]}')
		print(f'>> Recovered so far in {country}: {my_info[0] ["recovered"]}\n')
		print(f'>> Tested in {country}: {my_info[0] ["tests"]}\n')

		print(f'>> Cases per million in {country}: {my_info[0] ["casesPerOneMillion"]}')
		print(f'>> Deaths per million in {country}: {my_info[0] ["deathsPerOneMillion"]}')
		print(f'>> Tests per million in {country}: {my_info[0] ["testsPerOneMillion"]}')
		
		percent = (int(my_info[0] ["deaths"])/int(my_info[0] ["cases"])) * 100
		
		red()
		print('\n>> Percent: ' + str("%.2f" % percent) + '%\n')
		white()
		
	else:
		print(f'No data for {country}')
	
	go_again = input('Wanna go again? (y/n)').title()
	if go_again != 'N':
		another = True
	else:
		another = False
		#console.clear()
		banner()
		print('See you soon.\nStay Safe.\n\n#stayTheFuckHome\n'+'🦠🇺🇳🏳️‍🌈')