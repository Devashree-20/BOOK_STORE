def sort_books_alphabetically(books):
    """
    Sort the list of book objects alphabetically based on their titles.
    
    Args:
        books (list): A list of book objects.
        
    Returns:
        list: A sorted list of book objects.
    """
    sorted_books = sorted(books, key=lambda x: x.title)
    return sorted_books