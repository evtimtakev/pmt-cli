from database import *
from obf import *


class Cli:  # Command line interface for creating Projects and tickets (JIRA LIKE TOOL)

    def __init__(self):  # Init cli command loop in constructor
        self.projects = {}
        self.selected_project = None
        self.db = Database()
        console_input = ''
        self.project_selector = 0

        # Connect to Mongo db cluster
        self.db.connect_to_database()

        # Implement event loop
        while console_input != 'exit':
            console_input = input('Enter command: ')
            self.parse_commands(console_input)

    def parse_commands(self, input_user):  # Parse user commands
        """Parse commands from user"""

        if input_user == "new project":
            self.project_selector += 1
            self.create_new_project()
        elif input_user == 'select project':
            select_project = input("Select a project(by name): ")
            self.selected_project = self.db.get_one({"name": select_project}, "projects")
            print("project selected")
        elif input_user == "new issue":
            if self.selected_project is None:
                self.select_project()

                self.create_new_issue()
        elif input_user == "list projects":
            self.list_projects()
        elif input_user == "list issues":
            if self.selected_project is None:
                self.select_project()

            self.list_project_issues()
        elif input_user == "exit":
            print("Exiting.....")
        else:
            print('?')

    def list_projects(self):  # List all projects in DB
        """List all projects"""

        all_documents = self.db.list_all_documents("projects")
        for document in all_documents:
            project = ObjectFactory.get_instance_of("project", document)
            print(project)

    def list_project_issues(self):  # List projects issues
        """List projects issues"""

        all_documents = self.db.find({"project_id": self.selected_project["_id"]}, "issues")
        for document in all_documents:
            issue = ObjectFactory.get_instance_of("issue", document)
            print(issue)

    def create_new_issue(self):  # Create new issue for selected project
        """Create new issue for selected project"""

        user_input = {"type": input('What is the issue type: '), "status": input('What is the  issue status: '),
                      "title": input('Enter issue title: '), "description": input('Enter issue description: '),
                      'project_id': self.selected_project["_id"]}

        temporary_issue = ObjectFactory.get_instance_of("issue", user_input)
        self.db.insert_data(temporary_issue.__dict__, "issues")

    def create_new_project(self):  # Create new project
        """Create new project"""

        project_params = {"name": input("Enter project name: "), "project_version": input("Enter project version: "), "selector" : self.project_selector}
        project = ObjectFactory.get_instance_of("project", project_params)
        self.db.insert_data(project, "projects")
        self.selected_project = project
        print("Project created")

    def select_project(self):  # select project as default one for manipulations
        """select project as default one for manipulations"""

        select_project = input("Select a project(by name): ")
        self.selected_project = self.db.get_one({"name": select_project}, "projects")
