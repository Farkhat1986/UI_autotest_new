@echo off
echo [+] Creating Docker network 'grid'
docker network create grid 2>nul

echo [+] Starting Selenium Hub
docker run -d --name selenium-hub --network grid -p 4444:4444 -p 4442:4442 -p 4443:4443 selenium/hub:4.21

echo [+] Starting Chrome Node (2 instances)
docker run -d --name chrome-node --network grid ^
    -e SE_NODE_MAX_SESSIONS=2 ^
    -e SE_NODE_OVERRIDE_MAX_SESSIONS=true ^
    -e SE_EVENT_BUS_HOST=selenium-hub ^
    -e SE_EVENT_BUS_PUBLISH_PORT=4442 ^
    -e SE_EVENT_BUS_SUBSCRIBE_PORT=4443 ^
    selenium/node-chrome:4.21

echo [+] Starting Firefox Node (2 instances)
docker run -d --name firefox-node --network grid ^
    -e SE_NODE_MAX_SESSIONS=2 ^
    -e SE_NODE_OVERRIDE_MAX_SESSIONS=true ^
    -e SE_EVENT_BUS_HOST=selenium-hub ^
    -e SE_EVENT_BUS_PUBLISH_PORT=4442 ^
    -e SE_EVENT_BUS_SUBSCRIBE_PORT=4443 ^
    selenium/node-firefox:4.21

echo [+] Selenium Grid доступен: http://localhost:4444
pause
