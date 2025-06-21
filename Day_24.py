from dataclasses import dataclass

@dataclass
class LibraryBook():
    title: str
    author: str
    ISBN_number: str
    publication_year: str

    def DisplayDetails(self):
        print("Book Details:")
        print(f"~ Title             : {self.title}")
        print(f"~ Author            : {self.author}")
        print(f"~ ISBN Number       : {self.ISBN_number}")
        print(f"~ Publication Year  : {self.publication_year}")

coffee_can_investing = LibraryBook(title = 'Coffee Can Investing',
                                   author = "Saurabh Mukherjea",
                                   ISBN_number = "256-1578496273",
                                   publication_year = '2014')
coffee_can_investing.DisplayDetails()