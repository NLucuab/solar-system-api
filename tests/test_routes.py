def test_create_one_planet(client):
    # Act
    response = client.post("/planets", json={
        "name": "ZigZag Planet",
        "description": "A ziggy zaggy planet"
        })
    response_body = response.get_json()
    
    # Assert 
    assert response.status_code == 201
    assert response_body == "ZigZag Planet successfully created"

def test_get_one_planet(client, two_saved_planets):
    #Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    #Assert
    assert response.status_code == 200
    assert response_body == {"id": 1, "title": "Swirly Planet", "description": "a swirl planet"}