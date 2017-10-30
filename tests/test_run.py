import unittest
from unittest import mock

from jenkinsutils.run import *

ADDR = "http://192.168.1.1:8080"
BAD_CONFIG_REGEX = ".*?plugins-download.*?job-create"

class TestRun(unittest.TestCase):

    def setUp(self):
        self.arg_parser_patch = mock.patch("jenkinsutils.run.argparse.ArgumentParser")
        mock_arg_parser = self.arg_parser_patch.start()
        self.mock_args = mock_arg_parser.return_value.parse_args

    def tearDown(self):
        self.arg_parser_patch.stop()

    def test_parse_args_returns_parse_args_value(self):
        args = mock.MagicMock(server_address = ADDR, cmd = "job-create")
        self.mock_args.return_value = args
        self.assertEqual(args, parse_args())

    def test_parse_args_with_job_create_cmd_requires_config(self):
        args = mock.MagicMock(server_address = ADDR, cmd = "job-create")
        self.assertRaisesRegex(ValueError, BAD_CONFIG_REGEX, parse_args)

    def test_parse_args_with_plugins_download_cmd_requires_config(self):
        args = mock.MagicMock(server_address = ADDR, cmd = "plugins-download")
        self.assertRaisesRegex(ValueError, BAD_CONFIG_REGEX, parse_args)

    def test_parse_args_with_plugins_list_cmd_cannot_have_config(self):
        args = mock.MagicMock(server_address = ADDR, cmd = "plugins-list",
            config="myfile.json")
        self.assertRaisesRegex(ValueError, BAD_CONFIG_REGEX, parse_args)

    def test_parse_args_with_job_status_cmd_cannot_have_config(self):
        args = mock.MagicMock(server_address = ADDR, cmd = "job-status", )
        self.assertRaisesRegex(ValueError, BAD_CONFIG_REGEX, parse_args)

