"""Replicas for Telegram bot"""


class Replica:

    """Replica"""

    start = ("Привет, я помогу тебе втавить пропущенные буквы в слова.\n"
             "Правописание я ищу на сайте [грамота.ру](http://gramota.ru/).\n"
             "Пришли мне фото, и я отправлю тебе топ наиболее подходящих "
             "слов.\n\n*Команды*\n`/info` - Статисктика\n`/set_limit 3`"
             " - Установить лимит на количество наиболее подходящих слов"
             " (по умолчанию - *5*)")
    connectionError = "Сервер скоропостижно скончался\nПытаемся исправить"
    info = "Картинок обработанно: *%d*\nСлов найденно: *%d*"
    limitApplied = "Новый лимит уствновленн"
    notANumber = ("Не, друг, ты, кажись, оплошал. Мне нужно число, понимаешь?\n"
                  "Например, так: `/set_limit 3`")
    processing = "Работаем..."
    wrongFileType = ('Пупс, ты явно берега попутал. Как я тебе это обработаю? '
                     'Ты видишь там хотя бы намёк на картинку? Я лично - нет.')
