import json
import urllib.request

# Fill in your own values for the key and steamid variables
key = '1234567890ABCDEF1234567890ABCDEF' # Your Steam Web API key, get it from: https://steamcommunity.com/dev/apikey
steamid = '76561198092541763' # The Steam ID to get the friends list from, find yours from a website like https://steamid.io/

# Construct the URL with the key and steamid variables
url = 'https://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key=' + key + '&steamid=' + steamid + '&relationship=friend'

# Fetch the JSON data from the URL
response = urllib.request.urlopen(url)
json_data = json.loads(response.read())

# Extract the steam IDs from the JSON
steam_ids = [friend['steamid'] for friend in json_data['friendslist']['friends']]

# Concatenate the steam IDs into a comma-separated string
steam_ids_str = ','.join(steam_ids)

# Output the steam IDs string
print(steam_ids_str)

# Write the result to the friends.txt file
with open('friends.txt', 'w') as f:
    f.write(steam_ids_str)
