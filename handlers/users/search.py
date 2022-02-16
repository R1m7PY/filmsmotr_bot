from aiogram.types import Message
from parsing import parsing_films, search_film
from loader import dp


@dp.message_handler()
async def search(message: Message):
    answers = await search_film(message.text.lower())
    if answers != False:
        for answer in answers:
            mess = "Название: {}\nОписание: {}\nСсылка: {}".format(answer["Title"], answer["Description"], answer["URL"])
            await message.answer(mess)
    else:
        await message.answer("Дай подумаю...")
        await parsing_films()
        answers = await search_film(message.text.lower())
        if answers != False:
            for answer in answers:
                mess = "Название: {}\nОписание: {}\nСсылка: {}".format(answer["Title"], answer["Description"], answer["URL"])
                await message.answer(mess)
        else:
            await message.answer("Я не нашел такой фильм")
