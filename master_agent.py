class MasterAgent:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def route_tasks(self):
        # Logic for routing tasks based on some criteria
        return sorted(self.tasks, key=lambda x: x.priority)

    def optimize_system(self):
        # Logic for optimizing system performance
        pass

if __name__ == '__main__':
    agent = MasterAgent()
    # Example usage
    agent.add_task(Task('Task 1', priority=2))
    agent.add_task(Task('Task 2', priority=1))
    routed_tasks = agent.route_tasks()
    print(routed_tasks)