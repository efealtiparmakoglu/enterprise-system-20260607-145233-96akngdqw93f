from typing import List, Optional
from src.models import User, Project

class UserService:
    def __init__(self):
        self.users = []
    
    def create_user(self, username: str, email: str) -> User:
        user = User(id=len(self.users)+1, username=username, email=email)
        self.users.append(user)
        return user
    
    def get_user(self, user_id: int) -> Optional[User]:
        for user in self.users:
            if user.id == user_id:
                return user
        return None
    
    def list_users(self) -> List[User]:
        return self.users

class ProjectService:
    def __init__(self):
        self.projects = []
    
    def create_project(self, name: str, owner_id: int, description: str = None) -> Project:
        project = Project(
            id=len(self.projects)+1,
            name=name,
            owner_id=owner_id,
            description=description
        )
        self.projects.append(project)
        return project
