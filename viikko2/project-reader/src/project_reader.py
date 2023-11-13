from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")


        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        parsed_content = toml.loads(content)
        printable_content = parsed_content['tool']['poetry']
        dependencies = printable_content['dependencies'].keys()
        dev_dependencies = printable_content['group']['dev']['dependencies'].keys()

        return Project(printable_content['name'], printable_content['description'], dependencies, dev_dependencies, printable_content['license'], printable_content['authors'])
