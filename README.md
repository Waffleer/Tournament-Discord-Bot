# Tournament-Discord-Bot
This is a discord bot intended for use for MNCS tournaments to get match times and manage players. In progress and my not be finished due to my own laziness.


uses a api to do all of the heavy lifting and a discord bots calls the api
gives a lot more freedom for coding and not everything will be in the discord python file


use run.bat to start the api, it will run at localhost, use the link in the console and go to /docs to interact



file structure

/    

	- root
	
	- where all of the code directories will be based off of

/logsFull.txt  

	- full logs of api

/main.py  

	- where discord bot code will go

/api.py     

	- where api code will go

/test.py       

	- were api will be developed for ease of testing
	
	- final code will be copied and pasted to api.py for each release
	
	- might have multiple test.py files for different releases
													 
run.bat/run.sh

	- run files for api, bat for windows and sh for linux
	
	- this is for server and api testing
													 
/servers/   

	- where all of the information for each server is stored

/servers/{name of server}/         

	- each server will have a folder
	
/servers/{name of server}/admin.txt        

	- lists what channels can run admin commands
	
/servers/{name of server}/secondary.txt   

	- lists what channels have secondary perms, tbd

/servers/{name of server}/matchs/          

	- stores all of the matches information
	
/servers/{name of server}/matchs/{match id number}   

	- stores all the data associated with the match

/servers/{name of server}/teams/                   

	- stores all of the team folders
	
/servers/{name of server}/teams/{name of team}/           

	- stores all of the team folders
	
/servers/{name of server}/teams/{name of team}/players.txt    

	- has the names of all the players on the team
	
/servers/{name of server}/teams/{name of team}/matchs.txt    

	- has the ids of all of the matches associated with the teams

/servers/{name of server}/players/  

	- stores all of the players information
	
/servers/{name of server}/players/{player name}.txt   

	- stores all of the information related to each player

\n\n\n

api commands - still in progress of creating

