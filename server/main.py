from cleaning_data import command_func
from server import send_message

'''
This model runs all needed models in one place,
therefore it gives convince to devolp each model spesficly not effecting on other models,
And this model will be base all models of our cloud.... 
'''

#Code line 
while True:
    message = command_func()
    print(message)
    if message == 'break':
        break
    send_message(message)

