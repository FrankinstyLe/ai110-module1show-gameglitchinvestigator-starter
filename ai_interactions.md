# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

Verify, improve and generate test cases.

**What did the agent do?**

Edited the pre-existing test cases to suit with the new codebase, and generated more useful test cases.

**What did you have to verify or fix manually?**

Identifying user experience problems

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| First-try win score | "Generate a pytest case that targets the bug we have fixed so far" | `test_first_try_win_awards_90` — `update_score(0, "Win", 1) == 90` | Yes | Pins the scoring fix; the buggy `100 - 10*(attempt+1)` gave only 80. |
| Wrong guess on even attempt | (same) | `test_too_high_always_subtracts_5_even_attempt` — `update_score(100, "Too High", 2) == 95` | Yes | Old code added +5 on even attempts, rewarding wrong guesses; now a consistent -5. |
| Lowest reachable win | "Any edge case missed, given max 8 attempts?" | `test_win_on_last_easy_attempt` — `update_score(0, "Win", 8) == 20` | Yes | Attempt 8 is the largest cap (Easy); confirms wins stay positive without the removed floor. |
| Non-numeric input | (same) | `test_parse_guess_rejects_alphabetic` — `parse_guess("abc")` → `(False, None, "That is not a number.")` | Yes | Matches reflection bug where letters let attempts go negative. |
| Float-string input | (same) | `test_parse_guess_truncates_float_string` — `parse_guess("3.7")` → `(True, 3, None)` | Yes | Verifies the `int(float(raw))` truncation path. |
| Difficulty ranges | (same) | `test_range_for_each_difficulty` / `..._unknown_difficulty_falls_back` — Easy (1,20), Normal (1,50), Hard (1,100), unknown → (1,100) | Yes | Covers reflection bug where range ignored difficulty; locks the fallback. |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
<!-- Paste the prompt you gave the AI -->
```

**Linting output before:**

```
<!-- Paste relevant linter warnings/errors -->
```

**Changes applied:**

<!-- Describe what you changed based on the AI's suggestions -->

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

| | Model A | Model B |
|-|---------|---------|
| **Model name** | | |
| **Response summary** | | |
| **More Pythonic?** | | |
| **Clearer explanation?** | | |

**Which did you prefer and why?**

<!-- Your conclusion -->
