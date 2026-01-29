from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain_anthropic import AnthropicLLM
from langchain_ollama import ChatOllama

load_dotenv()


def main():

    information = '''Elon Musk (prononcé en anglais : /ˈiːlɒn ˈmʌsk/), né le 28 juin 1971 à Pretoria (Afrique du Sud), est un entrepreneur, homme d'affaires international, chef d'entreprise, homme politique et milliardaire sud-africain, canadien et américain. Il est considéré comme la personne la plus riche du monde.
                    Elon Musk commence sa carrière en affaires comme cofondateur de la société de logiciels Zip2 avec son frère, Kimbal Musk. La start-up est acquise par Compaq pour 307 millions de dollars en 1999. La même année, Musk cofonde la banque en ligne X.com, qui fusionne avec Confinity en 2000 pour former PayPal. eBay rachète PayPal en 2002 pour 1,5 milliard de dollars.'''
    summary_template = ''' given the information {information} about a person i want you to create :
                        1. a short summary
                        2. two interesting facts about them
                        '''
    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )
    
    #llm = AnthropicLLM(temperature=0, name="claude-3-haiku-20240307")   # temperature close to 0 for math code ect and 0.8 for creativity             
    llm = ChatOllama(temperature=0, model="llama3.2:3b") # local model 
    
    print("Hello from lanchain-course !")
    print(os.environ.get("ANTHROPIC_API_KEY"))
    chain = summary_prompt_template | llm # LCEL syntaxe (connect output to input as a chain) = runnable object (we can invoke)
    response = chain.invoke(input= {"information": information})
    print("Voici la réponse \n ", response)
    
if __name__ == "__main__":
    main()