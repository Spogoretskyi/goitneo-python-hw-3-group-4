from Exceptions.exceptions import DateError  

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Enter correct argumnt/s please."
        except IndexError:
            return "Give me name and phone please."
        except DateError as e:
            return f"{e}"
        except Exception as e:
            return f"An unexpected error occurred: {e}"

    return inner