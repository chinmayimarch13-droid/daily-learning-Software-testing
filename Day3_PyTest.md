# ⚙️ Day 3 - PyTest Practice

## 📌 Objective
To understand the basics of PyTest and how test execution works in automation testing.

---

## ✅ Activities Performed
- Learned basic concepts of PyTest framework
- Understood how test cases are structured and executed
- Practiced writing simple test functions using PyTest

---

## 🧪 Key Concepts Learned
- Test files should start with `test_`
- Test functions should start with `test_`
- Use of `assert` for validation
- Automatic test discovery and execution using PyTest

---

## 💻 Sample Test Code

```python
def test_addition():
    assert 2 + 3 == 5

def test_login():
    username = "admin"
    password = "1234"

    assert username == "admin" and password == "1234"
