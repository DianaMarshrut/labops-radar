# Радар — утренняя сводка руководителю

Каждое утро — одна короткая сводка в твоём ИИ: какие встречи сегодня, что горит, кому ответить.
Читается с телефона за минуту. Только читает — ничего не отправляет и не меняет.

## Как поставить

### Claude Code

```
/plugin marketplace add DianaMarshrut/labops-radar
/plugin install radar@labopsai-radar
```

### Codex

```
codex plugin marketplace add DianaMarshrut/labops-radar
```

Затем `/plugins` → Install → начни новую сессию.

### Claude (claude.ai и приложение)

1. «Customize» → «Plugins» → «Add marketplace» → вставь `DianaMarshrut/labops-radar` → «Install».
2. Подключи коннекторы Gmail и Google Calendar («Customize» → «Connectors»).
3. Создай проект «Радар» и напиши в нём: «Настрой радар».

Альтернатива — загрузить ZIP вручную:
1. Скачай `dist/radar.zip`. Распаковывать не нужно.
2. «Customize» → «Skills» → «+» → «+ Create skill» → «Upload a skill» → выбери `radar.zip`.

### ChatGPT

Создай проект «Радар», добавь в файлы проекта `chat-instruction.md`.
Напиши в проекте: «Работай по инструкции из файлов проекта. Настрой радар».

## Откуда данные

**Почта и календарь:**
1. **Gmail + Google Календарь** — через коннекторы.
   Гайд: https://guides.labopsai.pro/google-workspace-claude
2. **Яндекс Почта / Яндекс 360** — через пересылку на Gmail.
   Шаги: внутри навыка → «Источники данных».
3. **Outlook (Microsoft 365)** — через коннектор Microsoft 365.

**Задачи:**
4. **Битрикс24** — через MCP.
   Гайд: https://guides.labopsai.pro/bitrix24-claude

**Нет подключения:**
5. **Файл или текст** — загрузи экспорт почты, задач или календаря (CSV, Excel, TXT) или
   вставь текст в чат. Радар сделает сводку и укажет, каких источников не хватает.

## Ограничения

- Без подключения к почте и календарю радар не работает (или загрузи файл/текст).
- Запускается только по команде.

## Команды

- «Покажи утро»
- «Что горит по клиенту Х?»
- «Подготовь ответ на письмо от Ивана»

## Безопасность

- Только чтение. Коннекторы почты и календаря используй с правами «Читатель».
- Ключи и токены в чат не вставляй.

## Что в репозитории

| Путь | Для чего |
|---|---|
| `plugins/radar/skills/radar/` | Навык: `SKILL.md`, справочники `references/`, шаблоны сводки и настроек |
| `dist/radar.zip` | Навык в архиве — для загрузки в Claude |
| `chat-instruction.md` | Навык одним текстом — для ChatGPT и Codex |
| `scripts/build.py` | Пересобирает `dist/radar.zip` и `chat-instruction.md` после правок |

## Для разработчика

Нужен Python 3.10+.

```
python3 scripts/build.py
```

## Другие капсулы labopsai

- [Пульс — дашборд руководителя](https://github.com/DianaMarshrut/labops-puls)
- [След — встреча → задачи](https://github.com/DianaMarshrut/labops-sled)
