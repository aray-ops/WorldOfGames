from Utils import SCORES_FILE_NAME

def add_score(difficulty):
    POINTS_OF_WINNING = (int(difficulty) * 3) + 5
    try:
        with open(SCORES_FILE_NAME, 'r') as file:
            current_score = int(file.read().strip())
    except:
        current_score = 0
    
    new_score = current_score + POINTS_OF_WINNING
    with open(SCORES_FILE_NAME, 'w') as file:
        file.write(str(new_score))
    return new_score