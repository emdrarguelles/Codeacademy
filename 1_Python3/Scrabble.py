letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

s_letters = [letter.lower() for letter in letters]

points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letters_to_points = dict(zip(letters, points))
letters_to_points.update(dict(zip(s_letters, points)))
letters_to_points.update({" ": 0})

def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letters_to_points.get(letter, 0)
  return point_total

players_to_word = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

player_to_points = {}

def play_word(player, word):
  players_to_word[player] += [word]

def update_points_totals(player, word):
  play_word(player, word)
  for player, words in players_to_word.items():
    player_points = 0
    for word in words:
      player_points += score_word(word)
    player_to_points.update({player: player_points})
  return print(player_to_points)

# test update_points_totals("player1", "RED")

# test print(players_to_word)
