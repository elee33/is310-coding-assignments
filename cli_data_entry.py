from rich.console import Console
from rich.table import Table
import json
import os

# Create a Console instance
console = Console()

# Display pre-created example data
console.print("Here is some initial data:", style="bold cyan")

# Create a table with example data
table = Table(title="Favorite Books")
table.add_column("Title", style="magenta")
table.add_column("Author", style="cyan")
table.add_column("Published Year", justify="right")

# Add example rows to the table
table.add_row("1984", "George Orwell", "1949")
table.add_row("To Kill a Mockingbird", "Harper Lee", "1960")
table.add_row("The Great Gatsby", "F. Scott Fitzgerald", "1925")

# Display the table
console.print(table)

# Initialize a list to store user entries
user_entries = []

console.print("\n[bold cyan]Now I want you to enter your favorite books:[/bold cyan]")

# Collect data from the user
while True:
    # Collect data for each field
    book_title = console.input("Enter the title of the book: ")
    author = console.input("Enter the author of the book: ")
    published_year = console.input("Enter the published year of the book: ")

    # Store the data in a dictionary
    new_entry = {
        "Title": book_title,
        "Author": author,
        "Published Year": published_year
    }

    # Add the new entry to the list
    user_entries.append(new_entry)

    # Ask if the user wants to add another entry
    add_another = console.input("Do you want to add another book? (yes/no): ")
    if add_another.lower() != 'yes':
        break

# Confirm data with the user
confirmed_entries = []
for entry in user_entries:
    # Display the entry for confirmation
    console.print("\nYou entered the following book:")
    entry_table = Table(show_header=False)
    entry_table.add_row("Title:", entry["Title"])
    entry_table.add_row("Author:", entry["Author"])
    entry_table.add_row("Published Year:", entry["Published Year"])
    console.print(entry_table)

    # Ask for confirmation
    is_correct = console.input("Is this data correct? (yes/no): ")
    if is_correct.lower() == 'yes':
        confirmed_entries.append(entry)
    else:
        console.print("Let's re-enter the data for this book.")
        # Re-enter data
        book_title = console.input("Enter the title of the book: ")
        author = console.input("Enter the author of the book: ")
        published_year = console.input("Enter the published year of the book: ")
        # Update the entry
        entry["Title"] = book_title
        entry["Author"] = author
        entry["Published Year"] = published_year
        confirmed_entries.append(entry)

# Save the confirmed data to a JSON file
file_name = 'favorite_books.json'
file_path = os.path.abspath(file_name)

with open(file_name, 'w', encoding='utf-8') as jsonfile:
    json.dump(confirmed_entries, jsonfile, indent=4)

# Inform the user that the data has been saved
console.print(f"\nData has been saved to [bold green]{file_path}[/bold green]")

