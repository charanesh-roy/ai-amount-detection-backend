from typing import List, Tuple


def normalize_tokens(tokens: List[str]) -> Tuple[List[int], float]:
    """
    Convert string tokens to integers and remove noise
    """
    normalized = []

    for token in tokens:
        try:
            value = int(token)
            if value > 0:
                normalized.append(value)
        except ValueError:
            continue

    confidence = 0.82 if normalized else 0.0
    return normalized, confidence


def classify_amounts(text: str, amounts: List[int]):
    """
    Improved classification logic:
    - Ignore small numbers
    - Ignore years (1900–2100)
    - Pick the largest remaining value
    """

    if not amounts:
        return [], 0.0

    meaningful = []

    for a in amounts:
        if a < 50:
            continue
        if 1900 <= a <= 2100:
            continue
        meaningful.append(a)

    if not meaningful:
        meaningful = amounts

    total = max(meaningful)

    return [
        {
            "type": "total_amount",
            "value": total
        }
    ], 0.9
