import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_signup_and_unregister():
    # Use an activity with no initial participants for a clean test
    activity = "Drama Society"
    email = "testuser@example.com"
    # Sign up
    signup_resp = client.post(f"/activities/{activity}/signup?email={email}")
    assert signup_resp.status_code == 200
    # Unregister
    unregister_resp = client.post(f"/activities/{activity}/unregister?email={email}")
    assert unregister_resp.status_code == 200
    # Check participant removed
    activities = client.get("/activities").json()
    assert email not in activities[activity]["participants"]
