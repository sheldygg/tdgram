import asyncio

from tdgram import Client
from tdgram import Dispatcher
from tdgram.types import Ok


async def make_requests(client: Client):
    await client.set_log_verbosity_level(new_verbosity_level=1)
    response = await client.set_tdlib_parameters(
        use_test_dc=False,
        database_directory="tdgram_files/db",
        files_directory="tdgram_files",
        database_encryption_key=b"123456",
        use_file_database=True,
        use_chat_info_database=True,
        use_message_database=True,
        use_secret_chats=False,
        api_id=1,
        api_hash="",
        system_language_code="en",
        device_model="MacBook Pro M3",
        system_version="macOS",
        application_version="1.0",
    )
    if isinstance(response, Ok):
        await client.check_authentication_bot_token(token="123")

        r = await client.search_public_chat("tdlibchat")
        print(r)


async def main():
    client = Client(lib_path="libtdjson.dylib")

    dispatcher = Dispatcher()

    await asyncio.gather(
        dispatcher.start_polling(client),
        make_requests(client)
    )

try:
    asyncio.run(main())
except KeyboardInterrupt:
    pass
