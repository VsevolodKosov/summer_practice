import pytest
from source.generators.product import Product


@pytest.fixture
def get_product_generator():
    return Product()
