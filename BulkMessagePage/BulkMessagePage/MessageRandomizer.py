import random


class MessageRandomizer:
    def get_random_message(self, messages):
        valid_messages = []

        for message in messages:
            clean_message = message.strip()

            if clean_message:
                valid_messages.append(clean_message)

        if not valid_messages:
            raise ValueError("At least one message template is required.")

        return random.choice(valid_messages)