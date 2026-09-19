"""
Q2. Create a class Book with following attributes:
- title
- author
- list of reviews (each review is a string)

And add methods to:
- add a new review
- count the number of reviews
- display all reviews
"""

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.reviews = []

    def add_review(self, review):
        self.reviews.append(review)
        print(f"Review added: {review}")

    def count_reviews(self):
        return len(self.reviews)

    def display_reviews(self):
        if not self.reviews:
            print("No reviews available.")
        else:
            print(f"Reviews for '{self.title}' by {self.author}:")
            for idx, review in enumerate(self.reviews, start=1):
                print(f"{idx}. {review}")

# Example usage
book = Book("The Great Gatsby", "F. Scott Fitzgerald")
book.add_review("A timeless classic!")
book.add_review("Beautifully written, but a bit overrated.")
print(f"Total reviews: {book.count_reviews()}")
book.display_reviews()
