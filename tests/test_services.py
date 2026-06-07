import pytest
from src.services import UserService, ProjectService

def test_user_service():
    service = UserService()
    user = service.create_user("testuser", "test@example.com")
    assert user.username == "testuser"
    assert user.email == "test@example.com"
    
    found = service.get_user(user.id)
    assert found is not None
    assert found.username == "testuser"

def test_project_service():
    service = ProjectService()
    project = service.create_project("Test Project", 1, "Description")
    assert project.name == "Test Project"
    assert project.owner_id == 1
