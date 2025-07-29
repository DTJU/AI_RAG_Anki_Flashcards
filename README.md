# AI_RAG_Anki_Flashcards
Create Anki (Question-Answer) Flashcards with a LLM and your documents via a RAG Pipeline

Introduction:
The goal of this short program is to automatically create a specific number of flashcards, which are question and answer pairs, to a desired topic based on a document.
In this case the document can be a PDF File and the topic can be a querry about this document or specific topics inside.
The context of the document is devided into chunks stored into a faiss vector store during runtime.
Here is a Langchain QA RAG (retrieval augmented generation) Pipeline used with a OpenAI endpoint for the LLM.
These question answer pairs are formated in a CSV file which can be imported in the popular Anki App for spaced repetition.

How to use:
In the input section you can define a path to a PDF file and as well a filename for the generated CSV file.
Also a querry can be defined depending on the document.
The used AI Model can be selected and these must match the available models on the OpenAI API page. 
For the AI Model it is important, that the context tokens are large enough for your document.
Also the API Key from OpenAI is needed. 
Finally you can enter the number of flashcards that should be created in this deck.

In Anki you can import this deck via Files -> Import and give the deck a name.
