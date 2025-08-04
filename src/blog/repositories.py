import shelve
from abc import ABC, abstractmethod
from blog.domains import User, Admin, Article


class UserRepository(ABC):
    def get_users(self, username: str | None = None, password: str | None = None) -> list[User]:
        pass


class MemoryRepository(UserRepository):
    def __init__(self):
        self.users = [Admin(id="29ae7ebf-4445-42f2-9548-a3a54f095220", username='Admin228', password='legend')]

    def get_users(self, username: str | None = None, password: str | None = None) -> list[User]:
        filtered_users = []
        for user in self.users:
            if username is not None and user.username != username:
                continue
            if password is not None and user.password != password:
                continue
            filtered_users.append(user)
        return filtered_users


class ArticlesRepository(ABC):
    @abstractmethod
    def get_articles(self) -> list[Article]:
        pass

    def create_article(self, article: Article):
        pass


class ShelveArticleRepository(ArticlesRepository):
    def __init__(self):
        self.db_name = 'articles'

    def get_articles(self) -> list[Article]:
        with shelve.open(self.db_name) as db:
            return list(db.values())  # <- критично!

    def create_article(self, article: Article):
        with shelve.open(self.db_name) as db:
            db[article.id] = article


