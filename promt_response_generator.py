import json
import os
import ollama

"""
Promting von LLM-Modelen (Llama 3.1 und Mistral 0.3)
"""

input_dir = './prompts/prompts_for_llama_and_mistral'
output_dir = './prompting_result/mistral_result'   # HINWEIS: Abhängig vom Modell der Name soll angepast werden

input_files = ['P17_prompts.jsonl', 'P19_prompts.jsonl', 'P37_prompts.jsonl', 'P50_prompts.jsonl', 'P84_prompts.jsonl',
            'P127_prompts.jsonl', 'P136_prompts.jsonl', 'P170_prompts.jsonl', 'P176_prompts.jsonl', 'P276_prompts.jsonl',
            'P277_prompts.jsonl', 'P361_prompts.jsonl', 'P463_prompts.jsonl', 'P569_prompts.jsonl', 'P577_prompts.jsonl',
            'P641_prompts.jsonl', 'P915_prompts.jsonl', 'P1113_prompts.jsonl', 'P1376_prompts.jsonl', 'P1427_prompts.jsonl'
]


# Modell-Einstellungen: llama3.1 oder mistral
# HINWEIS: Bei "FROM" soll der Name des Modells entsprechend angepast werden
modelfile='''
FROM mistral                      

SYSTEM "You only like short answers in the form of a string."

'''
ollama.create(model='probe_model', modelfile=modelfile)

def generate_response(prompt):
    response = ollama.generate(model='probe_model', prompt=prompt)
    return response['response'].strip()



def main():

    for input_file in input_files:
        input_path = os.path.join(input_dir, input_file)
        output_file = input_file.replace('_prompts', '_mistral')  # HINWEIS: Abhängig vom Modell der Name soll angepast werden
        output_path = os.path.join(output_dir, output_file)

        count = 0
        with open(output_path, 'w') as output_fp:
            with open(input_path, 'r') as input_fp:
                for line in input_fp:
                    data = json.loads(line)
                    prompt = data['prompt']
                    response_text = generate_response(prompt)
                    result = {
                        "content": response_text
                    }
                    output_fp.write(json.dumps(result) + '\n')
                    count += 1
                    print(f"Datei: {input_file} - Verarbeitete Prompt: {count}")
        print(f"Antworten wurden in {output_path} gespeichert.")

    print("Alle Prompts-Dateien wurden verarbeitet.")


if __name__ == "__main__":
    main()






