from logic_utils import check_guess, update_score, parse_guess, get_range_for_difficulty

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Scoring bug regression tests -------------------------------------------
# These target the scoring bug we fixed in update_score:
#   1. A first-try win used to award 100 - 10*(attempt+1) = 80; it should be 90.
#   2. A "Too High" guess on an even attempt used to ADD 5 (rewarding a wrong
#      guess); every wrong guess should consistently subtract 5.

def test_first_try_win_awards_90():
    # Winning on the first attempt should give the max 90 points.
    # The buggy version awarded only 80.
    assert update_score(0, "Win", 1) == 90


def test_too_high_always_subtracts_5_even_attempt():
    # A wrong "Too High" guess on an even attempt must cost 5 points.
    # The buggy version added 5 on even attempts.
    assert update_score(100, "Too High", 2) == 95


def test_wrong_guess_penalty_is_consistent():
    # "Too High" and "Too Low" should both subtract 5 regardless of attempt.
    assert update_score(100, "Too High", 1) == 95
    assert update_score(100, "Too High", 4) == 95
    assert update_score(100, "Too Low", 2) == 95


def test_win_on_last_easy_attempt():
    # Easy allows 8 attempts (the largest cap). Winning on the final allowed
    # attempt is the lowest win score reachable in real play: 100 - 10*8 = 20.
    assert update_score(0, "Win", 8) == 20


def test_unknown_outcome_leaves_score_unchanged():
    # Any outcome that isn't Win/Too High/Too Low must not mutate the score.
    assert update_score(50, "Invalid", 1) == 50


# --- parse_guess edge cases -------------------------------------------------
# parse_guess returns (ok, guess_int, error_message). It owns two bugs from the
# reflection log: alphabetic input letting attempts go negative, and empty input.

def test_parse_guess_rejects_alphabetic():
    # Non-numeric text should be rejected, not counted as an attempt.
    ok, value, err = parse_guess("abc")
    assert ok is False
    assert value is None
    assert err == "That is not a number."


def test_parse_guess_rejects_empty_and_none():
    assert parse_guess("") == (False, None, "Enter a guess.")
    assert parse_guess(None) == (False, None, "Enter a guess.")  # type: ignore[arg-type]


def test_parse_guess_truncates_float_string():
    # "3.7" goes through the int(float(raw)) path and truncates toward zero.
    ok, value, err = parse_guess("3.7")
    assert ok is True
    assert value == 3
    assert err is None


# --- get_range_for_difficulty ------------------------------------------------

def test_range_for_each_difficulty():
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 50)
    assert get_range_for_difficulty("Hard") == (1, 100)


def test_range_unknown_difficulty_falls_back():
    # Anything unrecognized defaults to the full 1-100 range.
    assert get_range_for_difficulty("???") == (1, 100)
