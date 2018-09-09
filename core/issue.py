class Issue:

    def __init__(self, issue_type, status, title, description, project_id):
        self.type = issue_type
        self.status = status
        self.title = title
        self.description = description
        self.project_id = project_id

    def __str__(self):  # Override print method
        template = "============== \n Issue type: {0}  \n Issue status: {1} \n Issue title: {2} \n Issue description: {3} \n ============== \n"

        return template.format(self.type, self.status, self.title, self.description)

    @staticmethod
    def get_status_dictionary(self):
        return self.issueStatusDic

    @staticmethod
    def get_type_dictionary(self):
        return self.issueTypeDic
