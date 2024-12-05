from tqdm import tqdm
import os
from datetime import datetime

def extract_entities(text):
    """
    Extract named entities from text using SpaCy.
    """
    doc = nlp(text)
    entities = {"people": [], "organizations": [], "locations": []}
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            entities["people"].append(ent.text)
        elif ent.label_ == "ORG":
            entities["organizations"].append(ent.text)
        elif ent.label_ == "GPE":
            entities["locations"].append(ent.text)
    return entities



def process_and_add_to_global(
    dataset, dataset_name, column_mapping, topic=None, subtopic=None, additional_columns=None, save_dir=None
):
    """
    Process a dataset and integrate it into the global dataframe, dynamically updating the schema with a progress bar.

    Args:
    - dataset: pd.DataFrame, the input dataset.
    - dataset_name: str, the name of the dataset/source.
    - column_mapping: dict, mapping from dataset-specific column names to global column names.
    - topic: str, the high-level topic (e.g., 'COVID').
    - subtopic: str, the sub-topic within the main topic (e.g., 'Vaccines').
    - additional_columns: dict, optional additional columns and their default values for this dataset only.
    - save_dir: str, directory to save the global dataframe. Defaults to the current working directory.
    """
    global global_df

    print(f"Processing dataset: {dataset_name}")
    # Progress bar for the number of rows
    with tqdm(total=len(dataset), desc=f"Processing rows in {dataset_name}", unit="row", disable=True) as pbar:
        # Apply column mapping to standardize dataset
        standardized_data = pd.DataFrame()
        for global_col, dataset_col in column_mapping.items():
            if dataset_col in dataset.columns:
                standardized_data[global_col] = dataset[dataset_col]
            else:
                raise ValueError(f"Column '{dataset_col}' missing in the dataset '{dataset_name}'.")

        # Add standard fields
        standardized_data["source"] = dataset_name
        standardized_data["timestamp"] = pd.to_datetime(standardized_data.get("timestamp", None), errors="coerce")
        standardized_data["topic"] = topic
        standardized_data["subtopic"] = subtopic

        # Extract entities using SpaCy
        if "body" in standardized_data.columns:
            standardized_data["entities"] = [
                extract_entities(text) if pd.notna(text) else None for text in tqdm(
                    standardized_data["body"], desc="Extracting entities", leave=False, unit="entry"
                )
            ]
        elif "title" in standardized_data.columns:
            standardized_data["entities"] = [
                extract_entities(text) if pd.notna(text) else None for text in tqdm(
                    standardized_data["title"], desc="Extracting entities", leave=False, unit="entry"
                )
            ]
        else:
            standardized_data["entities"] = None

        # Add additional columns dynamically
        if additional_columns:
            for col_name, default_value in additional_columns.items():
                standardized_data[col_name] = default_value

                # Ensure column exists in global_df with None for prior rows
                if col_name not in global_df.columns:
                    global_df[col_name] = None

        # Simulate processing rows to update the progress bar
        for _ in standardized_data.iterrows():
            pbar.update(1)

    # Append new data to global_df
    global_df = pd.concat([global_df, standardized_data], ignore_index=True)

    # Save the updated global dataframe
    save_dir = save_dir or os.getcwd()  # Default to current working directory if no directory specified
    save_path = os.path.join(save_dir, "global_dataset.csv")
    global_df.to_csv(save_path, index=False)
    print(f"Global dataframe saved to: {save_path}")
