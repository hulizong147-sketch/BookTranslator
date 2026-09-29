

class Page:
    """
    代表书里面的一页内容
    """

    def __init__(self):
        self.content = []

    def add_content(self, content):
        self.content.append(content)