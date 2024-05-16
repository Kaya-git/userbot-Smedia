from asyncio import sleep
from config import conf
from handlers import send_message

TIMENOW = 0


class Schedular:
    # фоновая задача, которая ведет отсчет со старта
    async def set_time_flow():
        while True:
            global TIMENOW

            await sleep(60)
            TIMENOW += 1
            # Проверяем если есть, кто выбывает на этой минуте
            if TIMENOW in conf.timetable:

                for id in conf.timetable.pop[TIMENOW]:
                    await send_message(id)


    # Через сколько должен сразботать
    async def next_message_count_time(start_time: int, message_num: str):
        return TIMENOW + conf.message_table.message_table[f"{message_num}"][1]
