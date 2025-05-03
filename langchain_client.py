from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

import asyncio

load_dotenv()

llm = ChatOpenAI()

async def main():
    async with MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                "args": [
                    "/Users/isagron/sw_projects/learning/mcp-crash-course/servers/math_server.py"
                ],
            },
            "weather": {
                "url": "http://localhost:8000/sse",
                "transport": "sse",

            },
        }
    ) as client:
        agent = create_react_agent(llm, client.get_tools())
#        result = await agent.ainvoke({"messages": "what is 2+2?"})
        result = await agent.ainvoke({"messages": "what is the weather in Beer sheva?"})

        print(result["messages"][-1].content)

if __name__ == "__main__":
    asyncio.run(main())