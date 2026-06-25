"""Generate a day-by-day travel itinerary using Gemini based on destination, attractions, and weather forecast"""

import google.generativeai as genai

API_KEY = "AQ.Ab8RN6IIhEV12ZXn35gXfp9jbCOEE0Lgn_f4Gf4YdmZd7efPCg"
genai.configure(api_key = API_KEY)

def generate_ai_itinerary(destination, attractions, weather):
    model = genai.GenerativeModel("gemini-2.5-flash")
    prompt = f"""
    Create a short day-by-day travel itinerary for a trip to {destination}.

    Attractions to include: {attractions}
    Weather forecast: {weather}

    Spread the attractions across the trip days. On days with a high
    chance of rain, prefer indoor activities. Keep it friendly and concise.
    """
    response = model.generate_content(prompt)
    return response.text