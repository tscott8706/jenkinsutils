from distutils.core import setup

package_name = "jenkinsutils"
setup(
    name = package_name,
    version = "1.0.0",
    description = "Some utilities for Jenkins using the jenkinsapi library",
    author = "Tim Scott",
    author_email = "tim@developerautomation.com",
    install_requires = ["jenkinsapi"],
    url = "https://github.com/tscott8706/jenkinsutils",
    packages = [package_name],
    entry_points = {
        "console_scripts": [
            "jenkinsutils = jenkinsutils.run:run"
        ]
    },
)
