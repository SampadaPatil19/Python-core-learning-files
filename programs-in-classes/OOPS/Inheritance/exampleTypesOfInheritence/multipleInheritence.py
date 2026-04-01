# 2 base classes and 1 child class

class Writer:
    def __init__(self, writing_style):
        self.writing_style = writing_style

    def write(self):
        print("Writing in", self.writing_style, "style")

class Editor:
    def __init__(self, editing_tool):
        self.editing_tool = editing_tool

    def edit(self):
        print("Editing using", self.editing_tool)


class ContentCreator(Writer, Editor):
    def __init__(self, writing_style, editing_tool, platform):
        Writer.__init__(self, writing_style)
        Editor.__init__(self, editing_tool)
        self.platform = platform

    def show_creator(self):
        self.write()
        self.edit()
        print("Platform:", self.platform)


cc = ContentCreator("Narrative", "Grammarly", "YouTube")
cc.show_creator()