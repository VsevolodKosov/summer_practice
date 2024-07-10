from generators.product import Product
from random import randint


class ProductList:
    def __init__(self, reset_is=True):
        self.result = {}

    def set_hasMore(self, hasMore=True):
        self.result["hasMore"] = hasMore
        return self

    def set_page(self, page=None, lie=True):
        if page is None and lie is True:
            self.result["page"] = randint(1, 100)
            return self

        self.result["page"] = page
        return self

    def set_products(self, products=[], lie=True, n=0):
        if len(products) == 0 and lie is True:
            if n == 0:
                n = randint(1, 5)
            products = [Product().build() for i in range(n)]
            self.result["products"] = products
            return self

        self.result["products"] = products
        return self

    def set_size(self, size=None, lie=True):
        if size is None and lie is True:
            self.result["size"] = randint(1, 100)
            return self

        self.result["size"] = size
        return self

    def set_totalCount(self, totalCount=None, lie=True):
        if totalCount is None and lie is True:
            self.result["totalCount"] = randint(1, 100)
            return self

        self.result["totalCount"] = totalCount
        return self

    def set_totalPages(self, totalPages=None, lie=True):
        if totalPages is None and lie is True:
            self.result["totalPages"] = randint(1, 5)
            return self

        self.result["totalPages"] = totalPages
        return self

    def reset(self):
        self.set_hasMore()
        self.set_page()
        self.set_size()
        self.set_totalPages()
        self.set_totalCount()
        self.set_products()

    def build(self):
        return self.result
