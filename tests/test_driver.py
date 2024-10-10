import sys
import argparse
import pytest
from unittest.mock import patch
from cbz_unzipper.driver import parse_arguments  # Update with the actual module name

@pytest.fixture
def mock_sys_argv():
    """Fixture to mock sys.argv"""
    original_argv = sys.argv
    yield
    sys.argv = original_argv

@patch('sys.argv', ['driver.py', '--input', 'input_folder', '--output', 'output_folder'])
def test_successful_parsing(mock_sys_argv):
    """Test if arguments are parsed correctly when all required arguments are provided"""
    args = parse_arguments()
    assert args.input == 'input_folder'
    assert args.output == 'output_folder'

@patch('sys.argv', ['driver.py', '--input', 'input_folder'])
def test_missing_output(mock_sys_argv):
    """Test behavior when required --output argument is missing"""
    with pytest.raises(SystemExit):  # Use SystemExit for argparse errors
        parse_arguments()

@patch('sys.argv', ['driver.py', '--output', 'output_folder'])
def test_missing_input(mock_sys_argv):
    """Test behavior when required --input argument is missing"""
    with pytest.raises(SystemExit):  # Use SystemExit for argparse errors
        parse_arguments()

@patch('sys.argv', ['driver.py'])
def test_no_arguments(mock_sys_argv):
    """Test behavior when no arguments are provided"""
    with pytest.raises(SystemExit):  # Use SystemExit for argparse errors
        parse_arguments()

# To run the tests, use the command: pytest <filename>.py
