from flask import Flask, request, jsonify
from planner import TripRequest, plan_trip

app = Flask(__name__)

@app.route("/plan", methods = ["POST"])
def handle_plan():
    try:
        data = request.get_json()
        
        #extracting data from request
        budget = data["budget"]
        start_date = data["start_date"]
        end_date = data["end_date"]
        traveler_type = data["traveler_type"]
        destination = data["destination"]
        
        #creating a plan request obj
        trip_request = TripRequest(
            budget = budget,
            start_date = start_date,
            end_date = end_date,
            traveler_type = traveler_type,
            destination = destination
        )
        
        #creating the plan
        plan = plan_trip(trip_request)
        return jsonify(plan)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    
if __name__=="__main__":
    app.run(debug=True)