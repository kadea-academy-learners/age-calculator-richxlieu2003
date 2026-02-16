import datetime

def main():
    birth_year = int(input("Enter your birth year: ")) 

    current_year = datetime.date.today().year

    age = current_year - birth_year

    print("--------------------")
    print(f"Current Year: {current_year}")
    print(f"You are approximately {age} years old.")

if __name__ == "__main__":
    main()
