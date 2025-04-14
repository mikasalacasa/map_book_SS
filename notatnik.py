

users:list =[
    {"name":"Julia","location":"Ząbki","posts":10},
    {"name":"Julia","location":"Sokółka","posts":20},
    {"name":"Klaudia","location":"Warszawa","posts":7},
    {"name":"Marcin","location":"Grudziądz","posts":1000},
    {"name":"Mateusz","location":"Lublin","posts":1}
]


def update_user(users_data: list)-> None:
    username: str = input("Podaj imie znajomego którego chcesz zmodyfikować: ")
    for user in users:
        if user["name"] == username:
            user['name'] = input('Podaj nowe imie: ')
            user['location'] = input('Podaj nową lokalizację: ')
            user['posts'] = input('Podaj nową liczbę postów: ')


