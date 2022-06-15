import utils
import sorts

bookshelf = utils.load_books('books_small.csv')
bookshelf_v1 = bookshelf.copy()
bookshelf_v2 = bookshelf.copy()

long_bookshelf = utils.load_books('books_large.csv')

def by_title_ascending(book_a, book_b):
  return book_a['title_lower'] > book_b['title_lower']

def by_author_ascending(book_a, book_b):
  return book_a['author_lower'] > book_b['author_lower']

def by_total_length(book_a, book_b):
  return (len(book_a['title_lower'])+len(book_a['author_lower'])) > (len(book_b['title_lower'])+len(book_b['author_lower']))

# sort1 = sorts.bubble_sort(bookshelf, by_title_ascending)
# print(sort1)

# sort2 = sorts.bubble_sort(bookshelfv1, by_author_ascending)
# print(sort2)

# sorts.quicksort(bookshelf_v2, 0, len(bookshelf_v2) - 1,by_author_ascending)
# print(bookshelf_v2)

# sort4 = sorts.bubble_sort(long_bookshelf, by_total_length)
# print(sort4)

sorts.quicksort(long_bookshelf, 0, len(long_bookshelf) - 1,by_author_ascending)
print(long_bookshelf)
  
for book in bookshelf:
  print(book)