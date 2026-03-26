class MemberCollection:
    """
    ADT for managing members.

    Internal Structure:
    - Dictionary (hidden from user)
    """

    def __init__(self):
        self._members = {}

    def add_member(self, member):
        if member.member_id in self._members:
            raise ValueError("Member already exists")

        self._members[member.member_id] = member

    def remove_member(self, member_id):
        if member_id not in self._members:
            raise KeyError("Member not found")

        member = self._members[member_id]

        if member.get_borrowed_books():
            raise ValueError("Member still has borrowed books")

        del self._members[member_id]

    def find_by_id(self, member_id):
        return self._members.get(member_id)

    def find_by_name(self, name):
        return [
            m for m in self._members.values()
            if name.lower() in m.name.lower()
        ]

    def get_all_members(self):
        return list(self._members.values())

    def count(self):
        return len(self._members)