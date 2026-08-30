import json

from google.adk.agents import LlmAgent
from google.adk.apps import App


def get_menu() -> str:
    """Retrieves the coffee shop menu from menu.json."""
    try:
        with open("menu.json", "r") as f:
            menu_data = json.load(f)
            return json.dumps(menu_data)
    except Exception as e:
        return json.dumps({"error": f"Could not retrieve menu: {str(e)}"})


barista_agent = LlmAgent(
    name="barista_agent",
    model="gemini-3.5-flash",
    instruction="""You are a friendly barista at Coffee Shop.

Your job is to recommend drinks and pastries based on customer preferences.

Rules:
1. Recommend items only from the menu returned by get_menu().
2. Do not invent menu items.
3. If the preference is unclear, ask one friendly clarifying question.
4. Use the menu descriptions, tags, and allergens when recommending.
5. Keep responses helpful and concise.
""",
    tools=[get_menu],
)


app = App(
    name="coffee_barista_app",
    root_agent=barista_agent,
)
