class Author:
    def __init__(self, name):
        # Ensure the name is a non-empty string
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string.")
        
        self._articles = []

    @property
    def name(self):
        return self._name

    def add_article(self, article):
        # Adds an article to the author's articles list
        self._articles.append(article)

    def articles(self):
        # Returns a list of all articles the author has written
        return self._articles

    def magazines(self):
        # Returns a unique list of magazines the author has contributed to
        return list(set(article.magazine for article in self._articles))

    def topic_areas(self):
        # Returns unique magazine categories the author has contributed to
        return list(set(article.magazine.category for article in self._articles)) if self._articles else None
