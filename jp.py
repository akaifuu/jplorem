import sys
import random
import pyperclip

# Sample list of Japanese words - expand this list to include 300 words
japanese_words = [
    "時間", "愛", "平和", "光", "影", "雨", "雪", "風", "花", "星",
    "空", "海", "山", "川", "森", "緑", "夢", "希望", "悲しみ", "楽しみ", "ひらがな", "ありがとう", "こんにちは", "アナコンダ", "これ","を", "お願いします", "がんばって", "それ", "あれ", "あり", "へん", "あほ"
    # Add more words here...
]

def generate_sentences(num_sentences):
    sentences = []
    for _ in range(num_sentences):
        length = random.randint(5, 10)  # Adjust for more natural sentence lengths
        sentence = ''.join(random.choices(japanese_words, k=length))
        sentences.append(sentence)
    return ' '.join(sentences)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python generate_japanese_words.py [number]")
        sys.exit(1)
    
    num_sentences = int(sys.argv[1])
    text = generate_sentences(num_sentences)
    print(text)
    pyperclip.copy(text)  # Copy the generated text to the clipboard
