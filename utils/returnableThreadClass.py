import threading as T

# create sub class for threads, so it can return results
class returningThread(T.Thread):
    def __init__(self, target):
        T.Thread.__init__(self)
        self.target = target
        self.result = None
    
    def run(self):
        self.result = self.target()

    def getResult(self):
        return self.result