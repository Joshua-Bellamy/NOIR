from pydantic import BaseModel, Field


class CalculatorInput(BaseModel):
    """Input schema for the calculator tool."""
    expression: str = Field(description="A math expression to evaluate, e.g. '2 + 2 * 5'")


def calculator(expression: str) -> str:
  """Evaluates a basic math expression safely and returns the result as a string."""
    try:
      allowed_chars = "0123456789+-*/(). "
      if not all(char in allowed_chars for char in expression):
        return "Error: expression contains invalid characters"
      result = eval(expression, {"__builtins__": {}}, {})
      return str(result)
     except Exception as error:
         return f"Error evaluating expression: {error}"


class SearchIput(BaseModel):
    """Input schema for the web search tool."""
    query: str = Field(description="the search query to look up on the web")


def web_search(query: str) -> str)
    """Placeholder for a real web search call. Replace with an actual search API later."""
    return f"Search results for: {query}"


AVA
