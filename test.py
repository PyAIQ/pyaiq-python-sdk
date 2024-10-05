# client_app.py
import asyncio
from lifecycle import RESTEvent, WebSocketEvent


async def main():
    # Choose communication type
    # For REST
    rest_client = RESTEvent(base_url="http://localhost:8000")
    init_response = await rest_client.on_init({"user": "Alice"})
    print("REST on_init response:", init_response)

    query_response = await rest_client.on_query("select * from data")
    print("REST on_query response:", query_response)

    close_response = await rest_client.on_close('aaaaa')
    print("REST on_close response:", close_response)

    # For WebSockets
    ws_client = WebSocketEvent(ws_url="ws://localhost:8000/ws")
    init_response = await ws_client.on_init({"user": "Bob"})
    print("WebSocket on_init response:", init_response)

    query_response = await ws_client.on_query("select * from info")
    print("WebSocket on_query response:", query_response)

    close_response = await ws_client.on_close(1)
    print("WebSocket on_close response:", close_response)

    # Close WebSocket connection
    await ws_client._client.close()

if __name__ == "__main__":
    asyncio.run(main())
