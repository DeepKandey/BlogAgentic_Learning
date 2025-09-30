import uvicorn
from fastapi import FastAPI,Request
from src.graphs.graph_builder import GraphBuilder
from src.llms.openAI_llm import OpenAI_llm

import os
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

os.environ["LANGSMITH_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

# APIs

@app.post("/blogs")
async def create_blogs(request:Request):
    data=await request.json()
    topic=data.get("topic","")
    language=data.get("language","")

    # get the llm object
    OpenAI_llm_Obj = OpenAI_llm()
    llm = OpenAI_llm_Obj.get_llm()
    
    # get the graph
    graph_builder=GraphBuilder(llm)
    if language and topic:
        graph=graph_builder.setup_graph(usecase="language")
        state=graph.invoke({"topic":topic,"current_language":language.lower()})
    elif topic:
        graph=graph_builder.setup_graph(usecase="topic")
        state=graph.invoke({"topic":topic})

    return {"data":state}

if __name__=="__main__":
    uvicorn.run("app:app",host="0.0.0.0",port=8000,reload=True)