def test_create_one_planet(client):
    # Act
    response = client.post("/planets", json={
        "name": "ZigZag",
        "description": "A ziggy zaggy planet",
        "size": "Large"
        })
    response_body = response.get_json()
    
    # Assert 
    assert response.status_code == 201
    assert response_body['message'] == "Planet ZigZag successfully created"
    assert response_body['success'] == True

def test_get_one_planet(client, two_saved_planets):
    #Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    #Assert
    assert response.status_code == 200
    assert response_body["id"] == 1
    assert response_body["name"] == "Swirly Planet"
    assert response_body["description"] == "a swirl planet"
    assert response_body["size"] == "Small"