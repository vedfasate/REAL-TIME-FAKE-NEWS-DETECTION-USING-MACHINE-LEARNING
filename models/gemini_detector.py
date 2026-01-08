from pydantic import BaseModel, Field
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

class FakeNewsOutput(BaseModel):
    fake: bool = Field(description="True if the news appears to be fake, otherwise False.")
    reasoning: str = Field(description="Short explanation of why it is considered fake or real.")

class GeminiDetector:
    def __init__(self, api_key="AIzaSyAa-tNSI3uQiy2dJdgRf382EFB4rf3KBHw"):
        self.parser = PydanticOutputParser(pydantic_object=FakeNewsOutput)
        self.model = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            api_key=api_key
        )

    def detect(self, news_text):
        prompt = ChatPromptTemplate.from_template("""
        You are a fake news classification expert.
        Analyze the following news and determine whether it is fake or real.

        News:
        {news_text}

        {format_instructions}
        """)

        formatted_prompt = prompt.format_messages(
            news_text=news_text,
            format_instructions=self.parser.get_format_instructions()
        )

        response = self.model.invoke(formatted_prompt)
        parsed_output = self.parser.parse(response.content)

        return parsed_output.fake, parsed_output.reasoning
