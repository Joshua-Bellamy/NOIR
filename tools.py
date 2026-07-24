from pydantic import BaseModel, Field


class CalculatorInput(BaseModel):
    """Input schema for the calculator tool."""
    expression: str = Field(description="A math expression to evaluate, e.g. '2 + 2 * 5'")


def calculator(expression: str) -> str:
  """Evaluates a basic math expression safely and returns the result as a string."""
    try:
      allowed_chars = "0123456789+-*/(). "
      if not all(char in allowed_chars for char in expressions):
