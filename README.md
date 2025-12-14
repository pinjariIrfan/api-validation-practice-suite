# api-validation-practice-suite
REST API testing using Postman + Python 


```markdown
# API Validation Practice Suite

## Project Description
REST API testing practice suite using Postman for manual testing and Python Requests library for automation.

## Technologies Used
- Postman
- Python Requests
- REST API Testing
- JSON Validation

## Project Structure
```

api-validation-practice-suite/
├──postman_collections/   # Postman JSON exports
├──python_scripts/        # Python Requests scripts
├── test_data/             # Test data files
├──requirements.txt       # Dependencies
└──README.md             # Documentation

```

## Testing Coverage
- GET, POST, PUT, DELETE methods
- Status code validation
- Response body verification
- Error handling tests

## Execution
```bash
pip install -r requirements.txt
python python_scripts/test_apis.py
```

```

#### **3. Add requirements.txt**
```

requests==2.31.0
pytest==7.4.0
python-dotenv==1.0.0

```

#### **4. Create Python Requests Scripts**

**File:** `python_scripts/test_users_api.py`
```python
"""
API Testing with Python Requests
Testing JSONPlaceholder API - Free testing API
"""
import requests
import json

class TestUsersAPI:
    BASE_URL = "https://jsonplaceholder.typicode.com"
    
    def test_get_all_users(self):
        """Test GET /users endpoint"""
        response = requests.get(f"{self.BASE_URL}/users")
        
        # Status code validation
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        
        # Response validation
        users = response.json()
        assert isinstance(users, list), "Response should be a list"
        assert len(users) > 0, "Users list should not be empty"
        
        # Data structure validation
        first_user = users[0]
        assert 'id' in first_user
        assert 'name' in first_user
        assert 'email' in first_user
        
        print("✅ GET /users test passed")
        return users
    
    def test_get_specific_user(self):
        """Test GET /users/{id} endpoint"""
        user_id = 1
        response = requests.get(f"{self.BASE_URL}/users/{user_id}")
        
        assert response.status_code == 200
        user_data = response.json()
        
        assert user_data['id'] == user_id
        assert isinstance(user_data['name'], str)
        assert '@' in user_data['email']  # Basic email validation
        
        print(" GET /users/{id} test passed")
        return user_data
    
    def test_create_user(self):
        """Test POST /users endpoint"""
        new_user = {
            "name": "Pinjari Irfan",
            "email": "irfan.mhd.p@gmail.com", 
            "username": "irfan_test"
        }
        
        response = requests.post(f"{self.BASE_URL}/users", json=new_user)
        
        # This demo API returns 201 but doesn't actually create
        assert response.status_code in [200, 201]
        
        response_data = response.json()
        assert 'id' in response_data
        assert response_data['name'] == new_user['name']
        
        print("✅ POST /users test passed")
        return response_data

# Test execution
if __name__ == "__main__":
    api_tester = TestUsersAPI()
    
    print("🚀 Starting API Validation Tests")
    print("=" * 40)
    
    # Run all tests
    api_tester.test_get_all_users()
    api_tester.test_get_specific_user() 
    api_tester.test_create_user()
    
    print("=" * 40)
    print("🎉 All API tests completed successfully!")
```
