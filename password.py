import uuid

print('Welcome to Password Generator!')

while True:
    
    # generates UUID for password
    uuid = uuid.uuid4()
    
    password = str(uuid) + str(uuid) + str(uuid) + str(uuid) + str(uuid) + str(uuid) + str(uuid) + str(uuid) + str(uuid) + str(uuid)
    print('Your new password is : %s' % password)
    
    response = input('Press enter to close')
    if response == 'enter':
        break