import re
import hashlib

class User:
    """Represents a bank user."""
    def __init__(self, name, email, password, pin, birth_date, balance=0.0):
        self.name = name
        self.email = email
        self.password = self._hash_password(password)  # Passwords are hashed for security
        self.pin = pin  # 4-digit PIN
        self.birth_date = birth_date
        self.balance = balance  # Initial balance

    def _hash_password(self, password):
        """Hashes the password using SHA256."""
        return hashlib.sha256(password.encode()).hexdigest()

    def verify_password(self, password):
        """Verifies if the input password matches the hashed password."""
        return self._hash_password(password) == self.password

    def __str__(self):
        return f"User: {self.name}, Email: {self.email}, Balance: ${self.balance:.2f}"


class Bank:
    """Represents the bank system."""
    def __init__(self):
        self.users = {}  # Stores users by email

    def create_account(self, name, email, password, pin, birth_date, initial_balance):
        """Creates a new bank account."""
        if email in self.users:
            print("An account with this email already exists.")
            return False

        # Email validation
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            print("Invalid email address.")
            return False

        # Password validation (minimum 6 characters)
        if len(password) < 6:
            print("Password must be at least 6 characters long.")
            return False

        # PIN validation (must be exactly 4 digits)
        if not (pin.isdigit() and len(pin) == 4):
            print("PIN must be a 4-digit number.")
            return False

        # Birth date validation (simple format check and not greater than 1800)
        if not re.match(r"\d{4}-\d{2}-\d{2}", birth_date) or int(birth_date.split('-')[0]) < 1800:
            print("Invalid birth date. Ensure correct format (YYYY-MM-DD) and that year is greater than 1800.")
            return False

        # Initial balance validation (must be a positive number)
        if initial_balance < 0:
            print("Initial balance must be a positive amount.")
            return False

        # Create and store the user
        user = User(name, email, password, pin, birth_date, initial_balance)
        self.users[email] = user
        print(f"Account created successfully for {name}!")
        return True

    def login(self, email, password):
        """Logs in a user by verifying their credentials."""
        user = self.users.get(email)
        if not user:
            print("No account found with this email.")
            return None

        if not user.verify_password(password):
            print("Incorrect password.")
            return None

        print(f"Welcome back, {user.name}!")
        return user

    def __str__(self):
        return "\n".join([str(user) for user in self.users.values()])


# Main function for user interaction
def main():
    bank = Bank()
    while True:
        print("\nWelcome to the Bank!")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")

        choice = input("Please select an option: ")

        if choice == "1":
            # Creating a new account
            print("\n--- Create a New Account ---")
            email = input("Enter your email: ")
            
            if email in bank.users:
                print("An account with this email already exists.")
                continue

            birth_date = input("Enter your birth date (YYYY-MM-DD): ")
            if not re.match(r"\d{4}-\d{2}-\d{2}", birth_date) or int(birth_date.split('-')[0]) < 1800:
                print("Invalid birth date. Ensure correct format (YYYY-MM-DD) and that year is greater than 1800.")
                continue

            name = input("Enter your name: ")
            pin = input("Enter a 4-digit PIN: ")
            if not (pin.isdigit() and len(pin) == 4):
                print("PIN must be a 4-digit number.")
                continue

            password = input("Enter your password (at least 6 characters): ")
            if len(password) < 6:
                print("Password must be at least 6 characters long.")
                continue

            bank.create_account(name, email, password, pin, birth_date, 0.0)
            print("You have successfully entered your password.")

        elif choice == "2":
            # Logging in
            print("\n--- Login to Your Account ---")
            email = input("Enter your email: ")
            password = input("Enter your password: ")

            user = bank.login(email, password)
            if user:
                # Logged in successfully
                while True:
                    print(f"\nHello, {user.name}!")
                    print(f"You have ${user.balance:.2f} in your account.")
                    print("1. Deposit Money")
                    print("2. Withdraw Money")
                    print("3. Check Balance")
                    print("4. Logout")

                    action = input("Choose an action: ")

                    if action == "1":
                        amount = float(input("Enter amount to deposit: "))
                        user.deposit(amount)

                    elif action == "2":
                        amount = float(input("Enter amount to withdraw: "))
                        user.withdraw(amount)

                    elif action == "3":
                        print(f"Your current balance is: ${user.balance:.2f}")

                    elif action == "4":
                        print("Logging out...")
                        break

        elif choice == "3":
            print("Thank you for using our bank. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
