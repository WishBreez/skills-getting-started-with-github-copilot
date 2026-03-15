def test_signup_is_immediately_visible_in_followup_activity_fetch(client):
    # Arrange
    activity = "Programming Class"
    email = "instant.visibility@mergington.edu"

    # Act
    signup_response = client.post(f"/activities/{activity}/signup", params={"email": email})
    activities_response = client.get("/activities")

    # Assert
    assert signup_response.status_code == 200
    assert email in activities_response.json()[activity]["participants"]


def test_unregister_is_immediately_visible_in_followup_activity_fetch(client):
    # Arrange
    activity = "Debate Club"
    email = "liam@mergington.edu"

    # Act
    unregister_response = client.delete(
        f"/activities/{activity}/participants",
        params={"email": email},
    )
    activities_response = client.get("/activities")

    # Assert
    assert unregister_response.status_code == 200
    assert email not in activities_response.json()[activity]["participants"]
