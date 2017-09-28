from __future__ import print_function

import configparser
import quickstart
import datetime
import dateutil.parser
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

import datetime


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



try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials


def filterEventList(events, LocationClient):
    """Take the fetched events list and compare if it is relevant to the location
    returns filtered event list
    """
    LocalEvents = []				# Will contain all the relevant future events after filtering by location [ datetime,       'summary'] 

    for event in events:            
        #print( datetime.strptime( event['start']['dateTime']  )  )
        if LocationClient in event['location'].lower():
            LocalEvents.append( {'starttime':event['start'], 'summary':event['summary']})

    return LocalEvents




def fetch(location, credentialfile):
    """Shows basic usage of the Google Calendar API.

    Creates a Google Calendar API service object and outputs a list of the next
    10 events on the user's calendar.
    """
    
    CLIENT_SECRET_FILE = credentialfile
    LocationClient = location
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    #print('Getting the upcoming 10 events')
    
    eventsResult = service.events().list(
        calendarId='primary', timeMin=now, maxResults=10, singleEvents=True,
        orderBy='startTime').execute()
    events = eventsResult.get('items', [])

    #for m in events:
     #   print( type( m['start']['dateTime']) )
    
    if not events:
        print('No upcoming events found.')
        
    
    return filterEventList(events, LocationClient)
    
    

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

    
    
    