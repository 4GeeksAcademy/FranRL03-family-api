
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint


class FamilyStructure:

    def __init__(self, last_name):
        self.last_name = last_name
        self._members = [{'id': 1, 'first_name': 'John', 'last_name': self.last_name ,'age': 33, 'lucky_number': [7, 13, 22]},
                         {'id': self._generate_id(), 'first_name': 'Jane', 'last_name': self.last_name,  'age': 35, 'lucky_number': [10, 14, 32]},
                         {'id': self._generate_id(), 'first_name': 'Jimmy', 'last_name': self.last_name,  'age': 5, 'lucky_number': [1]}]  # Example list of members

    # Read-only: Use this method to generate random members ID's when adding members into the list
    def _generate_id(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # Fill this method and update the return
        member["id"] = self._generate_id()
        member["last_name"] = self.last_name
        self._members.append(member)
        return 

    def delete_member(self, id):
        # Fill this method and update the return
        self._members = [member for member in self._members if member['id'] != id]
        return self._members

    def get_member(self, id):
        # Fill this method and update the return
        member = [member for member in self._members if member["id"] == id]
        return member

    # This method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
