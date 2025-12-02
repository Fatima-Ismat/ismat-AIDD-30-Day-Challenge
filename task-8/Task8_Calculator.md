# Task 8: Simple Calculator using SPECKitPlus

## 1️⃣ Constitution
**Project Scope:**  
Build a simple calculator using SPECKitPlus that can perform basic arithmetic operations: addition, subtraction, multiplication, and division.  

**Features:**  
- Addition (+)  
- Subtraction (-)  
- Multiplication (*)  
- Division (/)  
- Handle division by zero  
- User-friendly input/output  

---

## 2️⃣ Specify
**Inputs:**  
- num1: First number  
- num2: Second number  
- operator: Arithmetic operator (+, -, *, /)  

**Outputs:**  
- Result of the operation  

**Constraints:**  
- Only numerical inputs allowed  
- Only specified operators allowed  

---

## 3️⃣ Plan
**Workflow:**  
1. Take two numbers from user  
2. Take operator (+, -, *, /)  
3. Compute result based on operator  
4. Handle invalid inputs / division by zero  
5. Display result  

---

## 4️⃣ Tasks
| Task No | Description |
|---------|-------------|
| 1       | Create input function for numbers and operator |
| 2       | Implement addition operation |
| 3       | Implement subtraction operation |
| 4       | Implement multiplication operation |
| 5       | Implement division operation |
| 6       | Handle invalid input (non-numeric) |
| 7       | Handle invalid operator |
| 8       | Handle division by zero |
| 9       | Display result |

---

## 5️⃣ Implement
**Python Code:**

```python
def calculator():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        op = input("Enter operator (+, -, *, /): ")

        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 == 0:
                print("Error: Division by zero")
                return
            result = num1 / num2
        else:
            print("Invalid operator")
            return

        print("Result:", result)
    except ValueError:
        print("Invalid input. Enter numbers only.")

calculator()

6️⃣ Test Screenshots

Screenshot 1: Addition Result

Screenshot 2: Multiplication Result


Screenshot 3: Error Handling (e.g., division by zero)
