@echo off
echo [+] Запуск только упавших тестов...
pytest --last-failed -v --tb=short
pause
