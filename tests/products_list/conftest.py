import pytest
from source.generators.products_list import ProductList


@pytest.fixture
def get_product_list_generator():
    return ProductList()
