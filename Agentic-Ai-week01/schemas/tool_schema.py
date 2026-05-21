from pydantic import (

    BaseModel,

    Field
)

# ---------- CALCULATOR ----------

class CalculatorInput(BaseModel):

    expression: str = Field(

        description=
        "Mathematical expression to solve"
    )

# ---------- WEATHER ----------

class WeatherInput(BaseModel):

    city: str = Field(

        description=
        "City name for weather lookup"
    )

# ---------- SEARCH ----------

class SearchInput(BaseModel):

    query: str = Field(

        description=
        "Search query for information retrieval"
    )