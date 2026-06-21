class Person:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def info(self):
        return f"{self.name}({self.role})"
    
class Media_Asset:
    def __init__(self, title, media_type, duration, file_size):
        self.title = title
        self.media_type = media_type
        self.duration = duration
        self.file_size = file_size

    def info(self):
        return f"{self.media_type}: {self.title} ({self.duration}, {self.file_size})"
    

class Task:
    def __init__(self, description):
        self.description = description
        self.assigned_to = None
        self.completed = False

    def assign(self, person):
        self.assigned_to = person
        return

    def mark_complete(self):
        self.completed = True
        return
    
    def info(self):
        status = None
        if self.completed == True:
            status = "completed"
        else:
            status = "incomplete"
        return f"{self.description} -- assigned to: {self.assigned_to.name}, status: {status}"
    
class Project:
    def __init__(self, title):
        self.title = title
        self.members = []
        self.assets = []
        self.tasks = []

    def add_member(self, person):
        self.members.append(person)
        return

    def add_asset(self, media_asset):
        self.assets.append(media_asset)
        return
    
    def add_task(self, task):
        self.tasks.append(task)

    def progress(self):
        status = 0
        for i in self.tasks:
            if i.completed == True:
                status += 1
            
        prog = status/len(self.tasks)

        return f"{prog*100}%"
    
    def summary(self):
        print(self.title)
        print("Members:")
        for i in self.members:
            print(i.name)
        print("\nAssets:")
        for i in self.assets:
            print(i.title)
        print("\nTasks:")
        for i in self.tasks:
            print(i.description)
        print(f"\nProgress: {self.progress()}")