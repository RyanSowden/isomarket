import flask
from flask import Flask, request, session
import pytest
from app import app
   
   
   
@pytest.fixture()
def client():
    return app.test_client()

def test_getWorker(client):
    with app.test_client() as c:
        with c.session_transaction() as sess:
            sess['user'] = True
    data ={"worker":"Marisee"}
    url = 'http://localhost:5000/home'
    response = c.get(url, data=data)
    assert response.status_code == 200

def test_noLogin_getWorker(client):
    data ={"worker":"Marisee"}
    url = 'http://localhost:5000/home'
    response = client.get(url, data=data)
    assert response.status_code == 401
