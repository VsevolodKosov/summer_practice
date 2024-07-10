# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.models_product import ModelsProduct
from swagger_server import util


class ModelsProductsList(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, has_more: bool=None, page: int=None, products: List[ModelsProduct]=None, size: int=None, total_count: int=None, total_pages: int=None):  # noqa: E501
        """ModelsProductsList - a model defined in Swagger

        :param has_more: The has_more of this ModelsProductsList.  # noqa: E501
        :type has_more: bool
        :param page: The page of this ModelsProductsList.  # noqa: E501
        :type page: int
        :param products: The products of this ModelsProductsList.  # noqa: E501
        :type products: List[ModelsProduct]
        :param size: The size of this ModelsProductsList.  # noqa: E501
        :type size: int
        :param total_count: The total_count of this ModelsProductsList.  # noqa: E501
        :type total_count: int
        :param total_pages: The total_pages of this ModelsProductsList.  # noqa: E501
        :type total_pages: int
        """
        self.swagger_types = {
            'has_more': bool,
            'page': int,
            'products': List[ModelsProduct],
            'size': int,
            'total_count': int,
            'total_pages': int
        }

        self.attribute_map = {
            'has_more': 'hasMore',
            'page': 'page',
            'products': 'products',
            'size': 'size',
            'total_count': 'totalCount',
            'total_pages': 'totalPages'
        }

        self._has_more = has_more
        self._page = page
        self._products = products
        self._size = size
        self._total_count = total_count
        self._total_pages = total_pages

    @classmethod
    def from_dict(cls, dikt) -> 'ModelsProductsList':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The models.ProductsList of this ModelsProductsList.  # noqa: E501
        :rtype: ModelsProductsList
        """
        return util.deserialize_model(dikt, cls)

    @property
    def has_more(self) -> bool:
        """Gets the has_more of this ModelsProductsList.


        :return: The has_more of this ModelsProductsList.
        :rtype: bool
        """
        return self._has_more

    @has_more.setter
    def has_more(self, has_more: bool):
        """Sets the has_more of this ModelsProductsList.


        :param has_more: The has_more of this ModelsProductsList.
        :type has_more: bool
        """

        self._has_more = has_more

    @property
    def page(self) -> int:
        """Gets the page of this ModelsProductsList.


        :return: The page of this ModelsProductsList.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page: int):
        """Sets the page of this ModelsProductsList.


        :param page: The page of this ModelsProductsList.
        :type page: int
        """

        self._page = page

    @property
    def products(self) -> List[ModelsProduct]:
        """Gets the products of this ModelsProductsList.


        :return: The products of this ModelsProductsList.
        :rtype: List[ModelsProduct]
        """
        return self._products

    @products.setter
    def products(self, products: List[ModelsProduct]):
        """Sets the products of this ModelsProductsList.


        :param products: The products of this ModelsProductsList.
        :type products: List[ModelsProduct]
        """

        self._products = products

    @property
    def size(self) -> int:
        """Gets the size of this ModelsProductsList.


        :return: The size of this ModelsProductsList.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size: int):
        """Sets the size of this ModelsProductsList.


        :param size: The size of this ModelsProductsList.
        :type size: int
        """

        self._size = size

    @property
    def total_count(self) -> int:
        """Gets the total_count of this ModelsProductsList.


        :return: The total_count of this ModelsProductsList.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count: int):
        """Sets the total_count of this ModelsProductsList.


        :param total_count: The total_count of this ModelsProductsList.
        :type total_count: int
        """

        self._total_count = total_count

    @property
    def total_pages(self) -> int:
        """Gets the total_pages of this ModelsProductsList.


        :return: The total_pages of this ModelsProductsList.
        :rtype: int
        """
        return self._total_pages

    @total_pages.setter
    def total_pages(self, total_pages: int):
        """Sets the total_pages of this ModelsProductsList.


        :param total_pages: The total_pages of this ModelsProductsList.
        :type total_pages: int
        """

        self._total_pages = total_pages
