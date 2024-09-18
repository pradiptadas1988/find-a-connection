from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI


def get_some_info(connection_detail):
    find_template = """
        give me 2 crisp points of Whom the below description is

        {information}
    """

    find_prompt_template = PromptTemplate.from_template(find_template)
    find_prompt_template.format(information=connection_detail)

    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
    llm_chain = find_prompt_template | llm

    result = llm_chain.invoke(input={"information": connection_detail})

    return result


if __name__ == "__main__":
    get_some_info("")
