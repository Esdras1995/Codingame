winners = ['CP', 'PR', 'RL', 'LS', 'SC', 'CL', 'LP', 'PS', 'SR', 'RC']

def winner(player_a, player_b):
    # receive ex: 104 R, 29 P
    spa = player_a.split(' ')
    spb = player_b.split(' ')

    # {'104 R': 'R', '29 P': 'P'}
    g = {player_a:spa[1], player_b:spb[1]}
    
    # play same value : R == R
    if g[player_a] == g[player_b]:
        return (player_a, player_b) if int(spa[0])<int(spb[0]) else (player_b, player_a)
    
    return (player_a, player_b) if g[player_a]+g[player_b] in winners else (player_b, player_a)

    
n = int(input())
data = []
for i in range(n):
    inputs = input()
    data.append(inputs)
    


game = {}
while(len(data)>1):
    for i in range(0, len(data), 2):
        win, lose = winner(data[i], data[i+1])
        game.setdefault(win, []).append(lose)
        
        # Remove the loser
        if lose in game:
            del game[lose]
        
    data = list(game.keys())

number_player_win =data[-1].split(' ')[0]

print(number_player_win)
print(' '.join([ loser.split(' ')[0] for loser in game[data[-1]] ]))