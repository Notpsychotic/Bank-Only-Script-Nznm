# Basic Surveillance System
import time

class SurveillanceSystem:
    def __init__(self):
        self.log = []

    def detect_activity(self, activity):
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        self.log.append({'timestamp': timestamp, 'activity': activity})
        print(f"Activity detected: {activity} at {timestamp}")

    def show_log(self):
        for entry in self.log:
            print(f"{entry['timestamp']}: {entry['activity']}")

if __name__ == '__main__':
    system = SurveillanceSystem()
    system.detect_activity('Motion detected in the living room')
    system.detect_activity('Door opened in the garage')
    system.show_log()
