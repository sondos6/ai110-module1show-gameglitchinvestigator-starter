# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- Purpose: Ask the user to guess a number between 1-100
- The initial bugs included backward logic in hints (go higher/lower), frozen game when pressing new game button, easy, normal, hard logic does not apply to the range prompted to user as it is always saying enter a number between 1-100

Applied fixes:
1. Re-initialize the game properly via asking the AI agent to fix the st.session_state.status and clear the attempts history so that it is re-initalized at 1.
2. Fixed the high/low error
3. Fixed the difficulty range input prompts where users are asked to input numbers according to diffculty level.
4. Fixed the update score logic as it added 5 points on even attempts, rewarding a wrong guess. Both wrong outcomes should consistently subtract points.
5. Throw a message if the user entered an out-of-range number 

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. 
2. <!-- Describe this step -->
3. <!-- Describe this step -->
4. <!-- Describe this step -->
5. <!-- Add more steps as needed -->

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
=================================================================== test session starts ===================================================================
platform darwin -- Python 3.13.9, pytest-8.4.2, pluggy-1.5.0
rootdir: /Users/sondos/Documents/GitHub/ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.10.0
collected 22 items                                                                                                                                        

tests/test_game_logic.py ......................                                                                                                     [100%]

=================================================================== 22 passed in 0.02s ====================================================================
```

