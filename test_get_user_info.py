"""!
Module to test the functionality of the get_user_info module.
"""
import json
import unittest
from unittest.mock import Mock, patch
from get_user_info import getUserInfo


class TestGetUserInfo(unittest.TestCase):
    """!
    @brief A class to test the getUserInfo function.
    """

    @patch('requests.get')
    def test_correct_repo_list(self, injected_mock):
        """!
        @test Test that the function returns the correct number of repositories.
        """
        mock_responses = [Mock(), Mock()]
        mock_responses[0].status_code = 200
        mock_responses[0].json.return_value = json.loads('[{"name": "repo1"}]')
        mock_responses[1].status_code = 200
        mock_responses[1].json.return_value = json.loads(
            '[{"commit": "com1"}]')
        injected_mock.side_effect = mock_responses
        result = getUserInfo('kylerobots')
        self.assertEqual(
            len(result), 1, 'Wrong number of repositories reported.')

    @patch('requests.get')
    def test_correct_commit_count(self, injected_mock):
        """!
        @test Test that the function correctly counts the number of commits for a repo.
        """
        mock_responses = [Mock(), Mock(), Mock()]
        mock_responses[0].status_code = 200
        mock_responses[0].json.return_value = json.loads(
            '[{"name": "algorithms"}, {"name": "ssw567-triangle-classification"}]')
        mock_responses[1].status_code = 200
        mock_responses[1].json.return_value = json.loads(
            '[{"commit": "com1"}]')
        mock_responses[2].status_code = 200
        mock_responses[2].json.return_value = json.loads(
            '[{"commit": "com1"}, {"commit": "com2"}]')
        injected_mock.side_effect = mock_responses
        result = getUserInfo('kylerobots')
        self.assertNotEqual(len(result), 0)
        # Pick two of the repositories
        self.assertEqual(result['algorithms'], 1,
                         'Repository reports the wrong number of commits.')
        self.assertEqual(result['ssw567-triangle-classification'],
                         2, 'Repository reports the wrong number of commits.')

    @patch('requests.get')
    def test_correct_types(self, injected_mock):
        """!
        @test Test that the function returns the correct types specified by the documentation.
        """
        injected_mock.return_value.status_code = 200
        injected_mock.return_value.json.return_value = json.loads('[]')
        result = getUserInfo('kylerobots')
        self.assertTrue(isinstance(result, dict), 'Wrong datatype reported.')

    @patch('requests.get')
    def test_wrong_user(self, injected_mock):
        """!
        @test Test that entering a nonexistant user returns an empty dict.
        """
        injected_mock.return_value.status_code = 200
        injected_mock.return_value.json.return_value = json.loads('[]')
        result = getUserInfo('kylerobots_does_not_exist')
        self.assertEqual(
            len(result), 0, 'Invalid user does not return empty dict')

    def test_wrong_input(self):
        """!
        @test Test that wrong input types raise errors
        """
        # I got this pattern from the documentation for unittest.
        with self.assertRaises(TypeError, msg='Function does not handle wrong types.'):
            getUserInfo(123)  # type: ignore


if __name__ == '__main__':
    unittest.main()
