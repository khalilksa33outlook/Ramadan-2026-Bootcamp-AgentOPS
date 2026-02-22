# tools.py

def get_weather(city):
    """Simulates looking up weather data."""
    print(f"[TOOL] Querying weather API for {city}...")
    # Mock data
    if city.lower() == "london":
        return "Rainy, 15°C"
    elif city.lower() == "dubai":
        return "Sunny, 40°C"
    else:
        return "Unknown location"

def calculator(expression):
    """Simulates a calculation tool."""
    print(f"[TOOL] Calculating: {expression}")
    try:
        # unsafe eval used for simplicity only!
        return str(eval(expression)) 
    except:
        return "Error in calculation"