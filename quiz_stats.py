if rounds_played > 0:

    # Game history
    print("**** Game Statistics ****")

    percentage_won = rounds_won / rounds_played * 100
    percentage_lost = rounds_lost / rounds_played * 100

    print(f"Won: {rounder(percentage_won)}%,  Lost: {rounder(percentage_lost)}%, "
          f"Draw: {rounder(100 - percentage_won - percentage_lost)}%")

else:
    print()