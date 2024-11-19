### Vatagens da FASTAPI
- É um framework rápido para desenvolver API's;
- Muito performático;
- Cria uma documentação automática;
- Trás consigo tipagens e processos assíncronos
- Por padrão já trás meios de comunição usando JSON como padrão

### UVICORN

Uvicorn é uma implementação de servidor web ASGI para Python.

  #####  ASGI VS WSGI

    - WSGI significa Web Server Gateway Interface e é adequado para programação ou aplicação síncrona.

    - ASGI significa Asynchronous Server Gateway Interface e é adequado para aplicações assíncronas. Ele suporta manipulação de conexões de longa duração, WebSockets e outros protocolos não HTTP. 

  #### Diferença entre ASGI e WSGI no Django

  ##### WSGI
  - O WSGI é síncrono, manipulando uma solicitação por vez e bloqueando a execução até que o processamento seja concluído.

  - O WSGI alcança a simultaneidade por meio de processos ou threads.

  - O WSGI suporta apenas HTTP, não oferecendo suporte a WebSocket.

  - Servidores WSGI populares incluem Gunicorn e mod_wsgi.

  - Os servidores WSGI usam processos ou threads para lidar com solicitações individualmente.

  - WSGI suporta HTTP/1.1.

  - O middleware WSGI é síncrono, impactando o desempenho em aplicativos assíncronos.

  ##### ASGI
  - ASGI é assíncrono, manipulando múltiplas solicitações simultaneamente sem bloquear outras solicitações.

  - O ASGI lida com simultaneidade de forma eficiente e é recomendado para conexões de longa duração ou muitos clientes.

  - O ASGI suporta HTTP e WebSocket, ideal para comunicação bidirecional em tempo real.

  - Servidores ASGI populares incluem Daphne e Uvicorn.

  - ASGI permite execução de código assíncrona, abordando questões de escalabilidade.

  - ASGI suporta HTTP/1.1, HTTP/2 e WebSockets.

  - O middleware ASGI é assíncrono, garantindo compatibilidade com aplicativos assíncronos.