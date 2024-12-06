import os
import logging

import google.generativeai as genai
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")

load_dotenv(dotenv_path)

logging.basicConfig(
    filename="gemini_call.log",
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s",
)

logger = logging.getLogger()


class Gemini_call:
    def __init__(
        self,
        model_name="gemini-1.5-flash",
        api_key=None,
        temperature=None,
        max_tokens=None,
        k_value=None,
        **kwargs,
    ):
        """
        Initializes the LLMCall class with a specific model and optional parameters.

        Args:
        - model_name (str): The Gemini model to use, default is "gemini-1.5-flash".
        - api_key (str): The API key for Google Generative AI, can be provided or fetched from environment.
        """
        self.model_name = model_name
        self.api_key = api_key or os.getenv("API_KEY")
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.k_value = k_value
        self.additional_params = kwargs

        # Configure the generative AI client
        genai.configure(api_key=self.api_key)

        # Load the model
        self.model = genai.GenerativeModel(self.model_name)

    def llm_call(self, prompt: str) -> str:
        try:
            # Log the entire prompt
            logger.info(f"Sending prompt: {prompt} to model {self.model_name}")
            response = self.model.generate_content(prompt)

            # Log the full response from the model
            logger.info(f"Received response: {response.text}")

            return response.text
        except Exception as e:
            logger.error(f"Error generating response: {e}")
            return ""


# Usage example:
if __name__ == "__main__":
    llm = Gemini_call(model_name="gemini-pro")
    response = llm.llm_call("Tell me one sentence on how to easily win at chess.")
    print(response)
