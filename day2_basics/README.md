# Day 2 – Python Basics (Applied Learning)

## What I Learned
On Day 2, I focused on understanding how core Python concepts work together in a single program instead of learning them in isolation. I learned how to control program flow, make decisions based on conditions, and process data using appropriate data structures.

The key concepts I learned include:
- Conditional statements (`if`, `else`)
- Logical operators (`and`, `or`, `in`)
- Looping constructs (`for`, `while`)
- Loop control statements (`break`, `continue`)
- Python data structures:
  - Lists for sequential data
  - Tuples for constant values
  - Dictionaries for structured data
- Formatted output using f-strings

---

## How I Implemented It
To apply these concepts, I built a **security log analyzer** using Python.  
The goal was to simulate how a system analyzes login attempts and blocks a user after repeated failures.

### Implementation Approach
- I stored constant security rules (allowed roles and block threshold) using tuples and variables.
- I represented user information using a dictionary to simulate real user records.
- I stored login attempt status codes in a list to preserve the order of events.
- I used conditional statements to validate user access before processing logs.
- I used a `for` loop to iterate through login attempts and count failed logins.
- I used `continue` to skip further checks for successful logins.
- I used `break` to immediately stop processing once the block threshold was reached.
- I used a `while` loop to simulate a cooldown period after the user was blocked.
- Finally, I printed a summary report based on the system state.

---

## File
