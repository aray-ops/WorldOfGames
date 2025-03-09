from app import welcome, start_play

if __name__ == "__main__":
    username = input("Enter your name: ")
    print(welcome(username))
    start_play()