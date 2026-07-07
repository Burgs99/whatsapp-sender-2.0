from openpyxl import load_workbook


class ExcelManager:
    def read_contacts(self, file_path):
        workbook = load_workbook(file_path)
        sheet = workbook.active

        headers = []
        contacts = []

        for cell in sheet[1]:
            if cell.value:
                headers.append(str(cell.value).strip())

        if "Name" not in headers or "Phone Number" not in headers:
            raise ValueError("Excel file must contain 'Name' and 'Phone Number' columns.")

        name_index = headers.index("Name")
        phone_index = headers.index("Phone Number")

        for row in sheet.iter_rows(min_row=2, values_only=True):
            if not row or all(value is None for value in row):
                continue

            name = row[name_index] if name_index < len(row) else None
            phone_number = row[phone_index] if phone_index < len(row) else None

            if not name or not phone_number:
                continue

            variable_data = {}

            for index, header in enumerate(headers):
                if index < len(row):
                    variable_data[header] = row[index]

            contact = {
                "name": str(name).strip(),
                "phone_number": str(phone_number).strip(),
                "variable_data": variable_data
            }

            contacts.append(contact)

        return contacts