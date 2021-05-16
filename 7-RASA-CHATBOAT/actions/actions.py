from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
import re

class ValidateNameForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_name_form"

    def validate_first_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `first_name` value."""

        # If the name is super short, it might be wrong.
        print(f"First name given = {slot_value} length = {len(slot_value)}")
        if len(slot_value) <= 2:
            dispatcher.utter_message(text=f"That's a very short name. I'm assuming you mis-spelled.")
            return {"first_name": None}
        else:
            return {"first_name": slot_value}

    def validate_last_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `last_name` value."""

        # If the name is super short, it might be wrong.
        print(f"Last name given = {slot_value} length = {len(slot_value)}")
        if len(slot_value) <= 2:
            dispatcher.utter_message(text=f"That's a very short name. I'm assuming you mis-spelled.")
            return {"last_name": None}
        else:
            return {"last_name": slot_value}

    def validate_email(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate email value"""
        
        # if the email is super short, it might be wrong.
        print(f"Email given = {slot_value} length = {len(slot_value)}")
        if len(slot_value) <= 10:
            dispatcher.utter_message(text=f"That's a very short email. I'm assuming you mis-spelled.")
            return {"email": None}
        else:
            return {"email": slot_value}



    def isValid(s):
        # 1) Begins with 0 or 91
        # 2) Then contains 7 or 8 or 9.
        # 3) Then contains 9 digits
        Pattern = re.compile("(0/91)?[7-9][0-9]{9}")
        return Pattern.match(s)

    def validate_phone(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict
    ) -> Dict[Text, Any]:
        """Validate email value"""

        # if the email is super short, it might be wrong.
        print(f"Your requirement is wrong name given = {slot_value} length = {len(slot_value)}")
        if isValid(slot_value):
            return {"phone": slot_value}
        else:
            dispatcher.utter_message(text=f"Your phone number is not valid. Please enter valid phone.")
            return {"phone": None}