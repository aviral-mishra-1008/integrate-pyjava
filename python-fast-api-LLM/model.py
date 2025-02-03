from pydantic_ai import Agent

class LLM_agent:
    def __init__(self):
        self.agent = Agent(  
                    'google-gla:gemini-1.5-flash',
                    system_prompt='Be concise, reply with one sentence.',
                )
        
    #The api calls are Async and generation time differs so async-await must be used for this purpose!!
    async def generate(self,prompt):
        result = await self.agent.run_sync(prompt)  
        return result.data