def get_positive_int(prompt, min_val, max_val):
    """Read an integer within given bounds."""
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Value must be between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def get_urgency_level():
    """Read urgency level (Critical, High, Medium, Low)"""
    levels = ["Critical", "High", "Medium", "Low"]
    while True:
        urgency = input("Urgency level (Critical/High/Medium/Low): ").strip()
        if urgency in levels:
            return urgency
        else:
            print("Please enter: Critical, High, Medium, or Low.")

def main():
    print("Disaster Relief Resource Distribution System")
    print("-" * 50)

    # Input: total available resources
    total_resources = get_positive_int(
        "Enter total available resources (200–10000): ", 200, 10000
    )

    # Input: number of locations (3–500)
    n_locations = get_positive_int(
        "Enter number of locations (3–500): ", 3, 500
    )

    # Read requests: location_id, urgency, required_units
    requests = []
    for i in range(n_locations):
        loc_id = input(f"Enter location ID for request {i+1}: ").strip()

        req_units = get_positive_int(
            f"Units required for {loc_id} (50–1000): ", 50, 1000
        )

        urgency = get_urgency_level()

        requests.append({
            "id": loc_id,
            "units": req_units,
            "urgency": urgency
        })

    # Define urgency priority order
    urgency_rank = {
        "Critical": 0,
        "High": 1,
        "Medium": 2,
        "Low": 3
    }

    # Sort by urgency (Critical first, then High, etc.)
    sorted_requests = sorted(
        requests,
        key=lambda x: urgency_rank[x["urgency"]]
    )

    # Allocate resources
    allocation = {}
    pending = []
    remaining = total_resources

    for req in sorted_requests:
        loc_id = req["id"]
        needed = req["units"]

        if needed <= remaining:
            allocation[loc_id] = needed
            remaining -= needed
        else:
            pending.append(loc_id)

    # Display output
    print("\nOutput:")
    print(f"Resource Allocation: {allocation}")
    if pending:
        print(f"Pending Locations: {pending}")
    else:
        print("Pending Locations: []")

if __name__ == "__main__":
    main()
