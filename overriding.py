class Developer:
    def work(self):
        print("Developer is working")
    
    def attendMeeting(self):
        print("Developer is attending meeting")

class PyDeveloper(Developer):
    def work(self):
        print("Python is working on a project") #overiding method
    
    def doPythonProject(self):
        print("Python developer building python project") #child specific method

class JavaDeveloper(Developer):
    def work(self):
        print("Java developer is working") #overiding method

    def doJavaProject(self):
        print("Java developer building java project") #child specific method


dev= Developer()
dev.work()
dev.attendMeeting()

py= PyDeveloper()
py.work()
py.doPythonProject()
py.attendMeeting()

java= JavaDeveloper()
java.work()
java.doJavaProject()
java.attendMeeting()
