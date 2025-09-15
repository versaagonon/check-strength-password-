```markdown
# Password Strength Checker

This Python script assesses the strength of a password based on several criteria, providing a score, a strength level (Weak, Medium, Strong), and feedback on how to improve it.

## Key Features

*   **Score-based assessment:** Assigns a numerical score to the password based on its characteristics.
*   **Strength level:** Categorizes the password into Weak, Medium, or Strong levels.
*   **Feedback mechanism:** Provides specific suggestions for improving password strength (e.g., adding uppercase letters, special characters).
*   **Common pattern detection:** Checks for and penalizes the use of common and easily guessable patterns.
*   **Interactive input:** Uses `getpass` to securely prompt the user for password input without displaying it on the screen.

## Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/versaagonon/check-strength-password-.git
    cd check-strength-password-
    ```

2.  **No external dependencies are required.** The script uses only built-in Python modules.

## Usage

1.  **Run the script:**

    ```bash
    python checkstrength.py
    ```

2.  **Enter your password when prompted.** The password will not be displayed on the screen.

3.  **View the results.** The script will output the password strength score, level, and any feedback for improvement.

    ```
    Input password:
    [+] score strength: 80/100
    [+] Level: STRONG
    [!] Password very strong !
    ```

    Or, if the password is weak:

    ```
    Input password:
    [+] score strength: 20/100
    [+] Level: WEAK
    [!] feedback:
     - Password to short (<8)
     - add uppercase letter
     - add number
     - add special character
    ```

## Tech Stack and Dependencies

*   **Python:** The script is written in Python 3.
*   **`re` module:** Used for regular expression matching to check for character types.
*   **`getpass` module:** Used for secure password input.

## Suggestions for Improvements

1.  **Customizable Strength Criteria:** Allow users to configure the scoring system and feedback messages through a configuration file or command-line arguments. This would enable tailoring the script to specific security requirements. For example, an organization might require a minimum score of 80 for a password to be considered strong.

2.  **Enhanced Pattern Detection:** Expand the list of weak patterns to include more common words, names, and keyboard sequences. Consider using a more sophisticated algorithm, such as a Markov model, to identify predictable password patterns.

3.  **Integration with Password Managers:** Explore the possibility of integrating the script with popular password managers to provide real-time feedback on password strength during password generation or modification. This could be achieved through a plugin or API.
