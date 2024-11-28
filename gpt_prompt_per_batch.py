from openai import OpenAI
import os
import argparse

"""
    Der Code für den Prompten von GPT-4o mit Batch API.
    Der Code stammt aus dem OpenAi Guide: https://platform.openai.com/docs/guides/batch/overview?lang=python
    
    HINWEIS: Dieser Befehl vorher im Terminal ausführen: export OPENAI_API_KEY="dein_API_KEY“
"""

def create_batch(file_path):
    api_key = os.getenv("OPENAI_API_KEY")
    client = OpenAI(api_key=api_key)

    batch_input_file = client.files.create(
      file=open(file_path, "rb"),
      purpose="batch"
    )

    batch_input_file_id = batch_input_file.id

    batch_response = client.batches.create(
        input_file_id=batch_input_file_id,
        endpoint="/v1/chat/completions",
        completion_window="24h",
        metadata={
          "description": "nightly eval job"
        }
    )

    batch_id = batch_response.id
    batch_details = client.batches.retrieve(batch_id)
    print(f"Batch-Info für Batch-ID {batch_id}:")
    print(batch_details)


def check_status(batch_id):
    api_key = os.getenv("OPENAI_API_KEY")
    client = OpenAI(api_key=api_key)

    batch_status = client.batches.retrieve(batch_id)
    print(f"Status für Batch {batch_id}: {batch_status}")


def download_batch(file_id, output_path):
    api_key = os.getenv("OPENAI_API_KEY")
    client = OpenAI(api_key=api_key)

    file_response = client.files.content(file_id)

    with open(output_path, 'w') as output_file:
        output_file.write(file_response.text)
    print(f"Batch wurde in {output_path} gespeichert.")



def main(file_path=None, batch_id=None, file_id=None, output_path=None):

    if file_path:
        create_batch(file_path)
    elif batch_id:
        check_status(batch_id)
    elif file_id and output_path:
        download_batch(file_id, output_path)
    else:
        raise ValueError("Nicht korrekte Eingabe!")



if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("--file_path", type=str, required=False)
    parser.add_argument("--batch_id", type=str, required=False)
    parser.add_argument("--file_id", type=str, required=False)
    parser.add_argument("--output_path", type=str, required=False)

    args = parser.parse_args()

    if args.file_path:
        main(file_path=args.file_path)
    elif args.batch_id:
        main(batch_id=args.batch_id)
    elif args.file_id and args.output_path:
        main(file_id=args.file_id, output_path=args.output_path)
    else:
        parser.error("Nicht korrekte Eingabe! Für create_batch benutze --file_path; "
                     "für check_status benutze --batch_id; "
                     "für download_batch benutze --file_id und --output_path")