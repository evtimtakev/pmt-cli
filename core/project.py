

class Project:  # Create a project type.It stores a project name and version

    def __init__(self, name, project_version):
        self.name = name
        self.project_version = project_version

    def __str__(self):  # Override print method
        """Overweight default print method."""
        template = "=========== \n Project name: {0} \n Project version: {1}\n =========== \n"

        return template.format(self.name, self.project_version)
