highway_number = int(input())
if (highway_number < 1) or (highway_number > 999) or (highway_number % 100 == 0):
    print(f'{highway_number} is not a valid interstate highway number')
else:
    if (highway_number > 99):
        print(f'I-{highway_number} is auxiliary', end='')
        primary_number = highway_number % 100
        print(f', serving I-{primary_number}', end='')
    else:
        print(f'I-{highway_number} is primary', end='')
    if (highway_number % 2 == 0):
        print(', going east/west.')
    else:
        print(', going north/south.')
