from ...models import User

class CustomerRepository:

    def find_by_id(self, user_id):
        try:
            return User.objects.get(id=user_id, role="customer")
        except User.DoesNotExist:
            return None

    def find_by_email(self, email):
        try:
            return User.objects.get(email=email, role="customer")
        except User.DoesNotExist:
            return None

    def find_all(self):
        return User.objects.filter(role="customer")

    def update(self, user_id, updated_data):
        try:
            user = User.objects.get(id=user_id, role="customer")

            user.first_name = updated_data.get("first_name", user.first_name)
            user.last_name = updated_data.get("last_name", user.last_name)
            user.email = updated_data.get("email", user.email)
            user.status = updated_data.get("status", user.status)

            user.save()
            return user

        except User.DoesNotExist:
            return None

    def delete(self, user_id):
        try:
            user = User.objects.get(id=user_id, role="customer")

            # Soft delete (better than actual delete)
            user.status = "deleted"
            user.is_active = False
            user.save()

            return True

        except User.DoesNotExist:
            return False

