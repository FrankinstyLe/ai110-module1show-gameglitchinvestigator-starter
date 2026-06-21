# FIX: Refactored these helpers out of app.py into logic_utils.py using agent mode (Claude) so the game logic is testable and isolated from the Streamlit UI.
def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 50
    if difficulty == "Hard":
        return 1, 100
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    # FIX: Hints were reversed (guess too high told you to go HIGHER). I spotted it from the bug repro log and had agent mode flip the messages so "too high" -> go LOWER and "too low" -> go HIGHER.
    if guess > secret:
        return "Too High", "📈 Go LOWER!"
    else:
        return "Too Low", "📉 Go HIGHER!"

# FIX: Scoring was off — a first-try win only gave 80 (it used attempt_number + 1) and "Too High" on even attempts handed out +5 instead of a penalty. Working with agent mode I traced it to the bug repro log, then dropped the +1 offset and made every wrong guess a consistent -5.
#FIX: Remove unreachable floor because points will never go below 10 with highest attempt never passes 9 accorss all difficulties.
def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * attempt_number
        return current_score + points

    if outcome == "Too High":
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
