import os
import pickle
import re

# Define a Contact class to store contact information
class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

# Define a ContactBook class to manage contacts
class ContactBook:
    def __init__(self, filename):
        self.contacts = {}
        self.filename = filename
        # Load contacts from file if it exists
        if os.path.exists(self.filename):
            with open(self.filename, "rb") as f:
                self.contacts = pickle.load(f)

    # Add a new contact to the book
    def add_contact(self, name, phone_number, email, address):
        # Check if contact already exists
        if name in self.contacts:
            print(f"\nContact with name {name} already exists.")
            return
        # Check if email is valid
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            print("\nInvalid email address.")
            return
        # Check if phone number is valid
        if not re.match(r"^[0-9-+() ]+$", phone_number):
            print("\nInvalid phone number.")
            return
        # Add contact to the book
        self.contacts[name] = Contact(name, phone_number, email, address)
        print(f"\nContact {name} added successfully.")

    # Edit an existing contact
    def edit_contact(self, name):
        # Check if contact exists
        if name not in self.contacts:
            print(f"\nNo contact found with the name {name}.")
            return
        # Prompt user for new contact information
        phone_number = input("Enter new phone number (leave blank to keep current): ")
        email = input("Enter new email (leave blank to keep current): ")
        address = input("Enter new address (leave blank to keep current): ")
        # Update contact information if provided
        if phone_number:
            if not re.match(r"^[0-9-+() ]+$", phone_number):
                print("\nInvalid phone number.")
                return
            self.contacts[name].phone_number = phone_number
        if email:
            if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                print("\nInvalid email address.")
                return
            self.contacts[name].email = email
        if address:
            self.contacts[name].address = address
        print(f"\nContact {name} updated successfully.")

    # Delete an existing contact
    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"\nContact {name} deleted successfully.")
        else:
            print(f"\nNo contact found with the name {name}.")

    # Search for a contact by name
    def search_contact(self, name):
        return self.contacts.get(name, None)

    # View all contacts in the book
    def view_all_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for contact in self.contacts.values():
                print(
                    f"\nName: {contact.name}\nPhone Number: {contact.phone_number}\nEmail: {contact.email}\nAddress: {contact.address}"
                )

    # Verify all contacts in the book for valid phone numbers and email addresses
    def verify_contacts(self):
        invalid_count = 0
        for contact in self.contacts.values():
            if not re.match(r"[^@]+@[^@]+\.[^@]+", contact.email):
                print(f"Invalid email address for contact {contact.name}.")
                invalid_count += 1
            if not re.match(r"^[0-9-+() ]+$", contact.phone_number):
                print(f"Invalid phone number for contact {contact.name}.")
                invalid_count += 1
        print(
            f"\nTotal contacts: {len(self.contacts)}\nInvalid fields: {invalid_count}"
        )

    # Save all contacts to file
    def save_contacts(self):
        with open(self.filename, "wb") as f:
            pickle.dump(self.contacts, f)

# Main function to run the program
def main():
    # Set filename for contact book
    filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), "contacts.pkl")
    # Create a new ContactBook object
    book = ContactBook(filename)
    while True:
        # Display menu options
        print("\n1: Add a new contact")
        print("2: Search for an existing contact")
        print("3: Delete a contact")
        print("4: View all contacts")
        print("5: Edit a contact")
        print("6: Verify all contacts")
        print("7: Exit the program")

        # Prompt user for choice
        choice = input("\nEnter your choice: ")

        # Execute selected option
        if choice == "1":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            book.add_contact(name, phone_number, email, address)

        elif choice == "2":
            name = input("Enter name: ")
            contact = book.search_contact(name)
            if contact:
                print(
                    f"\nName: {contact.name}\nPhone Number: {contact.phone_number}\nEmail: {contact.email}\nAddress: {contact.address}"
                )
            else:
                print("\nContact not found")

        elif choice == "3":
            name = input("Enter name: ")
            book.delete_contact(name)

        elif choice == "4":
            book.view_all_contacts()

        elif choice == "5":
            name = input("Enter the name of the contact you want to edit: ")
            book.edit_contact(name)

        elif choice == "6":
            book.verify_contacts()

        elif choice == "7":
            book.save_contacts()
            break

if __name__ == "__main__":
    main()