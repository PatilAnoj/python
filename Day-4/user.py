class User:
    def __init__(self,name,email):
        self.name=name
        self.email=email
        self.is_active=True

    def deactivate(self):
        self.is_active=False

    def get_profile(self):
        return {
            "name":self.name,
            "email":self.email,
            "is_active":self.is_active
        }
    
