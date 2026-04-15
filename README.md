# BagazhStorage — Агрегатор камер хранения багажа

Статический сайт под партнёрские программы Qeepl и Radical Storage.

## Структура

- `index.html` — главная (топ-80 городов)
- `[city-slug]/index.html` — страница города (488 городов)
- `assets/style.css` — стили
- `assets/main.js` — скрипты
- `vercel.json` — конфиг Vercel
- `generate.py` — скрипт регенерации из SIa.txt

## Реф-ссылки

| Партнёр | Параметры |
|---|---|
| Qeepl | `?discount=SBUHJKBO` |
| Radical Storage | `?erid=2VtzqvWLUd3&track_id=c29a6ef0036745e991d79dad4-549016&utm_term=travelpayouts` |

## Деплой на Vercel

```bash
git init
git add .
git commit -m "init luggage storage catalog"
# Создай репо на GitHub, затем:
git remote add origin https://github.com/YOUR_USER/luggage-catalog.git
git push -u origin main
# В Vercel: Import Project → выбери репо → Deploy
```

## Регенерация

Положи обновлённый SIa.txt рядом с generate.py и запусти:
```bash
python generate.py
```
