from logic_utils import check_guess, parse_guess, get_range_for_difficulty, update_score

# --- check_guess ---

def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

def test_guess_out_of_range_above():
    outcome, _ = check_guess(101, 50, low=1, high=100)
    assert outcome == "Out of Range"

def test_guess_out_of_range_below():
    outcome, _ = check_guess(0, 50, low=1, high=100)
    assert outcome == "Out of Range"

def test_guess_at_lower_boundary():
    outcome, _ = check_guess(1, 50, low=1, high=100)
    assert outcome == "Too Low"

def test_guess_at_upper_boundary():
    outcome, _ = check_guess(100, 50, low=1, high=100)
    assert outcome == "Too High"

def test_check_guess_returns_message_string():
    _, message = check_guess(50, 50)
    assert isinstance(message, str) and len(message) > 0

# --- parse_guess ---

def test_parse_valid_integer():
    ok, value, err = parse_guess("42")
    assert ok is True and value == 42 and err is None

def test_parse_float_truncates_to_int():
    ok, value, _ = parse_guess("7.9")
    assert ok is True and value == 7

def test_parse_empty_string():
    ok, value, _ = parse_guess("")
    assert ok is False and value is None

def test_parse_none():
    ok, value, _ = parse_guess(None)
    assert ok is False and value is None

def test_parse_non_numeric():
    ok, _, err = parse_guess("abc")
    assert ok is False and err is not None

# --- get_range_for_difficulty ---

def test_range_easy():
    assert get_range_for_difficulty("Easy") == (1, 20)

def test_range_normal():
    assert get_range_for_difficulty("Normal") == (1, 50)

def test_range_hard():
    assert get_range_for_difficulty("Hard") == (1, 1000)

def test_range_unknown_falls_back_to_default():
    low, high = get_range_for_difficulty("Unknown")
    assert low == 1 and high == 100

# --- update_score ---

def test_score_increases_on_win():
    assert update_score(0, "Win", attempt_number=2) > 0

def test_score_decreases_on_too_high():
    assert update_score(50, "Too High", attempt_number=3) == 45

def test_score_decreases_on_too_low():
    assert update_score(50, "Too Low", attempt_number=3) == 45

def test_score_unchanged_on_out_of_range():
    assert update_score(50, "Out of Range", attempt_number=3) == 50

def test_score_win_never_goes_below_minimum():
    # Very late win should still award at least 10 points
    assert update_score(0, "Win", attempt_number=100) == 10
