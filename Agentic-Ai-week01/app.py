from agents.tool_calling_agent import (
    run_agent
)

if __name__ == "__main__":

    while True:

        query = input(
            "\nAsk Anything: "
        )

        if query.lower() == "exit":

            break

        run_agent(query)