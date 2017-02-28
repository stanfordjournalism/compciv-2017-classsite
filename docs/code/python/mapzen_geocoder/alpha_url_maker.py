BASE_URL = 'https://search.mapzen.com/v1/search?api_key={apikey}&text={location}'

location_name = 'Stanford University'
# URLs can't have spaces in them
txtlocation = location_name.replace(' ', '+')
# note that there are a ton of characters that URLs can't have...but
# we're being naive
fake_api_key = 'BLAHBLAHKEY'

the_url = BASE_URL.format(apikey=fake_api_key, location=txtlocation)

print(the_url)





