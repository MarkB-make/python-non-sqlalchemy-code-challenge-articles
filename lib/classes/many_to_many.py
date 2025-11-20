# Represents an article written by an author for a magazine.
class Article:
    all = []  # Track all articles created
    
    def __init__(self, author, magazine, title):
        # Create a new article
        self.title = title
        self.author = author
        self.magazine = magazine
        Article.all.append(self)  # Register this article globally
    
    @property
    def title(self):
        # Get the article title
        return self._title
    
    @title.setter
    def title(self, value):
        # Set title only on creation. Must be a string between 5-50 characters.
        # Only allow setting once and validate it's a string of correct length
        if not hasattr(self, '_title') and isinstance(value, str) and 5 <= len(value) <= 50:
            self._title = value
    
    @property
    def author(self):
        # Get the article's author
        return self._author
    
    @author.setter
    def author(self, value):
        # Set the author. Must be an Author instance.
        if isinstance(value, Author):
            self._author = value
    
    @property
    def magazine(self):
        # Get the magazine this article is published in
        return self._magazine
    
    @magazine.setter
    def magazine(self, value):
        # Set the magazine. Must be a Magazine instance.
        if isinstance(value, Magazine):
            self._magazine = value
        
# Represents an author who writes articles for magazines.
class Author:
    
    def __init__(self, name):
        # Create an author with a name
        self.name = name
    
    @property
    def name(self):
        # Get the author's name
        return self._name
    
    @name.setter
    def name(self, value):
        # Set name only on creation. Must be a non-empty string.
        # Only allow setting once if not already set
        if hasattr(self, '_name'):
            return
        # Validate it's a non-empty string
        if isinstance(value, str) and len(value) > 0:
            self._name = value

    def articles(self):
        # Return all articles written by this author
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        # Return unique magazines this author has contributed to
        return list(set([article.magazine for article in self.articles()]))

    def add_article(self, magazine, title):
        # Create and return a new article for this author
        return Article(self, magazine, title)

    def topic_areas(self):
        # Return unique categories of magazines the author writes for, or None if no articles
        if not self.articles():
            return None
        return list(set([article.magazine.category for article in self.articles()]))

# Represents a magazine that publishes articles.
class Magazine:
    
    def __init__(self, name, category):
        # Create a magazine with a name and category
        self.name = name
        self.category = category
    
    @property
    def name(self):
        # Get the magazine's name
        return self._name
    
    @name.setter
    def name(self, value):
        # Set the magazine name. Can be changed. Must be 2-16 characters.
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
    
    @property
    def category(self):
        # Get the magazine's category
        return self._category
    
    @category.setter
    def category(self, value):
        # Set the magazine category. Can be changed. Must be a non-empty string.
        if isinstance(value, str) and len(value) > 0:
            self._category = value

    def articles(self):
        # Return all articles published in this magazine
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        # Return unique authors who have written for this magazine
        return list(set([article.author for article in self.articles()]))

    def article_titles(self):
        # Return list of article titles, or None if magazine has no articles
        if not self.articles():
            return None
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        # Return authors with more than 2 articles in this magazine, or None
        # Count how many articles each author has written for this magazine
        author_count = {}
        for article in self.articles():
            author_count[article.author] = author_count.get(article.author, 0) + 1
        
        # Filter to authors with more than 2 articles
        result = [author for author, count in author_count.items() if count > 2]
        return result if result else None
