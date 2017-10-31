import argparse
from jenkinsapi.jenkins import Jenkins

from jenkinsutils.create_jobs import create_jobs

_config_file_cmds = ("plugins-download", "job-create")

def parse_args():
    descr = "Setup a Jenkins server or get information about it"
    parser = argparse.ArgumentParser(description=descr)
    parser.add_argument("server_address", type=str, help="Jenkins URL and port")
    parser.add_argument("cmd", type=str, choices=("plugins-download","plugins-list",
        "job-create", "job-status"), help="Download plugins, list plugins, create jobs, "
        "or list the status of all jobs.  Downloading plugins and creating jobs "
        "requires a configuration file.")
    parser.add_argument("--config", type=str, help="Filepath to configuration file")

    args = parser.parse_args()
    _validate_args(args)
    return args

def _validate_args(args):
    config_must_be_none = (args.cmd not in _config_file_cmds)
    config_is_none = (args.config is None)
    if config_must_be_none != config_is_none:
        raise ValueError("Invalid arguments.  Config file must be given if and"
            f" only if the command is one of {_config_file_cmds}")

def run():
    args = parse_args()
    srv = Jenkins(args.server_address)
    {
        "job-create": lambda: create_jobs(srv, args.config)
    }[args.cmd]()
