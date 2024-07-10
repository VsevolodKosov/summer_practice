import pytest
import requests


class TestProductBody:
    @pytest.mark.parametrize("name", ["some name", 1])
    def test_product_post_name(self, name, get_product_generator):
        url = "http://localhost:7070/api/v1/products/post"
        data = get_product_generator.set_name(lie=False, name=name).build()
        response = requests.post(url, data)
        assert response.status_code == 201

    @pytest.mark.parametrize("description", ["some description", 1])
    def test_product_post_description(self, description, get_product_generator):
        url = "http://localhost:7070/api/v1/products/post"
        data = get_product_generator.set_description(
            lie=False, description=description
        ).build()
        response = requests.post(url, data)
        assert response.status_code == 201

    @pytest.mark.parametrize("price", [15, "some price"])
    def test_product_post_price(self, price, get_product_generator):
        url = "http://localhost:7070/api/v1/products/post"
        data = get_product_generator.set_price(lie=False, price=price).build()
        response = requests.post(url, data)
        assert response.status_code == 201

    @pytest.mark.parametrize("quantity", [15, "some quantity"])
    def test_product_post_quantity(self, quantity, get_product_generator):
        url = "http://localhost:7070/api/v1/products/post"
        data = get_product_generator.set_quantity(lie=False, quantity=quantity).build()
        response = requests.post(url, data)
        assert response.status_code == 201

    @pytest.mark.parametrize("rating", [10, "some rating"])
    def test_product_post_rating(self, rating, get_product_generator):
        url = "http://localhost:7070/api/v1/products/post"
        data = get_product_generator.set_rating(lie=False, rating=rating).build()
        response = requests.post(url, data)
        assert response.status_code == 201
