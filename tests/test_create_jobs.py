from io import StringIO
import unittest
from unittest import mock

from jenkinsutils.create_jobs import _parse_config, _get_job_config, create_jobs

JSON_FILE = """{
    "job1": ["repo1", "dir/to/Jenkinsfile"],
    "job2": ["repo2", "another/dir/Jenkinsfile"],
    "job3": ["repo3", "here/is/Jenkinsfile"]
}
"""

class TestCreateJobs(unittest.TestCase):

    @mock.patch("builtins.open")
    def test_parse_config_loads_json_config(self, mock_open):
        mock_open.return_value.__enter__.return_value = StringIO(JSON_FILE)
        config = _parse_config("filepath")
        self.assertTrue("job1" in config)
        self.assertTrue("job2" in config)
        self.assertTrue("job3" in config)
        self.assertEqual(config["job1"], ["repo1", "dir/to/Jenkinsfile"])
        self.assertEqual(config["job2"], ["repo2", "another/dir/Jenkinsfile"])
        self.assertEqual(config["job3"], ["repo3", "here/is/Jenkinsfile"])

    def test_get_job_config_contains_repo_and_jenkinsfile(self):
        repo = "myrepo"
        jenkinsfile = "my/Jenkinsfile"
        config = _get_job_config([repo, jenkinsfile])
        self.assertTrue(repo in config)
        self.assertTrue(jenkinsfile in config)

    @mock.patch("jenkinsutils.create_jobs._parse_config")
    @mock.patch("jenkinsutils.create_jobs._get_job_config")
    def test_create_jobs_calls_create_job_for_each_job_name(self,
        mock_get_job_config, mock_parse_config):
        mock_parse_config.return_value = {"job1": ["repo", "jfile"],
            "job2": ["repo", "jfile"]}
        mock_get_job_config.side_effect = ("config1", "config2")
        mock_srv = mock.MagicMock()
        create_jobs(mock_srv, "config_filepath")
        mock_srv.create_job.assert_any_call("job1", "config1")
        mock_srv.create_job.assert_any_call("job2", "config2")

