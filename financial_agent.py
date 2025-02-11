from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai

import os
from dotenv import load_dotenv
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
# Web search Agent
web_serch_agent = Agent(
   name = "Web search Agent",
   role = "Search the web from the information",
   model = Groq(id = "llama3-groq-70b-8192-tool-use-preview",api_key=GROQ_API_KEY),
   tools = [DuckDuckGo()],
   instructions= ['Always include sources'],
   show_tool_calls= True,
   markdown= True,
)


# Financial Agent
financ_agent = Agent(
   name = "Finance AI Agent",
   model = Groq(id = "llama3-groq-70b-8192-tool-use-preview",api_key=GROQ_API_KEY),
   tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True)],
   instructions=["Use tables to display the data"],
   show_tool_calls=True,
   markdown=True,
    
)

# Defining multi AI Agent
mutli_ai_agent = Agent(
    team = [web_serch_agent,financ_agent],
    instructions=["Always include sources","Use table to display the data"],
    show_tool_calls=True,
    markdown=True
)

mutli_ai_agent.print_response("Summarize analyst recommendation and share the latest news for NVIDA",stream=True)

