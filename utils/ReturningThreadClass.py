import threading as T

class ValueReturningThread(T.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.result = None

    def run(self):
        # fire the target function with the reuqired arguments
        self.result = self._target(*self._args, **self._kwargs)
    

    def join(self, *args, **kwargs): # Call parent class' join method and return the result stored
        super().join(*args, **kwargs)
        return self.result