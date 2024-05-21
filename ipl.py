from random import randrange
teams = [
    "KKR",
    "CSK",
    "MI",
    "RR",
    "GT",
    "PBKS",
    "RCB",
    "SRH",
    "DC",
    "LSG", 
]

trophy = randrange(1, len(teams))
print(f'{teams[trophy]} won!')