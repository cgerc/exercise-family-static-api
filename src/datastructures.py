class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 3  # Comienza en 3 porque ya hay 3 miembros con IDs 0, 1, 2
        self._members = [
            {
                "id": 0,
                "first_name": "John",
                "last_name": last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": 1,
                "first_name": "Jane",
                "last_name": "Jackson",
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id": 2,
                "first_name": "Jimmy",
                "last_name": "Jackson",
                "age": 5,
                "lucky_numbers": [1]
            },
        ]

    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        member["id"] = self._generate_id()
        member["last_name"] = self.last_name
        if "lucky_numbers" not in member:
            member["lucky_numbers"] = []
        self._members.append(member)
        print("Añadir miembro:", member)
        return member  # Devuelve solo el miembro agregado, no toda la lista

    def delete_member(self, id):
        for i, member in enumerate(self._members):
            if member["id"] == id:
                self._members.pop(i)
                print(f"Miembro con id {id} eliminado")
                return True
        print(f"Miembro con id {id} no encontrado")
        return False

    def get_member(self, id):
        for member in self._members:
            if member["id"] == id:
                return member
        return None

    def get_all_members(self):
        return self._members