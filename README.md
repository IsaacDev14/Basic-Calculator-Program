# Basic Calculator Program

A simple command-line calculator written in Python that performs basic arithmetic operations.

## Features

- **Addition**: Add two numbers
- **Subtraction**: Subtract one number from another
- **Multiplication**: Multiply two numbers
- **Division**: Divide one number by another
- **Interactive Menu**: User-friendly menu system
- **Continuous Operation**: Keep calculating until you choose to exit

## How to Use

1. **Run the Program**
   ```bash
   python calculator.py
   ```

2. **Select an Operation**
   - Choose from the menu options (1-5)
   - Enter the corresponding number for your desired operation

3. **Input Numbers**
   - Enter your first number when prompted
   - Enter your second number when prompted

4. **View Results**
   - The program will display the calculation and result
   - You'll return to the main menu to perform another calculation

5. **Exit**
   - Choose option 5 to exit the program

## Menu Options

```
1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit
```

## Example Usage

```
choose an operation: 

1. add
2. subtract
3. multiply
4. divide
5. Exit

please select an option: 1
please enter the first number: 10
Please Enter the second number: 5
Answer: 10 + 5 = 15
```

## Requirements

- Python 3.x
- No additional libraries required (uses built-in functions only)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/IsaacDev14/Basic-Calculator-Program.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Basic-Calculator-Program
   ```

3. Run the calculator:
   ```bash
   python calculator.py
   ```

## Functions

The program includes four main mathematical functions:

- `add(num1, num2)` - Returns the sum of two numbers
- `substract(num1, num2)` - Returns the difference of two numbers
- `multiplacation(num1, num2)` - Returns the product of two numbers
- `divition(num1, num2)` - Returns the quotient of two numbers

## Error Handling

- Invalid menu selections will prompt you to enter a valid number
- The program will continue running until you choose to exit

## Notes

- Currently accepts integer inputs only
- Division by zero is not handled (will raise a Python error)
- No input validation for non-numeric values

## Future Improvements

Potential enhancements could include:
- Float/decimal number support
- Division by zero error handling
- Input validation for non-numeric entries
- More advanced mathematical operations
- Calculator history feature

## Contributing

Feel free to fork this repository and submit pull requests for any improvements!

## License

This project is open source and available under the [MIT License](LICENSE).
