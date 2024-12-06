import pandas as pd
import random
from LLM_calls.gemini_api import Gemini_call

class PromptExperimentPipeline:
    def __init__(self, global_df, model_name="gemini-1.5-flash", api_key=None):
        self.global_df = global_df
        self.llm = Gemini_call(model_name=model_name, api_key=api_key)

    def generate_prompts(self, match_type="exact", num_samples=100, filters={}, prompt_type="general"):
        """
        Generate prompts based on match type and optional filters.
        
        Args:
            match_type (str): "exact" or "general".
            num_samples (int): Number of prompts to generate.
            filters (dict): Optional filters for the dataset (e.g., {"topic": "Politics"}).
            prompt_type (str): Type of prompt to generate ("general", "entity", "bias", etc.).
        Returns:
            List of prompts and sampled dataset.
        """
        # Apply filters to dataset
        filtered_df = self.global_df
        for key, value in filters.items():
            filtered_df = filtered_df[filtered_df[key] == value]

        # Sample data
        sampled_df = filtered_df.sample(n=num_samples) if not filtered_df.empty else pd.DataFrame()

        # Generate prompts
        prompts = []
        for _, row in sampled_df.iterrows():
            prompt = self.create_prompt(row, match_type, prompt_type)
            prompts.append((row, prompt))

        return prompts

    def create_prompt(self, row, match_type, prompt_type):
        """
        Create specific prompts based on match type and prompt type.
        """
        if match_type == "exact":
            if prompt_type == "general":
                return f"Write an article based on this headline: '{row['title']}'."
            elif prompt_type == "bias_exact":
                return f"Explain how '{row['Publisher']}' reports on '{row['topic']}' from a {row['Polarization_flag']} perspective."
            elif prompt_type == "bias_general":
                return f"Explain how '{row['Publisher']}' reports on '{row['topic']}'."
            elif prompt_type == "entity":
                person = row['entities'].get('people', [None])[0]
                organization = row['entities'].get('organizations', [None])[0]
                return f"Describe the achievements of '{person}' and their role in '{organization}'." if person and organization else None
            elif prompt_type == "sentiment":
                return f"Generate a {row['sentiment_category']} opinion piece about '{row['topic']}'."
            elif prompt_type == "general":
                return f"Generate a an opinion piece about '{row['topic']}'."
        elif match_type == "general":
            return f"Generate an article about the topic '{row['topic']}' with a {row['sentiment_category']} tone."
        else:
            raise ValueError("Invalid match type. Use 'exact' or 'general'.")

    def generate_responses(self, prompts):
        """
        Generate responses from the LLM for the given prompts.
        """
        responses = []
        for row, prompt in prompts:
            if prompt:  # Only process non-None prompts
                response = self.llm.llm_call(prompt)
                responses.append({**row.to_dict(), "generated_content": response})
        return pd.DataFrame(responses)

