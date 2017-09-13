# calendargpio Switching OrangePi/RaspberryPi GPIO Pins through the google calendar

# Map Relay Contact "A...H" to GPIO Pin "X" depending on Raspberry Pi or Orange Pi

[Boardlayout]
ContactPin_A=1
ContactPin_B=2
ContactPin_C=3
ContactPin_D=4

# Map Calendar String (="Function call") to Relay Contact

[CalendarToFunctionMap]
CallA = gutenmorgen
CallB = gutenabend
CallC = froheswochenende
CallD = empty



[InstanceInformation]

# name of the Google API credentials
credential_key = client_secret.json

# Location
location = playerinshop

#TODO:
#set/delete cronjobs

