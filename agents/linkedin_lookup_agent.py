from dotenv import load_dotenv

load_dotenv()
from langchain_openai import ChatOpenAI
from langchain_core.tools import Tool
from langchain.prompts.prompt import PromptTemplate
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
from tools.tools import get_profile_url_tavily, get_profile_url_tavily_demo


def look_up_linkedin_url(search_param: str, is_mock=True) -> str:
    if is_mock:
        linkedin_url = "https://www.linkedin.com/in/pradipta-das-6ab786a0"
    else:
        find_linkedin_url_template = """ given the full name {name_of_person} find the LinkedIn Profile Page URL. 
                    The title of the page should be {name_of_person} | LinkedIn.
                    {name_of_person} holds the information about education institute, profession, skill set and location
                    If there more profiles for the {name_of_person} provide only the one profile LinkedIN URL
                """
        find_linkedin_url_template_prompt = PromptTemplate(
            template=find_linkedin_url_template, input_variable=["name_of_person"]
        )

        llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
        tools_for_agent = [
            Tool(
                name="Crawl Google 4 linkedin profile page",
                func=get_profile_url_tavily,
                description="useful for when you need to get the Linkedin Page URL",
            )
        ]
        react_prompt = hub.pull("hwchase17/react")
        agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
        agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)

        result = agent_executor.invoke(
            input={
                "input": find_linkedin_url_template_prompt.format(
                    name_of_person=search_param
                )
            }
        )
        linkedin_url = result["output"]

    print(f'found the linkedin url: {linkedin_url}')
    return linkedin_url


if __name__ == "__main__":
    # print(look_up_linkedin_url("Pradipta Das National Institute of technology agartala Lead Software Engineer at Allstate India Bangalore"))
    # print(look_up_linkedin_url("Arijit Nayak National Institute of technology agartala PwC Labs Bangalore"))
    print(look_up_linkedin_url("Kumar Rituraj National Institute of technology agartala module lead mphasis bangalore"))
