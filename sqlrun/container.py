class Container:

    def __init__(self, processor, processes):
        self._processor = processor
        self._processes = processes

    def run(self):
        for process in self._processes:
            process.run()
