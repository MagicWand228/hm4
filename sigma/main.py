print(f"NameError - {type(NameError)} - {issubclass(NameError, BaseException)}") 
 

operatornames = ('Kyivstar', 'Vodafone', 'lifecell')

countryCode = '+380'

def checknumber(number, operatorname):
    if not number.startswith(countryCode):
        raise NameError(f'Your country code should be {countryCode}')
    
    if operatorname not in operatornames:
        raise NameError(f'Your operator "{operatorname}" is invalid')
    
    print('Your call is approved')

number = input('Enter your phone number  e.g. +380987654321: ')
operatorname = input('Enter your operator name: ')


try:
    checknumber(number, operatorname)
except NameError as e:
    print(e)