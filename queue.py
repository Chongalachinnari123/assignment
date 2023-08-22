class PrintSpoolerQueue:
    def __init__(self):
        self.queue = []

    def add_job(self, job):
        self.queue.append(job)
        print(f"Print job '{job}' added to the queue.")
        #print(len(self.queue))
    def process_print_jobs(self):
        while self.queue:
            job = self.queue.pop(0)
            print(f"Printing '{job}'...")
            print(f"Print job '{job}' completed.")
        #print(len(self.queue))
    def print_queue_status(self):
        print("Current Print Queue:")
        for job in self.queue:
            print(f"- {job}")

# Create an instance of the PrintSpoolerQueue class
spooler = PrintSpoolerQueue()
# Add print jobs to the queue
spooler.add_job("file1")
spooler.add_job("file2")

# Print the current queue status
spooler.print_queue_status()
# Process print jobs in the queue
print("Processing print jobs...")
spooler.process_print_jobs()
# Print the updated queue status
spooler.print_queue_status()