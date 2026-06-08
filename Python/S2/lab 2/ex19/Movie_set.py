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
    

