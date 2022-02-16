from aiogram.types import Message
from parsing import parsing_films, search_film
from loader import dp


@dp.message_handler()
async def search(message: Message):
    answer = await search_film(message.text.lower())
    if answer != False:
        mess = "Название: {}\nОписание: {}\nСсылка: {}".format(answer["Title"], answer["Description"], answer["URL"])
        await message.answer(mess)
    else:
        await message.answer("Дай подумаю...")
        await parsing_films()
        answer = await search_film(message.text.lower())
        if answer != False:
            mess = "Название: {}\nОписание: {}\nСсылка: {}".format(answer["Title"], answer["Description"], answer["URL"])
            await message.answer(mess)
        else:
            await message.answer("Я не нашел такой фильм")
