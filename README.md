# To do

- [X] API
  - [X] core
    - [X] User
    - [X] User management and grouping
  - [X] Task
    - [X] Models
    - [X] Serializers
    - [X] Views
    - [X] User authentication
    - [X] Throttling & Pagination
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
- `CSRF_COOKIE_SECURE` (Default: False)
- `SESSION_COOKIE_SECURE` (Default: False)
- `SECURE_SSL_REDIRECT` (Default: False)
- `SECURE_HSTS_SECONDS` (Default: 0)
- `SECURE_HSTS_INCLUDE_SUBDOMAINS` (Default: False)
- `SECURE_HSTS_PRELOAD` (Default: False)
### Database variables
  - `DB_ENGINE`
  - `DB_NAME`
  - `DB_HOST`
  - `DB_PORT`
  - `DB_USER`
  - `DB_PASS`
  - If not provided, **sqlite** will be used.