from agents.supervisor import supervisor

if __name__ == "__main__":
    task = input("Enter your research topic: ")
    result = supervisor(task)

    print("\n\n========RESEARCH REPORT======\n")
    print(result["research"])
