from faker import Faker
from random import randint

fake = Faker("en-US")


class Product:
    def __init__(self):
        self.result = {}
        self.reset()

    def set_description(self, description=None, lie=True):
        if isinstance(description, str) and lie is True:
            self.result["description"] = fake.text(max_nb_chars=10)
            return self

        self.result["description"] = description
        return self

    def set_name(self, name=None, lie=True):
        if isinstance(name, str) and lie is True:
            self.result["name"] = fake.text(max_nb_chars=10)
            return self

        self.result["name"] = name
        return self

    def set_price(self, price=None, lie=True):
        if isinstance(price, int) and lie is True:
            self.result[price] = randint(1, 100)
            return self

        self.result["price"] = price
        return self

    def set_quantity(self, quantity=None, lie=True):
        if isinstance(quantity, int) and lie is True:
            self.result[quantity] = randint(1, 100)
            return self

        self.result["quantity"] = quantity
        return self

    def set_rating(self, rating=None, lie=True):
        if isinstance(rating, int) and lie is True:
            self.result[rating] = randint(1, 10)
            return self

        self.result["rating"] = rating
        return self

    def set_CategoryId(self, CategoryId="", lie=True):
        if isinstance(CategoryId, str) and lie is True:
            self.result[CategoryId] = fake.text(max_nb_chars=10)
            return self

        self.result["categoryId"] = CategoryId
        return self

    def set_createdAt(self, createdAt="", lie=True):
        if isinstance(createdAt, str) and lie is True:
            self.result[createdAt] = fake.text(max_nb_chars=10)
            return self

        self.result["createdAt"] = createdAt
        return self

    def set_imageUrl(self, imageUrl="", lie=True):
        if isinstance(imageUrl, str) and lie is True:
            self.result[imageUrl] = fake.image_url()
            return self

        self.result["imageUrl"] = imageUrl
        return self

    def set_photos(self, items={}, lie=True):
        if isinstance(items, dict) and lie is True:
            self.result["items"] = {"photo": fake.image_url()}
            return self

        self.result["items"] = items
        return self

    def set_productId(self, productId="", lie=True):
        if isinstance(productId, str) and lie is True:
            self.result["productId"] = fake.text(max_nb_chars=10)
            return self

        self.result["productId"] = productId
        return self

    def set_updateAt(self, udpateAt="", lie=True):
        if isinstance(udpateAt, str) and lie is True:
            self.result["updateAt"] = fake.text(max_nb_chars=10)
            return self

        self.result["updateAt"] = udpateAt
        return self

    def reset(self):
        self.set_CategoryId()
        self.set_createdAt()
        self.set_description()
        self.set_imageUrl()
        self.set_name()
        self.set_photos()
        self.set_productId()
        self.set_quantity()
        self.set_rating()
        self.set_updateAt()
        self.set_price()
        return self

    def build(self):
        return self.result


p = Product().build()
print(p)
