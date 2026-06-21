#FIX: Refactored logic into logic_utils.py using agent mode

def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    elif difficulty == "Normal":
        return 1, 50
    elif difficulty == "Hard":
        return 1, 1000
    else:
        return 1, 100

#FIX: Refactored logic into logic_utils.py using agent mode
def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None or raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None

#FIX: Refactored logic into logic_utils.py using agent mode
def check_guess(guess, secret, low=None, high=None):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low", "Out of Range"
    """
    if low is not None and high is not None:
        if guess < low or guess > high:
            return "Out of Range", f"⚠️ {guess} is out of range! Please enter a number between {low} and {high}."

    if guess == secret:
        return "Win", "🎉 Correct!"

    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    return "Too Low", "📈 Go HIGHER!"


#FIX: Refactored logic into logic_utils.py using agent mode
def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome in ("Too High", "Too Low"):
        return current_score - 5

    return current_score
