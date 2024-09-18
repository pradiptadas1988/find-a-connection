from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI

from output_parsers import summary_parser


def find_a_connection(connection_detail: str):
    find_template = """
        given the Linkedin information {information} about a person I want you to create:
        1. A short summary
        2. two interesting facts about them
        \n{format_instructions}
    """

    find_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=find_template,
        partial_variables={
            "format_instructions": summary_parser.get_format_instructions()
        },
    )

    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
    llm_chain = find_prompt_template | llm | summary_parser

    result = llm_chain.invoke(input={"information": connection_detail})

    return result


if __name__ == "__main__":
    find_a_connection("")
