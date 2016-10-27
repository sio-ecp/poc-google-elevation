# Necessary libraries
import requests
import json

# mykey.py must be in the same folder
# It contains the private Google access key, store in the "KEY" var
import mykey

# Google Elevation URL
URL='https://maps.googleapis.com/maps/api/elevation/json'

def findElevation(latitude,longitude):

    # Build and send the request
    r = requests.get(URL, params={'key': mykey.KEY, 'locations': str(latitude) + ',' + str(longitude)})

    # Parse received JSON
    parsed_json = json.loads(r.text)
    results = parsed_json['results']

    return results[0]['elevation']







# Print Elevation result
#print('The "Champs-de-Mars" elevation is '+str(results[0]['elevation'])+' meters, according to Google.')
