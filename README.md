<div align="center">
<h1>ChatGPT UI</h1>
</div>

This branch shows an example of modifying ChatGPT UI to a RAG UI.

## How to start

1. Check out the code of this project, e.g. `chatgpt-ui`, then run `make`.
2. Check out the code of the server backend code from https://github.com/agenticworkflow-dev/chatgpt-ui-server, e.g. `chatgpt-ui-server`, then run `make`.
3. You should have 3 docker images built at this step.
4. Copy .env.example to .env and add necessary Azure OpenAI settings
5. Use `docker compose up -d` to start the servers
6. BEFORE attempting to login, open 'localhost:9000/admin' in a browser. 
   username: admin
   password: password
   
   Add a dummy key as shown below

![Add Key](./add_key.jpg)

5. Open `localhost` in a browser to start

## Vector Store

Chroma db is used as the vector store. In the docker_compose.yml, a jupyter server is also added (localhost:8888)
Users can use the notebook in jupyter to create/refresh document vectors.
