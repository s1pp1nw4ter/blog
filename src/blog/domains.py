from dataclasses import dataclass


@dataclass
class User:
    id: str


@dataclass
class Admin(User):
    username: str
    password: str


@dataclass
class Article:
    id: str
    title: str
    content: str
