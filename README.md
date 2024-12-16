# To do

- [ ] API
  - [X] core
    - [X] User
    - [ ] User management and grouping
  - [ ] Task
    - [X] Models
    - [X] Serializers
    - [X] Views
    - [X] User authentication
    - [ ] Throttling & Pagination
- [ ] Website
  - [ ] Login page
  - [ ] Task
    - [ ] Task view and management
  - [ ] Caching
- [ ] Telegram bot
  - [ ] Task
    - [ ] View
    - [ ] Notification
- [ ] Deployement
  - [ ] Python script
  - [ ] Github actions

# Environment variables

- `SECRET_KEY`
- `DEBUG` ('True' or 'False', Default: True)
- `ALLOWED_HOSTS` (Separated by comma)
### Database variables
  - `DB_ENGINE`
  - `DB_NAME`
  - `DB_HOST`
  - `DB_PORT`
  - `DB_USER`
  - `DB_PASS`
  - If not provided, sqlite will be used.