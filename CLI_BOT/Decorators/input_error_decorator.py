from Exceptions.exceptions import DateException  

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Enter user name please."
        except IndexError:
            return "Give me name and phone please."
        except DateException:
            return "Incorrect date, should be format 'd.m.Y'"
        except Exception as e:
            return f"An unexpected error occurred: {str(e)}"

    return inner