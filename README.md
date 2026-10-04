# PayUp

PayUp is a simple Python command-line program that calculates how much each person in a group should pay after splitting the total cost of an event or shared expense.

The project was created as part of my Python learning process to practice user input, arithmetic operations, variables, functions, and formatted output.

## Features

- Accepts the total cost of an event or shared expense
- Accepts the number of people splitting the cost
- Calculates the amount each person should pay
- Displays monetary values to two decimal places
- Provides a simple command-line interaction

## Example

```text
Enter the total cost: 120
Enter the number of people: 4

Each person must PayUp: $30.00
```

## Technologies

- Python

## Concepts Practiced

- Variables
- User input
- Type conversion
- Arithmetic operations
- Functions
- Floating-point numbers
- F-string formatting

For example:

```python
print(f"Each person must PayUp: ${total_per_person:.2f}")
```

The `.2f` formatting ensures that monetary values are displayed with two decimal places.

## Project Structure

```text
payup/
├── payup.py
└── README.md
```

## Running the Project

### 1. Clone the repository

```bash
git clone <your-repository-url>
```

### 2. Move into the project folder

```bash
cd payup
```

### 3. Run the program

```bash
python payup.py
```

## Future Improvements

Some features I may add as I continue developing the project include:

- Tip calculations
- Tax calculations
- Unequal expense splitting
- Input validation and error handling
- Multiple expenses within the same event
- Participant names
- Saving previous calculations
- A graphical or web-based interface

## Purpose

PayUp was created as a small practical project while strengthening my Python fundamentals.

Rather than focusing only on isolated syntax exercises, the goal was to apply those concepts to a simple real-world problem: splitting a shared expense among a group of people.

## Author

**Supreme Emhenya**

- GitHub: [Emya101](https://github.com/Emya101)
- LinkedIn: [Supreme Emhenya](https://www.linkedin.com/in/supreme-emhenya)
