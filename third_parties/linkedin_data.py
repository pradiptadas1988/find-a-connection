import os
import requests


def get_linkedin_data(linkedin_profile_url, is_mock=True):
    """scrape information from LinkedIn profiles,
    Manually scrape the information from the LinkedIn profile"""
    if is_mock:
        response = requests.get(
            "https://gist.githubusercontent.com/pradiptadas1988/421921ccfd6a6c6aee790ce34fdb2e42/raw/3a5bb360125e5e47c37e6961734716e276d7892d/pradipta_das_linkedin.json"
        )
    else:
        print(f'the linkedin url using for fetching data: {linkedin_profile_url}')
        headers = {"Authorization": "Bearer " + os.environ["PROXYCURL_API_KEY"]}
        api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"

        response = requests.get(
            api_endpoint, params={"url": linkedin_profile_url}, headers=headers
        )
    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data


if __name__ == "__main__":
    url = "https://www.linkedin.com/in/pradipta-das-6ab786a0/"
    linkedin_profile_data = get_linkedin_data(url, False)
    print(linkedin_profile_data)
