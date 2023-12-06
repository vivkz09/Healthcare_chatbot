
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class action_new_sym(Action):

    def name(self) -> Text:
        return "action_new_sym"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        sym=tracker.latest_message["text"]
        symFile=open('new_symptoms.txt','a+')
        symFile.write(sym)
        symFile.write('\n')
        symFile.close()
        dispatcher.utter_message(text="Symptom is noted, Sorry we do not have any reliable solution for your Symptom. kindly consult with the doctor ")

        return []
