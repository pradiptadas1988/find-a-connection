import os
import getpass
from dotenv import load_dotenv
from typing import Tuple

from agents.linkedin_lookup_agent import look_up_linkedin_url
from find_connection import find_a_connection
from third_parties.linkedin_data import get_linkedin_data
from output_parsers import Summary

load_dotenv()


def get_search_result(input_info_param: str) -> Tuple[Summary, str]:
    if "OPENAI_API_KEY" not in os.environ:
        os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your OpenAI API key: ")
        print(f'Set: {os.environ["OPENAI_API_KEY"]}')

    linkedin_url = look_up_linkedin_url(
        input_info_param, is_mock=False
    )  # is_mock by default true
    linkedin_data = get_linkedin_data(
        linkedin_url, is_mock=False
    )  # mock is true by default
    result = find_a_connection(linkedin_data)
    return result, linkedin_data.get("profile_pic_url")


if __name__ == "__main__":
    # input_info = look_up_linkedin_url("Pradipta Das Allstate India Lead Software Engineer Bangalore")
    get_search_result("https://in.linkedin.com/in/pradipta-das-6ab786a0")
    # Pradipta Das National institute of technology agartala lead allstate Bangalore
