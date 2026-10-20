""" Creates the parent class Publication where the title, author, and methods are defined. """
class Publication:
    """Defines the title and author of the publication."""
    def __init__(self, title, author): 
        self.title = title
        self.author = author
    
    def get_title(self): 
        """Gets the title"""
        return self.title
    
    def get_author(self): 
        """Gets the name of the author"""
        return self.author
    
    def set_title(self, title):
        """Sets the title of the publication."""
        self.title = title
    
    def set_author(self, author):
        """Sets the author of the publication."""
        self.author = author
    
    def display_info(self):
        """Displays the title and author of the publication."""
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")

""" Creates the child class Book that inherits from Publication. """
class Book(Publication):
    """"Defines the title, author, and number of pages of the book."""
    def __init__(self, title, author, number_of_pages):
        """ Acts as like a copy paste of the parent class Publication and adds the number_of_pages attribute. """
        super().__init__(title, author)
        self.number_of_pages = number_of_pages
    
    def get_number_of_pages(self):
        """Gets the number of pages in the book."""
        return self.number_of_pages
    
    def set_number_of_pages(self, number_of_pages):
        """Sets the number of pages in the book."""
        self.number_of_pages = number_of_pages
    
""" Creates the child class Magazine that inherits from Publication. """
class Magazine(Publication):
    """Defines the title, author, and issue number of the magazine."""
    def __init__(self, title, author, issue_number):
        "Same definition in line 32 but instead of adding number_of_pages, it adds issue_number."
        super().__init__(title, author)
        self.issue_number = issue_number
    
    def get_issue_number(self):
        """Gets the issue number of the magazine."""
        return self.issue_number
    
    def set_issue_number(self, issue_number):
        """Sets the issue number of the magazine."""
        self.issue_number = issue_number
    
"""These are the inputs for the classes and the print statements to display the information."""
"""These are the inputs for the classes and the print statements for the superclass Publication"""   
publication=Publication("Journal of Experimental Psychology", "Ratchiff, R. Van Dongen, H.") 
"""These are the inputs for the classes and the print statements for the subclass Book"""
book=Book("The Hobbit", "J.R.R. Tolkien", 310)
"""These are the inputs for the classes and the print statements for the subclass Magazine"""
magazine=Magazine("National Geographic", "Various Authors", 202)
"""Prints publication information, acting like a subtitle"""
print("Publication information:")
"""Prints the display info of the superclass Publication"""
publication.display_info()
"""Prints book information, acting like a subtitle and adding \n to create a new line making the code much cleaner"""
print("\nBook information:")
"""Prints the display info of the subclass Book"""
book.display_info()
"""Prints the number of pages in the book using the get_number_of_pages method, seperated from display info because it is a unique attribute of the subclass Book"""
print(f"Number of Pages: {book.get_number_of_pages()}")
"""Prints magazine information, acting like a subtitle and adding \n to create a new line making the code much cleaner"""
print("\nMagazine information:")
"""Prints the display info of the subclass Book"""
magazine.display_info()
"""Prints the issue number of the magazine using the get_issue_number method, seperated from display info because it is a unique attribute of the subclass Magazine"""
print(f"Issue Number: {magazine.get_issue_number()}")
    
