def get_user_input():
    user_name = input("Enter your name: ")
    user_email = input("Enter your email: ")
    destination = input("Enter your destination: ")
    start_date = input("Enter your trip start date (YYYY-MM-DD): ")
    end_date = input("Enter your trip end date (YYYY-MM-DD): ")
    return destination, start_date, end_date