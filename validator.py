def validate_record(name, age, email):
    if not name or not email:
        return False
    
    if not email.endswith("@gmail.com"):
        return False
    
    if not isinstance(age, int) or age <= 0:
        return False
    
    return True
