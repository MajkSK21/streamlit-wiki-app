import streamlit as st
from langchain_groq import ChatGroq
from langchain.chains import LLMMathChain,LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.agents.agent_types import AgentType
from langchain.agents import Tool,initialize_agent
from langchain.callbacks import StreamlitCallbackHandler

#SET UP THE STREAMLIT APP 
st.set_page_config(page_title = "Text To MAath Problem Solver And Data Search Assistant",page_icon="📚")
st.title("Text To Math Problem Solver Using Google Gemma 2")
groq_api_key = st.sidebar.text_input(label = "Groq API Key",type = "password")
if not groq_api_key:
    st.info("Please add your Groq API Key to continue ")
    st.stop()
llm = ChatGroq(model="Gemma2-9b-It",groq_api_key=groq_api_key)

##INITIALIZE THE TOOLS
wikipedia_wrapper=WikipediaAPIWrapper()
Wikipedia_tool = Tool(
    name ="Wikipedia",
    func=wikipedia_wrapper.run,
    description ="A Tool For Searching the Internet to find the various information on the topic mention "
)

## INITIALIZE THE MATH TOOL

math_chain=LLMMathChain.from_llm(llm=llm)
calculator=Tool(
    name="Calculator",
    func=math_chain.run,
    description="A Tools for answering math related queries.Only input mathematical expression need to provided "
)

prompt="""
You are a agent task for solving users mathematical question logically arrive at the solution and detailed explaination and display it point wise for the question below
Question:{question}
Answer:
"""
prompt_template=PromptTemplate(
    input_variables=["question"],
    template=prompt
)

## COMBINE ALL THE TOOLS INTO CHAIN

chain=LLMChain(llm=llm,prompt=prompt_template)
reasoning_tool=Tool(
    name="Reasoning Tool",
    func=chain.run,
    description="A tool for answering logic-based and reasoning questions."
)

## INTIALIZE THE AGENTS
assistant_agent = initialize_agent(
    tools=[Wikipedia_tool, calculator, reasoning_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False,
    handle_parsing_errors=True
)
if "messages" not in st.session_state:
    st.session_state["messages"]=[
        {"role":"assistant","content":"Hi,I'm a Math Chatbot who can answer all your maths problem"}
]
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg['content'])

## LETS START THE INTERACTION
question=st.text_area("Enter your question:","I have 5 bananas and 7 grapes.I eat 2 bananas ang give away 3 grapes.Then I buy a dozen apple and 2 packs of blueberries.Each pack of blueberries contains 25 berries.How many total piece of fruit do I have at the end?")
if st.button("find my answer"):
    if question:
        with st.spinner("Generate response.."):
            st.session_state.messages.append({"role":"user","content":question})
            st.chat_message("user").write(question)
            # Inside the button logic:
            st_cb = StreamlitCallbackHandler(st.container(),expand_new_thoughts=False)
            response = assistant_agent.run(st.session_state.messages, callbacks=[st_cb])

                                         
            st.session_state.messages.append({'role':'assistant',"content":response})
            st.write('### response:')
            st.success(response)
    else:
        st.warning("please enter the question")




