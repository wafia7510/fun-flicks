# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.


User Experience Testing:

- Usability Testing:
    - Users interacted with the game through the terminal, and feedback was gathered to ensure the game instructions were clear and easy to follow. No major issues were encountered regarding user input or gameplay flow.
    - **Outcome:** The game is intuitive, with clear instructions for users to input answers correctly.
- Accessibility Testing: The game handles invalid inputs gracefully and provides appropriate error messages. The terminal output was tested for readability, ensuring that users can easily understand and follow the game prompts.

Compatibility Testing:

- Platform Compatibility: Since this is a terminal-based game, testing was conducted on Windows to ensure consistent performance and smooth gameplay.
- Device Compatibility: The game runs effectively on various devices, including laptops and desktops, with no functional issues detected.

Performance Testing:
- Speed Testing: Since the game runs on Heroku, response times for starting new game sessions were tested and confirmed to be quick and responsive.


Regression Testing:

- After each update or bug fix, regression testing was performed to ensure that the core functionalities, such as score calculation, random question generation, and input validation, continued to work without any issues.

Documentation and Logs:

- Logs were maintained for testing procedures, including usability tests and any bugs encountered during development. Fixes were implemented promptly to ensure the game remained functional.



## Code Validation

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory | File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
|  | questions.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/wafia7510/fun-flicks/main/questions.py) | ![screenshot](documentation/question-validator.png) | |
|  | run.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/wafia7510/fun-flicks/main/run.py) | ![screenshot](documentation/main-validator.png) | |

## Browser Compatibility

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Use this space to discuss testing the live/deployed site on various browsers.

Consider testing AT LEAST 3 different browsers, if available on your system.

You DO NOT need to use all of the browsers below, just pick any 3 (minimum).

Recommended browsers to consider:
- [Chrome](https://www.google.com/chrome)
- [Firefox (Developer Edition)](https://www.mozilla.org/firefox/developer)
- [Edge](https://www.microsoft.com/edge)
- [Safari](https://support.apple.com/downloads/safari)
- [Brave](https://brave.com/download)
- [Opera](https://www.opera.com/download)

**IMPORTANT**: You must provide screenshots of the tested browsers, to "prove" that you've actually tested them.

Please note, there are services out there that can test multiple browser compatibilities at the same time.
Some of these are paid services, but some are free.
If you use these, you must provide a link to the source used for attribution, and multiple screenshots of the results.

Sample browser testing documentation:

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Home | About | Contact | etc | Notes |
| --- | --- | --- | --- | --- | --- |
| Chrome | ![screenshot](documentation/browsers/browser-chrome-home.png) | ![screenshot](documentation/browsers/browser-chrome-about.png) | ![screenshot](documentation/browsers/browser-chrome-contact.png) | ![screenshot](documentation/browsers/browser-chrome-etc.png) | Works as expected |
| Firefox | ![screenshot](documentation/browsers/browser-firefox-home.png) | ![screenshot](documentation/browsers/browser-firefox-about.png) | ![screenshot](documentation/browsers/browser-firefox-contact.png) | ![screenshot](documentation/browsers/browser-firefox-etc.png) | Works as expected |
| Edge | ![screenshot](documentation/browsers/browser-edge-home.png) | ![screenshot](documentation/browsers/browser-edge-about.png) | ![screenshot](documentation/browsers/browser-chrome-edge.png) | ![screenshot](documentation/browsers/browser-edge-etc.png) | Works as expected |
| Safari | ![screenshot](documentation/browsers/browser-safari-home.png) | ![screenshot](documentation/browsers/browser-safari-about.png) | ![screenshot](documentation/browsers/browser-safari-contact.png) | ![screenshot](documentation/browsers/browser-safari-etc.png) | Minor CSS differences |
| Brave | ![screenshot](documentation/browsers/browser-brave-home.png) | ![screenshot](documentation/browsers/browser-brave-about.png) | ![screenshot](documentation/browsers/browser-brave-contact.png) | ![screenshot](documentation/browsers/browser-brave-etc.png) | Works as expected |
| Opera | ![screenshot](documentation/browsers/browser-opera-home.png) | ![screenshot](documentation/browsers/browser-opera-about.png) | ![screenshot](documentation/browsers/browser-opera-contact.png) | ![screenshot](documentation/browsers/browser-opera-etc.png) | Minor differences |
| repeat for any other tested browsers | x | x | x | x | x |

## Responsiveness

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

Use this space to discuss testing the live/deployed site on various device sizes.

The minimum requirement is for the following 3 tests:
- Mobile
- Tablet
- Desktop

**IMPORTANT**: You must provide screenshots of the tested responsiveness, to "prove" that you've actually tested them.

Using the "amiresponsive" mockup image (or similar) does not suffice the requirements.
Consider using some of the built-in device sizes in the Developer Tools.

If you have tested the project on your actual mobile phone or tablet, consider also including screenshots of these as well.
It showcases a higher level of manual tests, and can be seen as a positive inclusion!

Sample responsiveness testing documentation:

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

I



## Defensive Programming

In the Fun Flick quiz game, defensive programming techniques were implemented to ensure that the game runs smoothly, securely, and handles invalid inputs effectively.

1. Input Validation:

    - Expected: Users are prompted to enter valid options (A, B, C, or D) for answers. Only these inputs are acceptable.
    - Testing: Tested by entering a mix of valid and invalid inputs (e.g., numbers, special characters, or empty inputs).
    - Result: The game correctly prompts for valid input when invalid options are entered.
    - Fix: Any invalid inputs are handled gracefully, and users are shown an error message to re-enter a valid choice (A, B, C, or D).

2. Handling Edge Cases:

    - Expected: If all questions have been asked, the game should end properly and notify the user.
    - Testing: Repeated the game until all questions were answered.
    - Result: The game ends properly with no crashes and shows the final score.
    - Fix: Ensured that no question is repeated, and when the quiz is over, the game displays the "Game Over" message.

3. Preventing Crashes from Empty or Corrupt Question Data:

    - Expected: If there are no questions in the database (empty list), the game should notify the player and not crash.
    - Testing: Simulated an empty list of questions.
    - Result: The game safely informs the player that no questions are available and exits.
    - Fix: Added a check to handle empty or invalid question data without causing errors.

4. Replay Handling:

    - Expected: Players should be able to restart the game or exit gracefully after completion.
    - Testing: Tested the replay function by choosing both 'Y' and 'N' after game completion.
    - Result: The game restarts or exits properly based on the user's input.
    - Fix: Added input validation for the replay prompt, ensuring only 'Y' or 'N' is accepted.






Defensive programming was manually tested with the below user acceptance testing:

| Page | Expectation | Test | Result | Fix | Screenshot |
| --- | --- | --- | --- | --- | --- |
| Answer Input | | | | | |
| | User should enter A, B, C, or D | Tested with numbers, special characters, letters | Prompts for valid input if invalid characters| Added input validation for user answers | ![screenshot](documentation/features/feature01.png) |
| Game Completion | | | | | |
| | Game should end after all questions are answered | Played until the last question | Displays "Game Over" message, no crashes| Handled edge cases for game completion| ![screenshot](documentation/features/feature03.png) |
| Empty Question Set | | | | | |
| | Game should exit gracefully if no questions exist | Simulated with an empty question list |Shows "No questions available" and exits | Added checks for empty or corrupt question data | ![screenshot](documentation/features/feature05.png) |
| Replay Option | | | | | |
| | User should restart or exit based on input | Chose 'Y' to replay and 'N' to exit |Game restarts or exits based on input | Ensured valid input (Y or N) for replay| ![screenshot](documentation/features/feature07.png) |



## Bugs

1. Issue with Input Validation:

    - Bug: When users entered an invalid input (e.g., numbers or special characters) instead of A, B, C, or D, the game crashed.
    - Solution: Implemented input validation to ensure that only valid options (A, B, C, or D) are accepted. Invalid inputs prompt an error message, and the user is asked to try again.

2. Question Repetition Bug:

    - Bug: During the game, a question was occasionally repeated even though it was supposed to be asked only once.
    - Solution: Fixed by keeping track of already asked questions using a list and ensuring each question is asked only once during the game session.

3. Game Not Ending Properly:

    - Bug: In some cases, the game would not end after all questions were answered, causing it to loop indefinitely.
    - Solution: Corrected the logic to check if all questions had been answered and display the "Game Over" message appropriately.

4. Display Formatting on Different Platforms:

    - The terminal output appeared misaligned on some systems due to differences in screen resolution and terminal window sizes.
    - Solution: Adjusted formatting and used consistent spacing to ensure the game displays correctly across different systems (although primarily tested on Windows).
    
5. No Bugs Identified for Other Platforms:
    - Since testing was only conducted on Windows, no bugs were identified for macOS or Linux systems, though these platforms have not been tested yet.

## Unfixed Bugs
1. Limited Cross-Platform Testing:

    - Bug: The game has only been tested on Windows, and functionality on macOS or Linux is not guaranteed.
    - Reason Unfixed: No access to macOS or Linux machines for comprehensive testing.
    - Workaround: None currently, but the game is expected to work with minor adjustments. Users can report any issues they encounter on non-Windows systems.

2. Game Freezing with Prolonged Idle Time:

    - Bug: If the game is left idle for too long without user input, it occasionally becomes unresponsive.
    - Reason Unfixed: Unable to replicate the issue consistently for debugging.
    Workaround: Users should restart the game if it becomes unresponsive.



🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-START OF NOTES (to be deleted)

If you legitimately cannot find any unfixed bugs or warnings, then use the following sentence:

🛑🛑🛑🛑🛑🛑🛑🛑🛑🛑-END OF NOTES (to be deleted)

> [!NOTE]  
> There are no remaining bugs that I am aware of.