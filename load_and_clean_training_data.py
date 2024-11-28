from datasets import load_dataset
import re
import os

"""
Code um Wikipedia-Datensatz (Version 20231101.en https://huggingface.co/datasets/wikimedia/wikipedia) 
herunterzuladen, zu bereinigen und in kleinere Teile zu zerlegen.
Der Datensatz enthält 6 407 814 Artikel. 
"""

dataset = load_dataset("wikimedia/wikipedia", "20231101.en", split='train')
output_file = "./datasets/training_data/wikipedia_dataset.txt"


def clean_data(w_data):
    w_data = w_data.lower()
    w_data = re.sub(r'\be\.g\.\b', ' ', w_data)
    w_data = re.sub(r':', '', w_data)
    w_data = re.sub(r';', '', w_data)
    w_data = re.sub(r'\s+', ' ', w_data).strip()
    w_data = re.sub(r'\(\)', ' ', w_data)
    if not re.search(r'\.\s*$', w_data):
        w_data += '.'
    return w_data


def save_all_in_batches(dataset, batch_size=10000):
    total_articles = len(dataset)
    with open(output_file, 'w', encoding='utf-8') as f:
        for i in range(0, total_articles, batch_size):
            batch = [dataset[j]['text'] for j in range(i, min(i + batch_size, total_articles))]
            for text in batch:
                new_data = clean_data(text)
                f.write(new_data + '\n')
            print(f"Batch {i // batch_size + 1} von {total_articles // batch_size + 1} gespeichert.")



# Zerlegen des Wikipedia-Datensatzes in 22 kleinere Dateien mit jeweils 300.000 Artikeln pro Datei.
def split_articles(file_path, output_dir, articles_per_file):

    os.makedirs(output_dir, exist_ok=True)
    file_count = 1
    articles = []

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            articles.append(line)
            if len(articles) >= articles_per_file:
                output_file = os.path.join(output_dir, f'part_{file_count}.txt')
                with open(output_file, 'w', encoding='utf-8') as output:
                    output.writelines(articles)
                print(f'Erstellt: {output_file}')
                file_count += 1
                articles = []

        # Falls noch Artikel übrig sind
        if articles:
            output_file = os.path.join(output_dir, f'part_{file_count}.txt')
            with open(output_file, 'w', encoding='utf-8') as output:
                output.writelines(articles)
            print(f'Erstellt: {output_file}')


def main():
    print(f"Der Datensatz enthält {len(dataset)} Artikel.")
    save_all_in_batches(dataset, batch_size=10000)
    print(f"Gesanter Wikipedia-Datensatz wurde in '{output_file}' gespeichert.")


    input_file_path = "./datasets/training_data/wikipedia_dataset.txt"
    output_directory = './datasets/training_data'
    articles_per_file = 300000
    split_articles(input_file_path, output_directory, articles_per_file)
    print(f"Zerlegter Datensatz wurden in '{output_directory}' gespeichert.")


if __name__ == "__main__":
    main()

