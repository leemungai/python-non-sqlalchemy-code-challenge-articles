class Article:
    all = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str) and 5 <= len(title)  <= 50 and not hasattr(self, "title"):
            self._title = title
        else:
            return None
        
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author 
        else:
            return None
        
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, magazine):
        if isinstance(magazine, Magazine):
            self._magazine = magazine 
        else:
            return None
class Author:
    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and name and not hasattr(self, "name"):
            self._name = name
        else:
            return None
            

    def articles(self):
        return [article for article in Article.all if article.author is self]
        

    def magazines(self):
        return list(set(article.magazine for article in self.articles))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        pass

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 2 <= len(name)  <= 16:
            self._name = name
        else:
            return None
    def articles(self):
        return [article for article in Article.all if article.magazine is self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        return ([article.title for article in self.articles()]
        if self.articles()
        else None)

    def contributing_authors(self):
        return [article.author for article in self.articles()]
    
    @classmethod
    def top_publisher(cls):
        return (
            max((mbuku for mbuku in {article.magazine for article in Article.all}), key=lambda magazine: len(magazine.articles()))
            if Article.all
            else None)