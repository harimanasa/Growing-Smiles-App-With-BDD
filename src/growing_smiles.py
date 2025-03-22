import json
import random
from datetime import datetime

# ----------------------------
# 🎭 Joke Library
# ----------------------------
jokes = [
    "Why did the teddy bear say no to dessert? Because it was stuffed!",
    "What do you call cheese that isn’t yours? Nacho cheese!",
    "Why don’t skeletons fight each other? They don’t have the guts!",
    "Why was the math book sad? Because it had too many problems.",
    "How do you make a tissue dance? You put a little boogie in it!"
]

# ----------------------------
# 🗂 Mood Journal File
# ----------------------------
MOOD_JOURNAL = "mood_journal.json"

def save_mood_to_journal(mood):
    entry = {
        "mood": mood,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    try:
        with open(MOOD_JOURNAL, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    data.append(entry)

    with open(MOOD_JOURNAL, "w") as file:
        json.dump(data, file, indent=2)

# ----------------------------
# 🤡 Joke Response
# ----------------------------
def tell_joke():
    joke = random.choice(jokes)
    print(f"\n🤡 Here’s something to cheer you up:\n\"{joke}\"")

# ----------------------------
# 🚀 Main App Logic
# ----------------------------
def main():
    print("👋 Hello! Welcome to Manasa's Growing Smiles App!")
    mood = input("💬 How are you feeling today? (e.g., happy, sad, meh): ").strip().lower()

    # Save mood
    save_mood_to_journal(mood)

    # Handle mood
    if mood in ["sad", "meh", "not great", "tired", "okay"]:
        print("💛 I'm here for you. Let's cheer you up!")
        tell_joke()
        response = input("\n😊 Did that make you smile? (yes/no): ").strip().lower()

        if response == "yes":
            print("🎉 Yay! I'm so glad. I'm always here when you need a smile.")
        else:
            print("💌 That’s okay. Want to hear another one or maybe a motivational quote?")
            # This can be expanded with another joke or quote
    elif mood in ["happy", "excited", "great", "awesome"]:
        print("🎈 That’s wonderful! Let’s keep it going!")
    else:
        print("🌈 Thanks for sharing. Every feeling matters.")

    print("\n📒 Your mood has been saved.")
    print("🧡 Come back tomorrow for another check-in!")
    print("Have a joyful day! 🌟")

if __name__ == "__main__":
    main()
