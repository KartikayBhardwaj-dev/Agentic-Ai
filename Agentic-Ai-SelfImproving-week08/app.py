# -------IMPORTS-----------
from dotenv import load_dotenv
from generator import generate_answer
from critic import critic_answer
from retry import improve_answer, extract_score

# ----------TAKING QUESTION FROM USER AND GENERATING FIRST ANSWER---------
question = input("Ask Question: ")
print("\nGENERATING ANSWER...\n")

answer = generate_answer(question)
print("INITIAL ANSWER:\n")
print(answer)

# ----------CRITICING THE ANSWER--------
print("\nCRITICING THE ANSWER...\n")
critic = critic_answer(question, answer)
print("CRITIC\n")
print(critic)

# ---------EXTRACTING THE SCORE--------
score = extract_score(critic)
print(f"\nSCORE: {score}/10")

if score < 7:
    print("\nIMPROVING ANSWER\n")
    improved = improve_answer(
        question,
        answer,
        critic
    )

    print("IMPROVED ANSWER:\n")
    print(improved)
else:
    print("\nFINAL ANSWER ACCEPTED")


