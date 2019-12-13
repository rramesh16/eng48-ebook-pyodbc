from db_books import *
books_table = EbooksBooks()


print("///Welcome!///")

while True:
    print('Please choose from the options below:')
    print("1: List all ebooks")
    print("2: Search for an ebook by name")
    print("3: Add a new ebook to the system")
    user_input = input("Please enter the option number...")

    if user_input == '1':
        print('Listing all ebooks...')
        books_table.print_all()

    elif user_input == '2':
        books_table.search_by_name()

    elif user_input == '3':
        print('Add an ebook to the system')
        books_table.add_book()

    elif 'bye' in user_input or 'exit' in user_input:
        print ('Goodbye!')
        break

    else:
        print("I didn't quite get that. Please choose from the available options")

