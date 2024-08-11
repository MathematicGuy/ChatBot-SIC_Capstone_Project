# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionSayData(Action):

    def name(self) -> Text:
        return "action_say_data"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        tech_number = tracker.get_slot("tech_number")
        name = tracker.get_slot("name")
        city = tracker.get_slot("city")
        
        if not tech_number:
            dispatcher.utter_message(text="I'm sorry, I couldn't find your information.")
        else:
            dispatcher.utter_message(text=f"Hi {name}, I see that your city is {city} and your neural id is {tech_number}.")

        return []

