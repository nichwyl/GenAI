#!/usr/bin/env python
# coding: utf-8

# In[3]:



# In[ ]:


from flask import Flask,request,render_template
from textblob import TextBlob
import google.generativeai as palm

model={
    'model':"models/chat-bison-001"
}

palm.configure(api_key='AIzaSyDSNgSJNhe6c8Yoca9TLiSJsKLwZ1Hw9vQ')

app = Flask(__name__)
@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/main",methods=["GET","POST"])
def main():
    r=request.form.get("q")
    return(render_template("main.html",r=r))

@app.route("/text",methods=["GET","POST"])
def text():
    return(render_template("text.html"))

@app.route("/text_reply",methods=["GET","POST"])
def text_reply():
    q=request.form.get("q")
    r=palm.chat(**model,messages=q)
    return(render_template("text_reply.html",r=r.last))
           
@app.route("/end",methods=["GET","POST"])
def end():
    return(render_template("end.html"))
    
if __name__ == "__main__":
    app.run()


# In[3]:


pip install google-generativeai


# In[ ]:




