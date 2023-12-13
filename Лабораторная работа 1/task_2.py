list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
m_index = len(list_players) // 2
l_team = list_players[:m_index]
r_team = list_players[m_index:]
print(l_team)
print(r_team)
