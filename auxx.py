from termcolor import colored

lst = ['adkf', 'adufji', 'aiodjf', 'jdioagjfa']
specials = [0, 1]

color = 'blue'
for i in range(len(lst)):
    if lst.index(lst[i]) in specials:
        color = 'green'
    else: color = 'blue'
    
    print(colored(lst[i], color))

