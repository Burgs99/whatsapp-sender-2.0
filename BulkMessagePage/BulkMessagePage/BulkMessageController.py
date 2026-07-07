class BulkMessageController:

    def __init__(self, excel_manager, message_builder, message_randomizer, db_manager):
        self.excel_manager = excel_manager
        self.message_builder = message_builder
        self.message_randomizer = message_randomizer
        self.db_manager = db_manager

    def create_preview(self, contacts, message, randomise):

        if not contacts:
            raise ValueError("No contacts found.")

        if randomise:
            templates = message.split("\n")
            selected_message = self.message_randomizer.get_random_message(
                templates
            )
        else:
            selected_message = message

        first_contact = contacts[0]

        final_message = self.message_builder.build_message(
            selected_message,
            first_contact
        )

        return final_message


    def save_campaign(self, contacts, message, randomise, attachment, min_delay, max_delay):
        saved_count = 0

        for contact in contacts:
            if randomise:
               templates = message.split("\n")
               selected_message = self.message_randomizer.get_random_message(templates)
            else:
               selected_message = message

            final_message = self.message_builder.build_message(selected_message, contact)

            self.db_manager.save_bulk_message(
               contact["name"],
               contact["phone_number"],
               contact["variable_data"],
               final_message,
               attachment,
               int(min_delay),
               int(max_delay)
            )

            saved_count += 1

        return saved_count