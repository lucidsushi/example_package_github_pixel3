#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `example_package_github_pixel3` package."""


import unittest
from click.testing import CliRunner

from example_package_github_pixel3 import example_package_github_pixel3
from example_package_github_pixel3 import cli


class TestExample_package_github_pixel3(unittest.TestCase):
    """Tests for `example_package_github_pixel3` package."""

    def setUp(self):
        """Set up test fixtures, if any."""
        self.test_message = "This is a test message for unittest"

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_test_message(self):
        """Test Print a Test Message"""
        test_message = example_package_github_pixel3.test_message()
        self.assertEqual(test_message, self.test_message)

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'example_package_github_pixel3.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
