from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from typing import Dict
import sqlite3
from datetime import datetime, timedelta
import uuid

class SQLiteTrackerStore():
    def __init__(self, db_name='chatbot_for_uni.db', **kwargs: Dict):
        self.db_name = db_name
        self.conversation_states = {}

    def save(self, tracker: Tracker, dispatcher: CollectingDispatcher) -> None:
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()

        session_id = tracker.sender_id
        session_start = datetime.fromtimestamp(tracker.events[0].get('timestamp')).strftime('%Y-%m-%d-%H-%M-%S')

        last_processed_event_index = self.conversation_states.get(session_id, -1)

        for idx, event in enumerate(tracker.events[last_processed_event_index + 1:], start=last_processed_event_index + 1):
            if event.get("event") == "user":
                question_id = str(uuid.uuid4())
                question_time = datetime.fromtimestamp(event.get('timestamp')).strftime('%Y-%m-%d-%H-%M-%S')
                question = event.get('text')
                answer = None
                intent = event.get('parse_data').get('intent').get('name')
                confidence = event.get('parse_data').get('intent').get('confidence')
                rep_date = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

                # Find the next bot event and set the answer value
                for next_event in tracker.events[idx + 1:]:
                    if next_event.get("event") == "bot":
                        answer = next_event.get('text')
                        break

                data = {
                    'question_id': question_id,
                    'session_id': session_id,
                    'session_start': session_start,
                    'question_time': question_time,
                    'question': question,
                    'answer': answer,
                    'intent': intent,
                    'confidence': confidence,
                    'rep_date': rep_date
                }

                # If no result in the last day, insert data into the database
                c.execute('''
                    SELECT * FROM conversations 
                    WHERE session_id = :session_id 
                    AND question_time = :question_time 
                    AND question = :question
                    AND question_time >= :one_day_ago
                ''', {**data, 'one_day_ago': (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d-%H-%M-%S')})

                result = c.fetchone()

                # If no result, insert data into the database
                if not result:
                    c.execute('''
                        INSERT INTO conversations VALUES (
                            :question_id,
                            :session_id,
                            :session_start, 
                            :question_time, 
                            :question, 
                            :answer, 
                            :intent, 
                            :confidence, 
                            :rep_date
                        )
                    ''', data)

        # Update the conversation state
        self.conversation_states[session_id] = idx

        conn.commit()
        conn.close()
