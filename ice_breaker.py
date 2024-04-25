import os
from dotenv import load_dotenv
if __name__ == '__main__':
  print("hello langchain")
  #print(os.environ['OPENAI_API_KEY'])
  load_dotenv()
  print('After load_dotenv()', os.getenv('OPENAI_API_KEY'))
  #print(load_dotenv.get('OPENAI_API_KEY'))