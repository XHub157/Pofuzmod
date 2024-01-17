# meta developer: @Pofuzmod_official

from .. import loader, utils

import random
from contextlib import suppress
from telethon.tl.types import Message, MessageMediaPhoto


bullr = [
   "Скинь ножки","ну не","Света, НОЖКИ!!!","Ножки быстро@*#","ну пжпж","жду ножки","СкИнЬ НоЖеНьКи СвоИ","Скинешь ножки?","Ты можешь скинуть ножки?","Хочешь показать ножки?","Готова показать ножки?","Ты скинешь ножки?","Можешь показать свои ножки?","Стесняешься скинуть ножки?","Зачем скидывать ножки?","Готова поделиться ножками?","Не хочешь показать свои ножки?","Покажешь свои красивые ножки?","Такие красивые ножки, покажешь еще раз?","Не стесняйся, скидывай ножки!","Ты не против скинуть ножки?","Скинешь ножки для меня?","Покажи мне свои ножки?","Готова скинуть ножки?","Почему не хочешь скинуть ножки?","Не стесняйся, можно скинуть ножки!","Ты можешь скинуть ножки на фото?","Скинешь ножки прямо сейчас?","Можешь ли ты скинуть ножки?","Ты скинешь ножки для меня?","Покажи мне свои ножки прямо сейчас!","Не хочешь показать свои ножки?","Такие красивые ножки, скинешь для меня?","Можешь ли ты скинуть ножки на камеру?","Скинь ножки и поделись со мной!","Покажи свои ножки во всей красе!"]


@loader.tds
class FuckerMod(loader.Module):
    strings = {
        "name": "💮Света, скинь ножки."
    }
    
    async def client_ready(self, client, db):
        self.db = db
        self.users = self.db.get("fucker", "users", [])
        self.phrases = self.db.get("fucker", "phrases", [])
    
    def add_phrase(self, phrase: str):
        self.phrases.append(phrase)
        self.db.set("fucker", "phrases", self.phrases)
    
    def add_user(self, user_id: int):
        self.users.append(user_id)
        self.db.set("fucker", "users", self.users)
    
    def remove_user(self, user_id: int):
        self.users.remove(user_id)
        self.db.set("fucker", "users", self.users)
    
    async def clearbullcmd(self, message):
        """Никого не просить скинуть ножки"""
        
        self.users = []
        self.db.set("fucker", "users", self.users)
        
        await utils.answer(
            message=message,
            response="<b><emoji document_id=5215260113291455937>🔚</emoji>Должна 100₽ на карту</b>"
        )
    
    async def bullacmd(self, message):
        """Добавить фразу | .bulla <фраза>"""
        
        args = utils.get_args_raw(message)
        
        if not args:
            return await utils.answer(
                message=message,
                response="<b><emoji document_id=5213181173026533794>⚠️</emoji>Не указан аргумент</b>"
            )
        
        self.add_phrase(args)
        
        await utils.answer(
            message=message,
            response="<b><emoji document_id=5213406375341731253>✅</emoji>Фраза добавлена</b>"
        )
    
    async def bullrcmd(self, message):
        """Вкинуть рандомное скинь ножки"""
        
        await utils.answer(
            message=message,
            response=random.choice(bullr + self.phrases)
        )
    
    async def addbullcmd(self, message):
        """Просить Свету скинуть ножки. <reply>"""
        
        reply = await message.get_reply_message()
        
        if reply is not None:
            if reply.from_id is not None:
                await utils.answer(
                    message=message,
                    response="<b><emoji document_id=5213147006561692829>🔛</emoji>Твои ноженьки;)</b>"
                )

                self.add_user(reply.from_id)
            
            else:
                await utils.answer(
                    message=message,
                    response="<b><emoji document_id=5215642288071387368>❌</emoji> Модуль не работает на анонимных администраторах или каналах</b>"
                )

        else:
            await utils.answer(
                message=message,
                response="<b><emoji document_id=5213181173026533794>⚠️</emoji> Нужен реплай</b>"
            )
    
    async def rmbullcmd(self, message):
        """Не просить ножки. <reply>"""
        
        reply = await message.get_reply_message()
        
        if reply is not None:
            await utils.answer(
                message=message,
                response="<b>Не скинула ножки, звоню дяде Серëже</b>"
            )
            
            try:
                self.remove_user(reply.from_id)
            except:
                await utils.answer(
                    message=message,
                    response="<b><emoji document_id=5213181173026533794>⚠️</emoji> Это не та Света!</b>"
                )

        else:
            await utils.answer(
                message=message,
                response="<b><emoji document_id=5213181173026533794>⚠️</emoji> Нужен реплай</b>"
            )
    
    async def watcher(self, message):
        if getattr(message, "from_id", None) in self.users:
            await message.reply(random.choice(bullr + self.phrases))