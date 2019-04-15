# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.basic_column import BasicColumn
from openapi_server import util

from openapi_server.models.basic_column import BasicColumn  # noqa: E501

class CategoricalColumn(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, type=None, name=None, categories=None, percent_missing=None):  # noqa: E501
        """CategoricalColumn - a model defined in OpenAPI

        :param type: The type of this CategoricalColumn.  # noqa: E501
        :type type: str
        :param name: The name of this CategoricalColumn.  # noqa: E501
        :type name: str
        :param categories: The categories of this CategoricalColumn.  # noqa: E501
        :type categories: List[str]
        :param percent_missing: The percent_missing of this CategoricalColumn.  # noqa: E501
        :type percent_missing: float
        """
        self.openapi_types = {
            'type': str,
            'name': str,
            'categories': List[str],
            'percent_missing': float
        }

        self.attribute_map = {
            'type': 'type',
            'name': 'name',
            'categories': 'categories',
            'percent_missing': 'percent_missing'
        }

        self._type = type
        self._name = name
        self._categories = categories
        self._percent_missing = percent_missing

    @classmethod
    def from_dict(cls, dikt) -> 'CategoricalColumn':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CategoricalColumn of this CategoricalColumn.  # noqa: E501
        :rtype: CategoricalColumn
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self):
        """Gets the type of this CategoricalColumn.

        Тип колонки  # noqa: E501

        :return: The type of this CategoricalColumn.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CategoricalColumn.

        Тип колонки  # noqa: E501

        :param type: The type of this CategoricalColumn.
        :type type: str
        """
        allowed_values = ["ID", "NUMERIC", "CATEGORICAL"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def name(self):
        """Gets the name of this CategoricalColumn.

        Название колонки  # noqa: E501

        :return: The name of this CategoricalColumn.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CategoricalColumn.

        Название колонки  # noqa: E501

        :param name: The name of this CategoricalColumn.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def categories(self):
        """Gets the categories of this CategoricalColumn.

        Минимальное значение  # noqa: E501

        :return: The categories of this CategoricalColumn.
        :rtype: List[str]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this CategoricalColumn.

        Минимальное значение  # noqa: E501

        :param categories: The categories of this CategoricalColumn.
        :type categories: List[str]
        """
        if categories is None:
            raise ValueError("Invalid value for `categories`, must not be `None`")  # noqa: E501

        self._categories = categories

    @property
    def percent_missing(self):
        """Gets the percent_missing of this CategoricalColumn.

        Процент отсутствующих значений  # noqa: E501

        :return: The percent_missing of this CategoricalColumn.
        :rtype: float
        """
        return self._percent_missing

    @percent_missing.setter
    def percent_missing(self, percent_missing):
        """Sets the percent_missing of this CategoricalColumn.

        Процент отсутствующих значений  # noqa: E501

        :param percent_missing: The percent_missing of this CategoricalColumn.
        :type percent_missing: float
        """
        if percent_missing is None:
            raise ValueError("Invalid value for `percent_missing`, must not be `None`")  # noqa: E501

        self._percent_missing = percent_missing
