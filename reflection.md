# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

1. The enter button wasn't working when I first guessed. I had to press "submit". 
2. The higher and lower hint are not correct since the correct number was 33 and I typed 40 and it says "go Higher". Probably flipped logic?
3. when I click "New Game", it says "You already won. Start a new game to play again". I have to restart the app from terminal as the New Game function not working properly
  

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|a guess of 12 | a hint of go HIGHER | a hint of go LOWER | "go LOWER"|
|-1000 | throw an error becaus i entered a number < 0| guess counted towards my trials/attempts| Go lower/proceeded even though input was out of bounds |
| press "New Game" | restart game | not accepting new guesses| "Game over. Start a new game to try again". |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used ClaudeCode, Sonnet model. I asked it to explain the logic behind why a newgame wouldn't start when I press "New Game", selecting relevant lines in the app.py.

It pointed out the glitch in how status is never reset to "playing" because the handler sets attempts = 0, and picks a new secret, then calls st.rerun(). But after the rerun, the st.stop block runs and the game is frozen. 

It spotted that attempts should be re-initialized as 0 "minor bug"but then mentioned after another prompt that this is not a bug and the game would run normally. However, if we fixed the st.session_state, re-run the new game, the attempts would stay at the last stored attempt "8" so when we submit a new guess, attempt would be incremented by 1 and the game would say "out of attempts" although it's the first guess

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
