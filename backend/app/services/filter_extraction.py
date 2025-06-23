import re
import os
import json
from openai import OpenAI
from typing import Dict, Optional
from dotenv import load_dotenv

# Load API key from environment variable
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai = OpenAI(api_key=OPENAI_API_KEY)
FILTER_EXTRACTION_MODEL = "gpt-4o"

# --- Configuration Constants ---
GENDER_PATTERNS = {
    "Women": r"(?i)\b(women|woman|ladies|female)\b",
    "Men": r"(?i)\b(men|man|gentlemen|male)\b",
    "Boys": r"(?i)\b(boys|boy)\b",
    "Girls": r"(?i)\b(girls|girl)\b",
    "Unisex": r"(?i)\b(unisex)\b",
}

COLOR_PATTERNS = {
    "Red": r"(?i)\b(red|burgundy|maroon)\b",
    "Blue": r"(?i)\b(blue|navy)\b",
    "Grey": r"(?i)\b(grey|silver|charcoal)\b",
    "Yellow": r"(?i)\b(yellow|gold|mustard|orange|khaki)\b",
    "Pink": r"(?i)\bpink\b",
    "Black": r"(?i)\bblack\b",
    "White": r"(?i)\bwhite\b",
}

PRICE_EXTRACTION_PROMPT = """
  You are an e-commerce assistant. Extract price range from user query.
  Return JSON like: {"min_price": xxx, "max_price": yyy}.
  If only 'under 5000' is mentioned, return {"max_price": 5000}.
  If only 'above 1000' is mentioned, return {"min_price": 1000}.
  If no price is mentioned, return empty JSON.
  """


# --- Main Filter Extraction Function ---
def extract_filters(query_text: str) -> Dict:
    """
    Extract filtering attributes (gender, color_group, price range) from user query.
    """
    filters = {}

    # Rule-based gender extraction
    for gender, pattern in GENDER_PATTERNS.items():
        if re.search(pattern, query_text):
            filters["gender"] = gender
            break

    # Rule-based color extraction
    for color, pattern in COLOR_PATTERNS.items():
        if re.search(pattern, query_text):
            filters["color_group"] = color
            break

    # LLM-based price extraction
    price_filter = _extract_price_with_llm(query_text)
    filters.update(price_filter)

    return filters


# --- LLM helper function ---
def _extract_price_with_llm(query_text: str) -> Dict:
    """
    Use OpenAI LLM to extract price range information from query.
    """
    try:
        response = openai.chat.completions.create(
            model=FILTER_EXTRACTION_MODEL,
            messages=[
                {"role": "system", "content": PRICE_EXTRACTION_PROMPT},
                {"role": "user", "content": f"Query: {query_text}"},
            ],
            temperature=0,
        )

        if not response.choices or not response.choices[0].message.content:
            print("LLM returned empty response.")
            return {}

        # Parse the JSON response from LLM
        content = response.choices[0].message.content
        price_filter = json.loads(content)
        return price_filter
    except Exception as e:
        print(f"LLM price extraction failed: {e}")
        return {}
