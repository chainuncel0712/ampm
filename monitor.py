import psutil
import logging
import time

# Setup logging
logging.basicConfig(filename='system_monitor.log', level=logging.INFO)

class SystemMonitor:
    def __init__(self):
        self.performance_metrics = {}

    def monitor_health(self):
        # Monitor system health
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_info = psutil.virtual_memory()
        
        # Store performance metrics
        self.performance_metrics = {
            "cpu_usage": cpu_usage,
            "memory_used": memory_info.used,
            "memory_total": memory_info.total,
            "disk_usage": psutil.disk_usage('/').percent
        }
        
        # Log the metrics
        logging.info(f"CPU Usage: {cpu_usage}, Memory Used: {memory_info.used}, Memory Total: {memory_info.total}, Disk Usage: {psutil.disk_usage('/').percent}")

    def optimize_system(self):
        # Suggest optimizations based on metrics
        if self.performance_metrics["cpu_usage"] > 80:
            return "Consider closing resource-heavy applications."
        return "System performance is optimal."

    def detect_issues(self):
        # Proactive issue detection
        if self.performance_metrics["memory_used"] > self.performance_metrics["memory_total"] * 0.9:
            logging.warning("Memory usage is critically high!")

    def run(self):
        while True:
            self.monitor_health()
            suggestion = self.optimize_system()
            self.detect_issues()
            logging.info(f"Optimization Suggestion: {suggestion}")
            time.sleep(60)  # Run every minute

if __name__ == "__main__":
    monitor = SystemMonitor()
    monitor.run()
