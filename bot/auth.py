import logging
from pyrogram import Client
from pyrogram.types import Message
from bot.tools import get_blocked_user_ids

try:
    from local_db import trusted_group, bl_users
except ImportError:
    trusted_group = []
    bl_users = []


def ensure_not_bl(func):
    async def wrapper(client: Client, message: Message):
        if message.from_user:
            user_id = message.from_user.id
            if user_id in bl_users:
                logging.warning(f'User {user_id} is in blacklist! Ignoring message.')
                return None
            else:
                return await func(client, message)
        else:
            return await func(client, message)
    return wrapper


if __name__ == '__main__':
    print('Listing blocked users')

    import asyncio
    from session import config

    me = Client(
        'me',
        api_id=config['kuma']['api_id'],
        api_hash=config['kuma']['api_hash']
    )

    async def main():
        async with me:
            blocked_users = await get_blocked_user_ids(me)

        for i in blocked_users:
            print(i.id, '\t', i.first_name)

    asyncio.run(main())