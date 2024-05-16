from pyrogram import Client, filters
from config import conf
from handlers import check_user, add_user, send_message, next_message_count_time


app = Client(
    name='Smedia', api_id=conf.botconf.api_id, api_hash=conf.botconf.api_hash
)


@app.on_message(filters.private)
async def answer(event, message):
    if message.from_user.id != (await app.get_me()).id:
        # Проверяем вхождение юзер айди в базу
        message_number = await check_user(message.from_user.id)

        if message_number == 0:
            # Добавить пользователя в базу
            await add_user(message.from_user.id)

        # Отправляем сообщение
        await app.send_message(
            chat_id=message.chat.id,
            text=conf.message_table.message_table[message_number]
        )
        # Вычисляем через сколько должно прийти следующее сообщение
        time = await next_message_count_time()

        # Добавляем на данное время айди юзера в таблицу
        conf.timetable.timetable[time] = message.from_user.id


if __name__ == "__main__":
    app.run()
