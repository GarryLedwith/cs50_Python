def main(): 
    difficulty = input("Difficult or casual?")
    players = input("Multiplayer oir single-player?")
    
    # Conditional  
    if difficulty == "difficult" and players == "multiplayer":
        recommend("Dark Souls")
    elif difficulty == "difficult" and players == "single-player":
        recommend("The Last of Us")
    elif difficulty == "casual" and players == "multiplayer":
        recommend("Mario Kart")
    elif difficulty == "casual" and players == "single-player":
        recommend("Horizon Zero Dawn")
    else:
        print("Invalid input. Please try again.")
    
def recommend(game): 
    print("You might like", game)
    
    
main() 