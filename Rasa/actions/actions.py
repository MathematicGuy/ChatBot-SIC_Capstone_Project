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
            dispatcher.utter_message(text="I'm sorry, I couldn't find your tech number. Could you please provide it?")
        elif not name or not city:
            dispatcher.utter_message(text="It seems I'm missing some of your details. Could you confirm your name and city?")
        else:
            dispatcher.utter_message(text=f"Hi {name}, I see that your city is {city} and your tech number is {tech_number}.")

        return []

class ActionGreetUser(Action):

    def name(self) -> Text:
        return "action_greet_user"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        name = tracker.get_slot("name")
        
        if name:
            dispatcher.utter_message(text=f"Hello {name}! How can I assist you today?")
        else:
            dispatcher.utter_message(text="Hello! How can I assist you today?")
        
        return []
