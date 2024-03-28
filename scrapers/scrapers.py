from bs4 import BeautifulSoup
import json

from tools.tools import Response

class Target:
    def __init__(self, user_input) -> None:
        self.user_input = user_input
    
    async def extract_products(self) -> dict: 
        
        return 
        ...
    async def extract_user_agents(self) -> None:
        content = await Response(self.user_input).content()
        
        soup = BeautifulSoup(content, "html.parser")        
        
        # find div with user agents
        div_with_json_ua = soup.find('div', id='most-common-desktop-useragents-json-csv')
        
        # find the text area
        
        textarea = div_with_json_ua.find('textarea', {'class': 'form-control'})
        
        if textarea:
            user_agents = json.loads(textarea.text)
            
            # This deletes content from the user agent.txt file
            with open("./tools/user-agents.txt", "w") as file:
                pass
            with open("./tools/user-agents.txt", "a") as file:
                for user_agent in user_agents:
                    file.write(f'{user_agent.get("ua")}\n')

