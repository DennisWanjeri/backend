#!/usr/bin/env python3
"""util test module"""
import unittest
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """
    unit tests for AccessNestedMap
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map, path, expected):
        """test access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
        ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """
        test exception 
        """
        self.assertRaises(KeyError)

class TestGetJson(unittest.TestCase):
    """tests utils.get_json returns expected result"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])

    def test_get_json(self, test_url, test_payload):
        """tests get_json for correct output"""
        #set mock method to have return value of payload"
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        with patch('requests.get', return_value=mock_response):
            real_response = get_json(test_url)
            self.assertEqual(real_response, test_payload)
            mock_response.json.assert_called_once()

class TestMemoize(unittest.TestCase):
    """Test memoize module"""
    def test_memoize(self):
        """test memoize function"""
        class TestClass:
            """Test_class"""
            def a_method(self):
                """always returns 42"""
                return 42

            @memoize
            def a_property(self):
                """calls a_method"""
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as patched:
            test_class = TestClass()
            mem_return = test_class.a_property
            mem_return = test_class.a_property

            self.assertEqual(mem_return, 42)
            patched.assert_called_once()
