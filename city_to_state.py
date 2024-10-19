# This script maps a city to its state code and sends it to the state department

city_to_state_mapping = {
    'New York': 'NY',
    'Los Angeles': 'CA',
    'Chicago': 'IL',
    'Houston': 'TX',
    'Phoenix': 'AZ'
}

city = input('Enter the name of the city: ')

state_code = city_to_state_mapping.get(city, 'Unknown')

if state_code != 'Unknown':
    print(f'The state code for {city} is {state_code}. Sending to state department...')
    # Here you would add the code to send the state code to the state department
else:
    print(f'City {city} not found in the mapping.')
