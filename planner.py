from datetime import datetime
import random

class TripRequest:
    def __init__(self, budget, start_date, end_date, traveler_type = None, destination = None):
        self.budget = budget
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d")
        self.end_date = datetime.strptime(end_date, "%Y-%m-%d")
        self.traveler_type = traveler_type
        self.destination = destination
        
    def duration_days(self):
        return (self.end_date - self.start_date).days + 1
    
def plan_trip(trip_request):
    plan = []
    for day in range(trip_request.duration_days()):
        plan.append({
            "day": day + 1,
            "activity": random.choice([
                "Explore loacal museum",
                "Visit a nature park",
                "Try local food tour",
                "Relax at the beach",
                "Go hiking in nearby trails"
            ])
        })
    
    return {
        "destination": trip_request.destination or "Suggested destinations will appear here",
        "budget": trip_request.budget,
        "days": trip_request.duration_days(),
        "traveler_type": trip_request.traveler_type,
        "plan": plan
    }