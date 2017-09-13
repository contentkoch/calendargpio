import configparser

config = configparser.ConfigParser()
config.read("config.ini")

ContactPin_A = config.get('Boardlayout', 'ContactPin_A')
ContactPin_B = config.get('Boardlayout', 'ContactPin_B')
ContactPin_C = config.get('Boardlayout', 'ContactPin_C')
ContactPin_D = config.get('Boardlayout', 'ContactPin_D')




print(ContactPin_A, ContactPin_B,ContactPin_C,ContactPin_D)

#[CalendarToFunctionMap]
#CallA = gutenmorgen
#CallB = gutenabend
#CallC = froheswochenende
#CallD = empty

CalendarToFunctionMap = { 
'CallA': config.get('CalendarToFunctionMap', 'CallA'), 
'CallB': config.get('CalendarToFunctionMap', 'CallB'), 
'CallC': config.get('CalendarToFunctionMap', 'CallC'), 
'CallD': config.get('CalendarToFunctionMap', 'CallD')
}

print(CalendarToFunctionMap)

# Read string from calendar and switch pin according to mapped key from config file

# if ( getEventName == FunctionMapValue ): 
#	
