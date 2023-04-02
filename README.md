# BeatSaberQuestSteamFriends
Unlike the Steam version of ScoreSaber when using it on Quest the scores of Steam friends are not automatically shown in Beat Saber.
From [here](https://www.patreon.com/posts/65844663):
> Friends have to be manually added to /sdcard/ModData/com.beatgames.beatsaber/Mods/ScoreSaber/friends.txt

To be more precise, the Steam ID 64 values of your friends need to be put there as a comma separated list. To do this manually would be a quite tedious task, especially for accounts with a large number of friends.

This python script automatically retrieves the comma separated list of steam IDs of all Steam friends of an account using the Steam API. The data is output to the console as well as written to the "friends.txt" file that you need.

## Usage
ℹ️ To use this script you need to have Python installed. There are many guides online on how to install Python on any operating system, please find one suitable for yourself.

⚠️ Steam Web API keys are often involved in Steam account theft. Never give out your key to anyone! Don't enter the key in binary tools that you don't know the source code of, there is a reason why this is released as a python script with source code readable for everyone!

1. Download the script [from the latest release](https://github.com/YorVeX/BeatSaberQuestSteamFriends/releases/latest) (click one of the "Source Code" links) and save it somewhere.
1. Go to https://steamcommunity.com/dev/apikey and register for a Steam Web API key if you haven't already (it doesn't matter what you enter for the domain field), then retrieve the key from there.
1. Go to the folder of the downloaded script and open it (BeatSaberQuestSteamFriends.py) with a text editor.
1. Find the line `key = '1234567890ABCDEF1234567890ABCDEF'` and replace the dummy key between the single quotes with the Steam Web API key that you retrieved from the Steam website.
1. Find the line starting with `steamid =` and put the SteamID64 of your Steam account. You can use a tool like [SteamID.io](https://steamid.io) to find the steamID64 of any given account.
1. Save the script and run it by double clicking or from a console window.
1. The script should now have created a friends.txt file in the same folder the script is in.
1. Connect your Quest to your PC so that you can access its file system and copy the friends.txt file to the folder `/sdcard/ModData/com.beatgames.beatsaber/Mods/ScoreSaber/` on the device.
1. ⚠️ Unless you know you need the Steam Web API key for anything else it is strongly advised to revoke the key again now, using the same URL where you created it, it's an unnecessary security risk to have an unused API key configured!

The script also outputs the comma separated list of friends Steam IDs to the console, so you could pipe it into any other script to process it there.

Note that the script currently has no error handling whatsoever. Either it can retrieve the list or random things will happen 😛
