# Fills a message template with a specific contact's actual details
class MessageBuilder:
    # Replaces text in the message with real values from the contact
    def build_message(self, message_template, contact):
        final_message = message_template

        variable_data = contact.get("variable_data", {})

        for key, value in variable_data.items():
            placeholder = "{{" + str(key) + "}}"
            final_message = final_message.replace(placeholder, str(value))

        return final_message
