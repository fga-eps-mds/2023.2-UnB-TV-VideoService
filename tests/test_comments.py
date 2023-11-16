import pytest
from fastapi.testclient import TestClient

from src.main import app
from src.model import commentModel
from src.database import engine
from src.constants import errorMessages

client = TestClient(app)

comment = {
  'user_id': 1,
  'user_name': 'Lucas',
  'video_id': 1,
  'content': 'Comentario'
}

comment_update = {
  'content': 'Comentario Atualizado'
}

class TestVideoComment:
  @pytest.fixture(scope="session", autouse=True)
  def setup(self):
    response = client.post('/api/comments/', json=comment)
    data = response.json()
    assert response.status_code == 200
    assert data['user_id'] == comment['user_id']
    assert data['user_name'] == comment['user_name']
    assert data['video_id'] == comment['video_id']
    assert data['content'] == comment['content']

    yield
    
    commentModel.Base.metadata.drop_all(bind=engine)

  def test_root(self, setup):
    response = client.get('/')
    data = response.json()
    assert response.status_code == 200
    assert data["message"] == "Hello from Video Service"

  def test_comment_read_comment(self, setup):
    response = client.get('/api/comments/1')
    data = response.json()
    assert response.status_code == 200
    assert len(data) == 1
    assert data[0]['user_id'] == comment['user_id']
    assert data[0]['user_name'] == comment['user_name']
    assert data[0]['video_id'] == comment['video_id']
    assert data[0]['content'] == comment['content']

  def test_comment_update_comment_not_found(self, setup):
    response = client.patch('/api/comments/2', json=comment_update)
    data = response.json()
    assert response.status_code == 404
    assert data['detail'] == errorMessages.COMMENT_NOT_FOUND

  def test_comment_update_comment(self, setup):
    response = client.patch('/api/comments/1', json=comment_update)
    data = response.json()
    assert response.status_code == 200
    assert data['user_id'] == comment['user_id']
    assert data['user_name'] == comment['user_name']
    assert data['video_id'] == comment['video_id']
    assert data['content'] == comment_update['content']

  def test_comment_delete_comment_not_found(self, setup):
    response = client.delete('/api/comments/2')
    data = response.json()
    assert response.status_code == 404
    assert data['detail'] == errorMessages.COMMENT_NOT_FOUND
  
  def test_comment_delete_comment(self, setup):
    response = client.delete('/api/comments/1')
    data = response.json()
    assert response.status_code == 200
    assert data['user_id'] == comment['user_id']
    assert data['user_name'] == comment['user_name']
    assert data['video_id'] == comment['video_id']