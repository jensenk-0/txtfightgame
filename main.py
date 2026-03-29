# runs the main game 

from turns import player_turn, enemy_turn, player, enemy


def choice_of_turns():
    choice = input("How many turns do you want to play with: ")
    number = int(choice)
    return number

def main_game(turns):
    for turn in range(1, turns+1):
        
        if player.health <= 0:
            print(f"the player has died!, player has {player.health} health left\n")
            print("GAME OVER!")
            break

        try:
            player_turn(turn)
        except Exception as err:
            print(err)
            continue


        if enemy.health <= 0:
            print(f"the enemy was defeated!, enemy has {enemy.health} health left\n")
            print("YOU WIN")
            break

        enemy_turn(turn)

    if player.health > 0 and enemy.health > 0:
        print(f"It is a tie!\nplayer had {player.health} health remaining\nenemy had {enemy.health} health remaining")


try:

    amount_of_turns = choice_of_turns()

except ValueError:
    print("invalid input, please type in a interger (ex: 3, 15, 62)")
    

main_game(amount_of_turns)



