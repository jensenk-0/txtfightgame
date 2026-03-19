from turns import player_turn, enemy_turn, player, enemy


def main_game(turns):
    for turn in range(1, turns+1):
        if player.health <= 0:
            print(f"the player has died!, player has {player.health} health left")
            print("GAME OVER!")
            break
        player_turn(turn)
        if enemy.health <= 0:
            print(f"the enemy was defeated!, enemy has {enemy.health} left")
            print("YOU WIN")
            break
        enemy_turn()

main_game(5)


