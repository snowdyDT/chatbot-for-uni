from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionSpravkaButtons(Action):
    def name(self) -> Text:
        return "action_spravka_buttons"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        buttons = [
            {"payload": "/mesta_ucheby_spravka", "title": "С места учебы"},
            {"payload": "/gosudarstvennye_posobiya_spravka", "title": "Государственные пособия (ГЦВП)"},
            {"payload": "/voenkomat_spravka", "title": "Для военкомата"}
        ]

        dispatcher.utter_message(text="Какая справка вам нужна?", buttons=buttons, button_type='vertical')

        return []


class ActionOnayButtons(Action):
    def name(self) -> Text:
        return "action_onay_buttons"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        buttons = [
            {"payload": "/kak_poluchit_onay", "title": "Как получить Онай?"},
            {"payload": "/poteryal_onay", "title": "Потерял Онай"},
            {"payload": "/kolledj_kak_poluchit_onay", "title": "Онай выпускникам колледжей"},
            {"payload": "/inostranec_kak_poluchit_onay", "title": "Онай иностранным студентам"},
        ]

        dispatcher.utter_message(text="Что вас интересует насчет 'Оңай'?", buttons=buttons, button_type='vertical')

        return []


class ActionCourseraButtons(Action):
    def name(self) -> Text:
        return "action_coursera_buttons"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        buttons = [
            {"payload": "/prosyat_oplatu_coursera", "title": "Просят произвести оплату"},
            {"payload": "/netu_priglachenie_coursera", "title": "Не могу найти приглашение"},
            {"payload": "/drugie_kursy_coursera", "title": "Могу ли я пройти другие курсы?"},
            {"payload": "/starye_kursy_coursera", "title": "Поменял специальность, а курсы старые"},
            {"payload": "/retake_coursera", "title": "Ретейк по Coursera"},
        ]
        dispatcher.utter_message(text="Что вас интересует по поводу Coursera?", buttons=buttons, button_type='vertical')

        return []


class ActionAcademMobButtons(Action):
    def name(self) -> Text:
        return "action_academ_mob_buttons"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        buttons = [
            {"payload": "/prosyat_oplatu_coursera", "title": "Что такое академическая мобильность?"},
            {"payload": "/netu_priglachenie_coursera", "title": "Критерии отбора"},
            {"payload": "/drugie_kursy_coursera", "title": "Сроки подачи"},
            {"payload": "/starye_kursy_coursera", "title": "Что получим при успешном окончании?"}
        ]
        dispatcher.utter_message(text="Что вас интересует по поводу академической мобильности?", buttons=buttons, button_type='vertical')

        return []

