# Evaluation von großen Sprachmodellen in Bezug auf seltenes Faktenwissen (Bachelorarbeit)

## Allgemeine Informationen
Dieses Verzeichnis enthält Python-Skripte zum Sammeln von Daten, die für das Experiment benötigt werden, und zum Evalueren von seltenem Faktenwissen von großen Sprachmodellen anhand der gesammelten Daten.

Unsere Methodik umfasst eine Korrelations- und Leistungsanalyse. Um zwischen seltenen und häufigen Fakten zu unterscheiden, schätzen wir die Häufigkeiten von Fakten, die wir als Tripel (Subjekt, Relation, Objekt) verstehen, in Trainingsdaten von ausgewählten großen Sprachmodellen. Diese Fakten dienen uns auch als Vorlage für die Formulierung von Prompts, um die Antworten von großen Sprachmodellen in Form einer Rangliste zu erhalten. Mit Hilfe verschiedener Metriken führen wir eine Korrelationsanalyse durch, um lineare und monotone Zusammenhänge zwischen den Daten zu untersuchen, sowie eine Leistungsanalyse. 


## Anforderungen
- Python 3.9
- pip 24.2
- Ollama Software herunterladen (steht unter https://ollama.com zur Verfügung)
```
pip install -r requirements.txt
```

## Um das Experiment zu wiederholen, müssen folgende Schritte durchgeführt werden:


- Trainingsdatensatz herunterladen, bereinigen und in kleinere Teile zerlegen.
```
python3 load_and_clean_training_data.py
```
> Der Trainingsdatensatz, der bereits in 22 kleinere Teile aufgeteilt ist, steht unter folgendem Pfad zur Verfügung: ``` ./datasets/training_data.zip ```


- Berechnung von Häufigkeiten der Fakten mit Hilfe von distant supervision assumption (DSA) (beachten Sie die Hinweise in den Kommentaren im Code). 
```
python3 calculate_freq.py
```
> Der Faktendatensatz ist unter folgendem Pfad verfügbar: ``` ./datasets/fakt_data_raw ```
> 
> Die bereits berechnete Häufigkeiten für jede relationale Beziehung sind unter folgendem Pfad verfügbar: ``` ./datasets/fakt_data_freq ```


- Prompting von Llama 3.1 und Mistral 0.3 mit Ollama (beachten Sie die Hinweise in den Kommentaren im Code).
```
Ollama Software lokal einschalten
```
```
python3 prompt_response_generator.py
```
> Manuell erstellte Fragen-Templates sind unter folgendem Pfad verfügbar: ``` ./prompts/close_fragen_template.jsonl ```
> 
> Fertige Prompts für Llama 3.1 und Mistral 0.3 sind unter folgendem Pfad verfügbar: ``` ./prompts/prompts_for_llama_and_mistral ```
 
> Erhaltene Antworten von Llama 3.1 auf Prompts sind unter folgendem Pfad verfügbar: ``` ./prompting_result/llama_result ```
> 
> Erhaltene Antworten von Mistral 0.3 auf Prompts sind unter folgendem Pfad verfügbar: ``` ./prompting_result/mistral_result ```


- Prompting von GPT-4o per Batch-API.
```
export OPENAI_API_KEY="dein_API_KEY“
```
```
python3 gpt_prompt_per_batch.py --file_path "_"
```
> ``` --file_path ```: Pfad zur JSON-Datei mit den fertigen Batches, die an API gesendet wird. Zum Beispiel ``` "./prompts/prompts_for_gtp_per_batches/P17_gpt_batches.jsonl" ```

> Fertige Prompts für GPT-4o sind unter folgendem Pfad verfügbar: ``` ./prompts/prompts_for_gtp_per_batches ```
```
python3 gpt_prompt_per_batch.py --batch_id "_"
```
> ``` --batch_id ```: ID des Batches, um Status zu überprüfen. Zum Beispiel ``` "batch_66f3c6325f0c8190aa207ae42d8fe870" ```
```
python3 gpt_prompt_per_batch.py --file_id "_"  --output_path "_"
```
> ``` --file_id ```: ID der Datei, um Ergebnisse herunterzuladen. Zum Beispiel ``` "file-teJF9ChSNXgUv86W5xgyXjky" ```
> 
> ``` --output_path ```: Pfad, wo die heruntergeladene Datei gespeichert werden soll. Zum Beispiel ``` "./prompting_result/gpt_result" ```

> Erhaltene Antworten auf Prompts sind unter folgendem Pfad verfügbar: ``` ./prompting_result/gpt_result ```


- Evaluation der erhaltenen Daten durch Berechnung verschiedener Metriken.
```
python3 metriks.py <model_name>
```
 >Mögliche Varianten des Modellnamens:
  >
  >gpt / llama / mistral (um Ergebnisse für alle relationalen Beziehungen einzeln zu erhalten) 
  >
  >all_gpt / all_llama / all_mistral (um Ergebnisse für alle relationalen Beziehungen zusammen zu erhalten)

> Bereits berechnete Ergebnisse sind über die folgenden Pfade verfügbar:
> 
> für GPT-4o ``` ./metrics_result/metrics_gpt.jsonl ```
> 
> für Llama 3.1 ``` ./metrics_result/metrics_llama.jsonl ```
> 
> für Mistral 0.3 ``` ./metrics_result/metrics_mistral.jsonl ```
> 
> für alle Modelle über alle relationalen Beziehungen zusammen ``` ./metrics_result/metrics_all.jsonl ```
