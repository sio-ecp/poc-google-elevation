# Necessary libraries
import requests
import json

# mykey.py must be in the same folder
# It contains the private Google access key, store in the "KEY" var
import mykey

# Constants used for test
URL='https://maps.googleapis.com/maps/api/elevation/json'
# Exact location of the "Champs de Mars". Expected elevation i~s 35m.
LAT=48.856416
LONG=2.297273

# Build and send the request
r = requests.get(URL, params = {'key':mykey.KEY, 'locations':str(LAT)+','+str(LONG)})

# Parse received JSON
parsed_json = json.loads(r.text)
results = parsed_json['results']

# Print Elevation result
print('The "Champs-de-Mars" elevation is '+str(results[0]['elevation'])+' meters, according to Google.')