import json
import os
from scipy.stats import pearsonr
from scipy.stats import spearmanr
import numpy as np
import argparse


# LLM-Dateien Paare nach LLM-Typ bilden (GPT/Llama/Mistral oder all_gpt/all_llama/all_mistral)
def get_file_paths(llm_type):

    if llm_type == "gpt":

        # Faktendatensätze mit Frequenzen
        fact_dir = "./datasets/fakt_data_freq"
        fact_files = [
            "P17_merged_freq.jsonl", "P19_merged_freq.jsonl", "P37_merged_freq.jsonl",
            "P50_merged_freq.jsonl", "P84_merged_freq.jsonl", "P127_merged_freq.jsonl",
            "P136_merged_freq.jsonl", "P170_merged_freq.jsonl", "P176_merged_freq.jsonl",
            "P276_merged_freq.jsonl", "P277_merged_freq.jsonl", "P361_merged_freq.jsonl",
            "P463_merged_freq.jsonl", "P569_merged_freq.jsonl", "P577_merged_freq.jsonl",
            "P641_merged_freq.jsonl", "P915_merged_freq.jsonl", "P1113_merged_freq.jsonl",
            "P1376_merged_freq.jsonl", "P1427_merged_freq.jsonl"
        ]

        # Dateien mit den Ausgaben des Modells
        llm_dir = "./prompting_result/gpt_result"
        llm_files = [
            "P17_gpt_extracted.jsonl", "P19_gpt_extracted.jsonl", "P37_gpt_extracted.jsonl",
            "P50_gpt_extracted.jsonl", "P84_gpt_extracted.jsonl", "P127_gpt_extracted.jsonl",
            "P136_gpt_extracted.jsonl", "P170_gpt_extracted.jsonl", "P176_gpt_extracted.jsonl",
            "P276_gpt_extracted.jsonl", "P277_gpt_extracted.jsonl", "P361_gpt_extracted.jsonl",
            "P463_gpt_extracted.jsonl", "P569_gpt_extracted.jsonl", "P577_gpt_extracted.jsonl",
            "P641_gpt_extracted.jsonl", "P915_gpt_extracted.jsonl", "P1113_gpt_extracted.jsonl",
            "P1376_gpt_extracted.jsonl", "P1427_gpt_extracted.jsonl"
        ]


    elif llm_type == "llama":

        # Faktendatensätze mit Frequenzen
        fact_dir = "./datasets/fakt_data_freq"
        fact_files = [
            "P17_merged_freq.jsonl", "P19_merged_freq.jsonl", "P37_merged_freq.jsonl",
            "P50_merged_freq.jsonl", "P84_merged_freq.jsonl", "P127_merged_freq.jsonl",
            "P136_merged_freq.jsonl", "P170_merged_freq.jsonl", "P176_merged_freq.jsonl",
            "P276_merged_freq.jsonl", "P277_merged_freq.jsonl", "P361_merged_freq.jsonl",
            "P463_merged_freq.jsonl", "P569_merged_freq.jsonl", "P577_merged_freq.jsonl",
            "P641_merged_freq.jsonl", "P915_merged_freq.jsonl", "P1113_merged_freq.jsonl",
            "P1376_merged_freq.jsonl", "P1427_merged_freq.jsonl"
        ]

        # Dateien mit den Ausgaben des Modells
        llm_dir = "./prompting_result/llama_result"
        llm_files = [
            "P17_llama_extracted.jsonl", "P19_llama_extracted.jsonl", "P37_llama_extracted.jsonl",
            "P50_llama_extracted.jsonl", "P84_llama_extracted.jsonl", "P127_llama_extracted.jsonl",
            "P136_llama_extracted.jsonl", "P170_llama_extracted.jsonl", "P176_llama_extracted.jsonl",
            "P276_llama_extracted.jsonl", "P277_llama_extracted.jsonl", "P361_llama_extracted.jsonl",
            "P463_llama_extracted.jsonl", "P569_llama_extracted.jsonl", "P577_llama_extracted.jsonl",
            "P641_llama_extracted.jsonl", "P915_llama_extracted.jsonl", "P1113_llama_extracted.jsonl",
            "P1376_llama_extracted.jsonl", "P1427_llama_extracted.jsonl"
     ]


    elif llm_type == "mistral":

        # Faktendatensätze mit Frequenzen
        fact_dir = "./datasets/fakt_data_freq"
        fact_files = [
            "P17_merged_freq.jsonl", "P19_merged_freq.jsonl", "P37_merged_freq.jsonl",
            "P50_merged_freq.jsonl", "P84_merged_freq.jsonl", "P127_merged_freq.jsonl",
            "P136_merged_freq.jsonl", "P170_merged_freq.jsonl", "P176_merged_freq.jsonl",
            "P276_merged_freq.jsonl", "P277_merged_freq.jsonl", "P361_merged_freq.jsonl",
            "P463_merged_freq.jsonl", "P569_merged_freq.jsonl", "P577_merged_freq.jsonl",
            "P641_merged_freq.jsonl", "P915_merged_freq.jsonl", "P1113_merged_freq.jsonl",
            "P1376_merged_freq.jsonl", "P1427_merged_freq.jsonl"
        ]

        # Dateien mit den Ausgaben des Modells
        llm_dir = "./prompting_result/mistral_result"
        llm_files = [
            "P17_mistral_extracted.jsonl", "P19_mistral_extracted.jsonl", "P37_mistral_extracted.jsonl",
            "P50_mistral_extracted.jsonl", "P84_mistral_extracted.jsonl", "P127_mistral_extracted.jsonl",
            "P136_mistral_extracted.jsonl", "P170_mistral_extracted.jsonl", "P176_mistral_extracted.jsonl",
            "P276_mistral_extracted.jsonl", "P277_mistral_extracted.jsonl", "P361_mistral_extracted.jsonl",
            "P463_mistral_extracted.jsonl", "P569_mistral_extracted.jsonl", "P577_mistral_extracted.jsonl",
            "P641_mistral_extracted.jsonl", "P915_mistral_extracted.jsonl", "P1113_mistral_extracted.jsonl",
            "P1376_mistral_extracted.jsonl", "P1427_mistral_extracted.jsonl"
        ]


    elif llm_type == "all_gpt":

        fact_dir = "./datasets/fakt_data_freq"
        fact_files = ["freq_merged.jsonl"]

        llm_dir = "./prompting_result/gpt_result"
        llm_files = ["gpt_merged.jsonl"]    # Alle Ausgaben von GPT in einer Datei



    elif llm_type == "all_llama":

        fact_dir = "./datasets/fakt_data_freq"
        fact_files = ["freq_merged.jsonl"]

        llm_dir = "./prompting_result/llama_result"
        llm_files = ["llama_merged.jsonl"]     # Alle Ausgaben von Llama in einer Datei



    elif llm_type == "all_mistral":

        fact_dir = "./datasets/fakt_data_freq"
        fact_files = ["freq_merged.jsonl"]

        llm_dir = "./prompting_result/mistral_result"
        llm_files = ["mistral_merged.jsonl"]    # Alle Ausgaben von Mistral in einer Datei


    else:
        raise ValueError(f"Unbekannter LLM-Typ: {llm_type}")


    file_pairs = []
    for fact_file, llm_file in zip(fact_files, llm_files):
        fact_file_path = os.path.join(fact_dir, fact_file)
        llm_file_path = os.path.join(llm_dir, llm_file)
        file_pairs.append((fact_file_path, llm_file_path))

    return file_pairs



def load_jsonl(file_path):
    with open(file_path, 'r') as file:
        return [json.loads(line) for line in file]



def calculate_rank(fact, llm):

    rank_list = []

    for item in fact:
        obj_label = item['obj_label'][0].strip().lower()      # da wir immer nur einen obj_label haben
        item_id = item['id']

        llm_item = None
        for temp in llm:
            if temp['id'] == item_id:
                llm_item = temp
                break
        if llm_item is None:
            continue

        response_list = [resp.strip().lower() for resp in llm_item['content'].split('$')]

        rank = 0
        for i, response in enumerate(response_list):
            if obj_label in response:
                rank = i + 1  # Rang ist 1-basiert, daher +1
                break
        rank_list.append(rank)

        #print(f"ID: {item_id}")
        #print(f"Richtige Antwort (obj_label): {obj_label}")
        #print(f"Ausgabe des Modells: {response_list}")
        #print(f"Rang der richtigen Antwort: {rank}\n")

    return rank_list



def create_list_of_freq(fact):

    frequencies = [item['freq'] for item in fact]
    return frequencies



def calculate_p_at_k(fact, llm, k_values):

    results = {}
    total_instances = len(fact)

    for k in k_values:
        total_relevant = 0
        for item in fact:
            obj_label = item['obj_label'][0].strip().lower()
            item_id = item['id']

            llm_item = None
            for temp in llm:
                if temp['id'] == item_id:
                    llm_item = temp
                    break
            if llm_item is None:
                continue

            response_list = [resp.strip().lower() for resp in llm_item['content'].split('$')]

            relevant_count = 0
            for resp in response_list[:k]:
                if obj_label == resp:
                    relevant_count += 1
            total_relevant += relevant_count

        p_at_k = total_relevant / total_instances
        results[k] = p_at_k

    return results



def calculate_hit_rate(fact, llm):

    rank_list = calculate_rank(fact, llm)

    relevant_item = 0
    for item in rank_list:
        if item > 0:
            relevant_item += 1
    print(f"Anzahl relevanter Treffer: {relevant_item}")

    hit_rate = relevant_item / len(rank_list)

    return hit_rate




def calculate_mrr(rank_list):

    reciprocal_ranks = []
    #print(f"Ursprüngliche Rangliste: {rank_list}")

    for rank in rank_list:
        if rank > 0:
            reciprocal_rank = 1 / rank
            reciprocal_ranks.append(reciprocal_rank)
            #print(f"Rank: {rank}, Reziproker Rang: {reciprocal_rank:.4f}")

    if reciprocal_ranks:
        mrr = sum(reciprocal_ranks) / len(reciprocal_ranks)
        #print(f"Summe der reziproken Ränge: {sum(reciprocal_ranks):.4f}, Anzahl der gültigen Ränge: {len(reciprocal_ranks)}")
        #print(f"MRR: {mrr:.4f}")
    else:
        mrr = 0

    return mrr



def calculate_pearson(ranks, frequencies):

    correlation, p_value = pearsonr(ranks, frequencies)
    return correlation, p_value



def calculate_spearman(ranks, frequencies):

    correlation, p_value = spearmanr(ranks, frequencies)
    return correlation, p_value



def get_quantil(fact):

    freq_values = sorted([temp['freq'] for temp in fact])
    quantile_10 = np.percentile(freq_values, [10, 90])

    print(f"10% Quantil: {quantile_10}")

    return quantile_10



def main(llm_type):

    print(f"LLM-Typ: {llm_type}")
    file_pairs = get_file_paths(llm_type)

    # Unterschedliche Metriken für jede File-Paar berechnen
    for fact_file_path, llm_file_path in file_pairs:
        fact_data = load_jsonl(fact_file_path)
        llm_data = load_jsonl(llm_file_path)

        # Rang
        rank_list = calculate_rank(fact_data, llm_data)
        #print(f"Rangliste für {os.path.basename(llm_file_path)}: {rank_list}")

        # Frequenzen
        frequencies = create_list_of_freq(fact_data)
        #print(f"Häufigkeiten für {os.path.basename(llm_file_path)}: {frequencies}")

        # P@k
        k_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        p_at_k_results = calculate_p_at_k(fact_data, llm_data, k_values)
        print(f"Berechnung für Datei: {llm_file_path}")
        for k, p_at_k in p_at_k_results.items():
            print(f"P@{k} insgesamt: {p_at_k:.4f}")

        # Hit Rate
        hit_rate = calculate_hit_rate(fact_data, llm_data)
        print(f"Hit Rate für {os.path.basename(llm_file_path)}: {hit_rate:.2f}")

        # MRR
        mrr_value = calculate_mrr(rank_list)
        print(f"MRR für {os.path.basename(llm_file_path)}: {mrr_value:.4f}")

        # Pearson-Korrelation
        pearson_corr, p_value = calculate_pearson(rank_list, frequencies)
        print(f"PK für {os.path.basename(llm_file_path)}: {pearson_corr:.4f}")
        print(f"p-Wert für {os.path.basename(llm_file_path)}: {p_value:.4f}")

        # Spearman-Korrelation
        spearman_corr, spearman_p_value = calculate_spearman(rank_list, frequencies)
        print(f"SK für {os.path.basename(llm_file_path)}: {spearman_corr:.4f}")
        print(f"p-Wert für {os.path.basename(llm_file_path)}: {spearman_p_value:.4f}")

        # 10% Quantil und 90% Quantil
        get_quantil(fact_data)



if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("llm_type", type=str, choices=["gpt", "llama", "mistral", "all_gpt", "all_llama", "all_mistral"])
    args = parser.parse_args()
    main(args.llm_type)