# Run this cell in order to have these two dictionary variables defined.
tukey_paper = {
    "title": "The Future of Data Analysis",
    "author": "John W. Tukey",
    "link": "https://projecteuclid.org/euclid.aoms/1177704711",
    "year_published": 1962
}

thomas_paper = {
    "title": "A mathematical model of glutathione metabolism",
    "author": "Rachel Thomas",
    "link": "https://www.ncbi.nlm.nih.gov/pubmed/18442411",
    "year_published": 2008
}

book = {
    "title": "Genetic Algorithms and Machine Learning for Programmers",
    "price": 36.99,
    "author": "Frances Buontempo"
}

books = [
    {
        "title": "Genetic Algorithms and Machine Learning for Programmers",
        "price": 36.99,
        "author": "Frances Buontempo"
    },
    {
        "title": "The Visual Display of Quantitative Information",
        "price": 38.00,
        "author": "Edward Tufte"
    },
    {
        "title": "Practical Object-Oriented Design",
        "author": "Sandi Metz",
        "price": 30.47
    },
    {
        "title": "Weapons of Math Destruction",
        "author": "Cathy O'Neil",
        "price": 17.44
    }
]

# Exercise 87
# Write a function named get_paper_title that takes in a dictionary and returns the title property

def get_paper_title(dict):
    return dict['title']

assert get_paper_title(tukey_paper) == "The Future of Data Analysis"
assert get_paper_title(thomas_paper) == "A mathematical model of glutathione metabolism"
print("Exercise 87 is correct.")

# Exercise 88
# Write a function named get_year_published that takes in a dictionary and returns the value behind the "year_published" key.

def get_year_published(dict):
    return dict['year_published']

assert get_year_published(tukey_paper) == 1962
assert get_year_published(thomas_paper) == 2008
print("Exercise 88 is correct.")

# Exercise 89
# Write a function named get_price that takes in a dictionary and returns the price

def get_price(dict):
    return dict['price']

assert get_price(book) == 36.99
print("Exercise 89 is correct.")

# Exercise 90
# Write a function named get_book_author that takes in a dictionary (the above declared book variable) and returns the author's name

def get_book_author(dict):
    return dict['author']

assert get_book_author(book) == "Frances Buontempo"
print("Exercise 90 is correct.")

# Exercise 91
# Write a function named get_number_of_books that takes in a list of objects and returns the number of dictionaries in that list.

def get_number_of_books(books_list):
    return len(books_list)

assert get_number_of_books(books) == 4
print("Exercise 91 is correct.")

# Exercise 92
# Write a function named total_of_book_prices that takes in a list of dictionaries and returns the sum total of all the book prices added together

def total_of_book_prices(books_list):
    # return sum(book['price'] for book in books_list)
    total = 0
    for book_price in books_list:
        total += book_price['price']
    return total

assert total_of_book_prices(books) == 122.9
print("Exercise 92 is correct.")

# Exercise 93
# Write a function named get_average_book_price that takes in a list of dictionaries and returns the average book price.

def get_average_book_price(books_list):
    return sum(book['price'] for book in books_list) / len(books_list)

assert get_average_book_price(books) == 30.725
print("Exercise 93 is correct.")

# Exercise 94
# Write a function called highest_price_book that takes in the above defined list of dictionaries "books" and returns the dictionary containing the title, price, and author of the book with the highest priced book.
# Hint: Much like sometimes start functions with a variable set to zero, you may want to create a dictionary with the price set to zero to compare to each dictionary's price in the list

def highest_price_book(books_list):
    # faster when n is closer to 0
    # return max(books_list, key=lambda book: book['price'])
    
    #faster when n is further than 100
    highest_price_information = {
        "price": 0,
        "book_dict": {}
        }
    for book in books_list:
        if book['price'] > highest_price_information['price']:
            highest_price_information['price'] = book['price']
            highest_price_information['book_dict'] = book
    
    return highest_price_information['book_dict']
    

assert highest_price_book(books) == {
    "title": "The Visual Display of Quantitative Information",
    "price": 38.00,
    "author": "Edward Tufte"
}

print("Exercise 94 is correct.")