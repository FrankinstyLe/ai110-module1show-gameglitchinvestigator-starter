# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| 79 (secret: 80) | Go higher hint | Hint says go lower | Go Lower |
| 85 (secret: 82) | Go lower hint | Hint says go higher | Go Higher |
| Difficulty level | Easy: range 1 - 20, Normal: range 1 - 50, Hard: range 1 - 100 | Secret number assigned randomly no matter the difficulty | None |
| Starting new game after winning/losing | New game starts, no need to refresh webpage | The announcement stays the same, no new game started | Game over. Start a new game to try again./ You won!...|
| Hit "Enter" to submit | Input taken, shows hints | Input not taken| None | 
| Submit Guess | History records correct attempts | History misrecords 1 attempt | Attempts: 8, History:[0:1, 1:2, 2:3, 3:15, 4:16, 5:15, 6:14] |
| Entering alphabic answer | Only count numeric answers as attempts | Game does not stop and let attempts go to negative and keep recorded in History | Attempts left: -4 |
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
