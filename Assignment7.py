#Anh Vu - Assignment 7
# Write a main module that does something interesting with any of these "state" functions.
# For example, you could create a quiz, ask the user for the capital of 'North Dakota',
# and tell them if they are correct or not.
# Or you could test them on whether they know their state abbreviations.
# It doesn't have to be complex unless you are ambitious,
# just demonstrate the use of modules in Python and learn about the power of modular design.

import random
#Gameloop

StatesName = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware',

    'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana',

    'Maine', 'Maryland', 'Massachusettes', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana',

    'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina',

    'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina',

    'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia',

    'Wisconsin', 'Wyoming']

Abbreviations = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA',

    'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH',

    'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX',

    'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']

state_capitals = ['Montgomery', 'Juneau', 'Phoenix', 'Little Rock', 'Sacramento', 'Denver',

    'Hartford', 'Dover', 'Tallahassee', 'Atlanta', 'Honolulu', 'Boise', 'Springfield',

    'Indianapolis', 'Des Moines', 'Topeka', 'Frankfort', 'Baton Rouge', 'Augusta',

    'Annapolis', 'Boston', 'Lansing', 'St. Paul', 'Jackson', 'Jefferson City', 'Helena',

    'Lincoln', 'Carson City', 'Concord', 'Trenton', 'Santa Fe', 'Albany', 'Raleigh',

    'Bismarck', 'Columbus', 'Oklahoma City', 'Salem', 'Harrisburg', 'Providence',

    'Columbia', 'Pierre', 'Nashville', 'Austin', 'Salt Lake City', 'Montpelier',

    'Richmond', 'Olympia', 'Charleston', 'Madison', 'Cheyenne']

    #func1
def state_to_abbrev(state_name):

    for i in range(0, len(StatesName)):

        if StatesName[i] == state_name:

            return Abbreviations[i]

    pass

    #func2
def abbrev_to_state(abbreviation):

    for i in range(0, len(StatesAbbreviations)):

        if Abbreviations[i] == abbreviation:

            return StatesName[i]

    pass
    #func3
def state_to_capital(state_name):

    for i in range(0, len(StatesName)):

        if StatesName[i] == state_name:

            return state_capitals[i]

    pass