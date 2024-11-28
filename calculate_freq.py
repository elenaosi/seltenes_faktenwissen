import json
import glob
from collections import defaultdict


# DSA-Logik
def find_fact(sentence: str, sub_labels: [str], obj_labels: [str]):
    sub = False
    for i in sub_labels:
        if i.lower() in sentence.lower():
            sub = True
            break  # Subjekt gefunden -> Schleife abbrechen, weiter mit dem Objekt

    if not sub:
        return False  # kein Subjekt gefunden -> Funktion beenden

    obj = False
    for j in obj_labels:
        if j.lower() in sentence.lower():
            obj = True
            break  # Objekt gefunden -> Schleife abbrechen

    return sub and obj


def main():

    fact_data = []
    with open('./datasets/fakt_data_raw/17.jsonl', 'r', encoding='utf-8') as f:
                                    # HINWEIS: Der Name von JSON-Datei soll immer angepasst werden
        for line in f:
            relation = json.loads(line)
            fact_data.append(relation)

    for i in range(1, 23):  # 22 Wikipedia-Teildateien
        wiki_filename = f'./datasets/training_data/kleinere_teile/part_{i}.txt'
        with open(wiki_filename, 'r', encoding='utf-8') as file:
            text_data = file.read()

        sentences = text_data.split('.')  # Sätze enden mit '.'
        output_filename = f'./datasets/fakt_data_freq/P17/17_{i}_freq.jsonl'
                                    # HINWEIS: Der Name von Verzeichnis "P*" und JSON-Datei soll immer angepasst werden
        with open(output_filename, 'w', encoding='utf-8') as output_file:

            for relation in fact_data:
                sub_label = relation["sub_label"]
                obj_label = relation["obj_label"]
                print(f"Verarbeiter Fakt in der Datei {i}: sub_label={sub_label}, obj_label={obj_label}")

                freq = 0
                for sentence in sentences:
                    if find_fact(sentence, [sub_label], obj_label):
                        freq += 1

                result = {
                    "sub_label": sub_label,
                    "obj_label": obj_label,
                    "freq": freq
                }
                output_file.write(json.dumps(result) + "\n")
        print(f"Alle Häufigkeiten für die Fakten in der Datei {i} wurden in {output_filename} gespeichert.")

    print("Alle Wikipepia-Dateien sind bearbeitet.")


    frequency_dict = defaultdict(int)  # leeres Dictionary für die Summierung berechneter Häufigkeiten
    output_path = './datasets/fakt_data_freq/17_merged_freq.jsonl'
                                # HINWEIS: Name von JSON-Datei soll immer angepasst werden

    for filename in glob.glob(
            './datasets/fakt_data_freq/P17/17_*_freq.jsonl'):
                                # HINWEIS: Name der Dateien im Format *_{i}_freq.jsonl soll immen angepasst werden
        with open(filename, 'r') as f:
            for line in f:
                record = json.loads(line)
                fact = (record['sub_label'], tuple(record['obj_label']))
                frequency_dict[fact] += record['freq']

    with open(output_path, 'w') as merged_file:
        for fact, frequency in frequency_dict.items():
            result = {
                'sub_label': fact[0],
                'obj_label': list(fact[1]),
                'freq': frequency
            }
            merged_file.write(json.dumps(result) + '\n')

    print(f"Summierte Häufigkeiten sind in '{output_path}' gespeichert.")


if __name__ == "__main__":
    main()
