import configparser
import quickstart
import datetime
import dateutil.parser


config = configparser.ConfigParser()
config.read("config.ini")

ContactPin_A = config.get('Boardlayout', 'ContactPin_A')
ContactPin_B = config.get('Boardlayout', 'ContactPin_B')
ContactPin_C = config.get('Boardlayout', 'ContactPin_C')
ContactPin_D = config.get('Boardlayout', 'ContactPin_D')
ContactPin_E = config.get('Boardlayout', 'ContactPin_E')
ContactPin_F = config.get('Boardlayout', 'ContactPin_F')
ContactPin_G = config.get('Boardlayout', 'ContactPin_G')
ContactPin_H = config.get('Boardlayout', 'ContactPin_H')



#print(ContactPin_A, ContactPin_B,ContactPin_C,ContactPin_D)

#[CalendarToFunctionMap]
#CallA = gutenmorgen
#CallB = gutenabend
#CallC = froheswochenende
#CallD = empty

CalendarToFunctionMap = { 
'CallA': config.get('CalendarToFunctionMap', 'CallA'), 
'CallB': config.get('CalendarToFunctionMap', 'CallB'), 
'CallC': config.get('CalendarToFunctionMap', 'CallC'), 
'CallD': config.get('CalendarToFunctionMap', 'CallD'),
'CallE': config.get('CalendarToFunctionMap', 'CallE'), 
'CallF': config.get('CalendarToFunctionMap', 'CallF'), 
'CallG': config.get('CalendarToFunctionMap', 'CallG'), 
'CallH': config.get('CalendarToFunctionMap', 'CallH')
}


# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/calendar-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
APPLICATION_NAME = 'Google Calendar API Python Quickstart'
location = config.get( 'InstanceInformation', 'location')
credentialfile = config.get( 'InstanceInformation', 'credential_key')



# Read string from calendar and switch pin according to mapped key from config file


filteredList= quickstart.fetch(location, credentialfile)

for entry in filteredList:
    #check every event for a defined call
    
    for call in CalendarToFunctionMap:  
        #compare all the calls to the ones from configfile
        
        if CalendarToFunctionMap[call] in entry['summary'].lower():
            dt = dateutil.parser.parse (entry['starttime']['dateTime'] )            #wasted 2 hours on this, official google api reference says event starttime datetime should be of type datetime
            
            print(dt.strftime('%M %H %d %m'))                                       #minute hour day month
            #todo set up job to set to set gpio pin according to configfile

    
    
    