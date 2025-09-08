# CozyBot
**This is a passion project, not for profit, discord bot to be used on a server amongst friends.**  
**There is to be no distribution without written consent from Sean Tank.**  
**There is to be no monetary gain from anyone distributing this bot.**  
**Thank you.** 

## Credits:
**Development:** Sean Tank  
**Server Hosting:** Sean Tank  
**Bot Hosting:** Sean Tank  
**Database Hosting:** Sean Tank  

## Current Functionality:
- Moderation
  - Members
    - Member Joins the Server
    - Member Leaves the Server
  - Message
    - WIP

## Local Development:
You must create a .env with  
  - ```'BOT_TOKEN=YourTwentyDigetDiscordToken'```  
  and 
  - ```'DB_CONNECTION_STRING'=postgresql+psycopg2://<Your database connection string>```  
Then run the Docker command:  
- ```docker compose -f docker-compose-dev.yml up```

To update the migrations:  
- ```alembic revision --autogenerate -m "<Migration message>"```  
- ```alembic upgrade head```  
