"""!
Module to test the functionality of the get_user_info module.
"""
import unittest
from get_user_info import getUserInfo


class TestGetUserInfo(unittest.TestCase):
    """!
    @brief A class to test the getUserInfo function.
    """

    def test_correct_repo_list(self):
        """!
        @test Test that the function returns the correct number of repositories.
        """
        result = getUserInfo('kylerobots')
        self.assertEqual(
            len(result), 11, 'Wrong number of repositories reported.')

    def test_correct_commit_count(self):
        """!
        @test Test that the function correctly counts the number of commits for a repo.
        """
        result = getUserInfo('kylerobots')
        self.assertNotEqual(len(result), 0)
        # Pick two of the repositories
        self.assertEqual(result['algorithms'], 30,
                         'Repository reports the wrong number of commits.')
        self.assertEqual(result['ssw567-triangle-classification'],
                         10, 'Repository reports the wrong number of commits.')

    def test_correct_types(self):
        """!
        @test Test that the function returns the correct types specified by the documentation.
        """
        result = getUserInfo('kylerobots')
        self.assertTrue(isinstance(result, dict), 'Wrong datatype reported.')

    def test_wrong_user(self):
        """!
        @test Test that entering a nonexistant user returns an empty dict.
        """
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
