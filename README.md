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

- [x] The game generates a secrect number and gives player a number of attempt and a range to guess within.
- [x] Overal game logic (hints, scoring, attempts count/mismatch). Some UI functionalities (delay on real-time updates, inputs take-in, incorrect information showing from player's POV)
- [x] Code refactoring, AI edits, Game logic rewiring.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. When first launch the game, select difficulty level from drop-down menu on you left. Make sure "Show hint" box is ticked.
2. Enter a guess as instructed. Adjust your next guesses based on hint.
3. If hint says "Go Lower", enter a lower value than previous guess. Do otherwise if hint says "Go Higher"
4. Score updates correctly after each guess, it goes down after each wrong guess. Max score depends on difficulties and number of attempts used. New game/difficulty resets the score.
5. Game ends after the correct guess or no more attempts left. 

**Screenshot** *(optional)*: ![alt text](<Winning screenshot.png>)

## 🧪 Test Results

```
======================================== test session starts =========================================
platform win32 -- Python 3.13.1, pytest-8.4.1, pluggy-1.6.0
rootdir: C:\Users\Frankinstyle\CodePath\AI110\Project 1\ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.9.0, asyncio-1.1.0, cov-6.2.1
asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=None, asyncio_default_test_loop_scope=function
collected 13 items                                                                                    

tests\test_game_logic.py .............                                                          [100%]

========================================= 13 passed in 0.03s =========================================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
