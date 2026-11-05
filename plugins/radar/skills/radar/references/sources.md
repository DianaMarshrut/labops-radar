# Подключение почты, календаря и задач

Веди пользователя по шагам для его системы. Один шаг за сообщение.
Подключаем один раз. После этого радар читает источники по расписанию или по фразе «радар».

| Источник | Claude | ChatGPT |
|---|---|---|
| Gmail, Google Календарь | Коннекторы Gmail и Google Calendar | Приложения Gmail и Google Calendar |
| Outlook (Microsoft 365) | Коннектор Microsoft 365 (рабочие аккаунты) | Приложения Outlook Email и Outlook Calendar |
| Яндекс Почта / Яндекс 360 | Через пересылку на Gmail | Через пересылку на Gmail |
| Битрикс24: задачи и календарь | MCP (ключ в настройках MCP) | файлом (Excel/CSV) |

---

## Gmail и Google Календарь

Гайд: https://guides.labopsai.pro/google-workspace-claude

**Claude.** Коннекторы есть на всех тарифах, включая Free.
1. «Customize» → «Connectors».
2. «Gmail» → «Connect» → войди в Google-аккаунт.
3. То же для «Google Calendar».

**ChatGPT.**
1. «Settings» → «Apps».
2. «Gmail» → подключить. То же для «Google Calendar».
3. В разрешениях выбери «Allow read actions».

Проверка: «покажи отправителей трёх последних писем и мою ближайшую встречу».

---

## Outlook, Microsoft 365

**Claude.** Коннектор для рабочих аккаунтов Microsoft (Entra ID).
1. «Customize» → «Connectors» → «Microsoft 365» → «Connect».
2. Войди в рабочий аккаунт.

**ChatGPT.**
1. «Settings» → «Apps» → «Outlook Email» и «Outlook Calendar» → подключить.

---

## Яндекс Почта / Яндекс 360

Подключается через пересылку почты на Gmail и экспорт календаря в Google.

**Почта → Gmail:**
1. В Яндекс Почте: «Настройки» → «Правила обработки» → пересылка на свой Gmail.
2. Или в Gmail: «Настройки» → «Аккаунты» → «Получать почту с других аккаунтов» → добавь Яндекс.
3. Дальше подключай Gmail через коннектор (шаги выше).

**Яндекс Календарь → Google Календарь:**
1. В Яндекс Календаре: настройки → «Экспорт» → скопируй iCal-ссылку.
2. В Google Календаре: «Добавить календарь» → «По URL» → вставь ссылку.
3. Дальше подключай Google Календарь через коннектор.

Источник: https://yandex.com/support/calendar/common/sync/export.html

---

## Битрикс24: задачи и календарь

Гайд: https://guides.labopsai.pro/bitrix24-claude

**Через MCP.** Следуй шагам из гайда. Права — только чтение задач и календаря.

Ключи и токены в чат не вставляй — храни только в настройках MCP-подключения.

---

## Источники (проверено 27.10.2026)

- Claude, коннекторы Google: https://support.claude.com/en/articles/10166901
- Claude, Microsoft 365: https://support.claude.com/en/articles/12542951
- ChatGPT, подключённые приложения: https://help.openai.com/en/articles/11487775
- ChatGPT, приложения Google: https://help.openai.com/en/articles/10408842
