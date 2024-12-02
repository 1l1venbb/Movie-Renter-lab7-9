from calendar import monthrange


class Validations:

    def validateRentDate(self, day, month, year,):

        errors = ''

        if year < 2024 or year > 2025:
            errors += "Invalid year"
        if month < 1 or month > 12:
            errors += "Invalid month"
        if day < 1 or day > monthrange(year, month)[1]:
            errors += "Invalid day"

        if errors != "":
            raise ValueError(errors)