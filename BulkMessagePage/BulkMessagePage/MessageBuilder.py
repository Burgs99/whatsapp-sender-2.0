class MessageBuilder:
    def build_message(self, message_template, contact):
        final_message = message_template

        variable_data = contact.get("variable_data", {})

        for key, value in variable_data.items():
            placeholder = "{{" + str(key) + "}}"
            final_message = final_message.replace(placeholder, str(value))

        return final_message