class Book:

    def __init__(self, title, ISBN, edition=1, author="", pages=0):
        self.title = title
        self.ISBN = ISBN
        self.edition = edition
        self.author = author
        self.pages = pages

    # title = ""
    # ISBN = 0
    # edition = 1
    # author = ""
    # pages = 0


book1 = Book(title="War of the Worlds", ISBN=1232432342, edition=1, author="Brendan", pages=300) # Instantiate

# book1.title = "War of the Worlds"
# book1.ISBN = 1232432342
# book1.edition = 1
# book1.author = "Brendan"
# book1.pages = 300

# book2 = Book()
# book2.title = "Zorro"
# book2.ISBN = 1232432338
# book2.edition = 1
# book2.author = "Nathalie"
# book2.pages = 287


inventory = []
inventory.append(book1)
#inventory.append(book2)

# Get the total number of pages of all books.

page_count = 0

for b in inventory:
    page_count += b.pages

print(page_count)