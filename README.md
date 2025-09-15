# Password Strength Checker

This Python script assesses the strength of a password based on several criteria and provides feedback on how to improve it. It calculates a score and assigns a strength level (WEAK, MEDIUM, STRONG) to the password.

## Key Features

*   **Score-based assessment:** Assigns a numerical score to the password based on its characteristics.
*   **Strength level:** Categorizes the password into WEAK, MEDIUM, or STRONG levels.
*   **Detailed feedback:** Provides specific suggestions for improving password strength, such as adding uppercase letters, lowercase letters, numbers, or special characters.
*   **Common pattern detection:** Identifies and penalizes passwords containing common patterns like "123456" or "password".
*   **Interactive input:** Uses `getpass` to securely prompt the user for password input without displaying it on the screen.

## Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/versaagonon/check-strength-password-.git
    cd check-strength-password-
    ```

2.  **No external dependencies are required.** The script uses built-in Python modules.

## Usage

1.  **Run the script:**

    ```bash
    python checkstrength.py
    ```

2.  **Enter your password when prompted.** The script will then display the password strength score, level, and any feedback.

    ```
    Input password:
    [+] score strength: 80/100
    [+] Level: STRONG
    [!] Password very strong !
    ```

    Or, if the password is weak:

    ```
    Input password:
    [+] score strength: 10/100
    [+] Level: WEAK
    [!] feedback:
     - Password to short (<8)
     - = add uppercase letter
     - add lowercase letter
     - add number
     - add special character
     - Hindari pola umum seperti 123456
    ```

## Tech Stack and Dependencies

*   **Python 3:** The script is written in Python 3.
*   **`re` module:** Used for regular expression matching to check for character types.
*   **`getpass` module:** Used for secure password input.

## Suggestions for Improvements

1.  **Expand Weak Pattern List:** The current list of weak patterns is limited. Expanding this list with more common passwords, names, and keyboard patterns would improve the accuracy of the strength assessment. Consider loading this list from an external file for easier updates.

2.  **Customizable Scoring:** Allow users to customize the scoring weights for different criteria. This would enable them to tailor the password strength assessment to their specific security requirements.  For example, some users might prioritize length over special characters.

3.  **Implement a Password Complexity Policy:** Add functionality to enforce a password complexity policy. This could include minimum length requirements, mandatory character types, and restrictions on using dictionary words. This would make the script more useful for organizations that need to enforce strong password policies.
