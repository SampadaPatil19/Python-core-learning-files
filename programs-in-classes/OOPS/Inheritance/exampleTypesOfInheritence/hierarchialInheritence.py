# 1 base class and multiple derived class

class Course:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration
    
    def show_course(self):
        print("Course Title:", self.title)
        print("Duration:", self.duration, "hours")


class OnlineCourse(Course):    # OnlineCourse IS-A Course
    def __init__(self, title, duration, platform):
        super().__init__(title, duration)
        self.platform = platform
    
    def show_online(self):
        self.show_course()
        print("Platform:", self.platform)


class OfflineCourse(Course):   # OfflineCourse IS-A Course
    def __init__(self, title, duration, location):
        super().__init__(title, duration)
        self.location = location
    
    def show_offline(self):
        self.show_course()
        print("Location:", self.location)


class HybridCourse(Course):    # HybridCourse IS-A Course
    def __init__(self, title, duration, platform, location):
        super().__init__(title, duration)
        self.platform = platform
        self.location = location
    
    def show_hybrid(self):
        self.show_course()
        print("Platform:", self.platform)
        print("Location:", self.location)

online = OnlineCourse("Python Mastery", 40, "Udemy")
offline = OfflineCourse("Data Science Bootcamp", 60, "Pune")
hybrid = HybridCourse("AI Pro Program", 80, "Coursera", "Mumbai")

online.show_online()
print()
offline.show_offline()
print()
hybrid.show_hybrid()
