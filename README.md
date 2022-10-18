# Tournament-Discord-Bot
This is a discord bot intended for use for MNCS tournaments to get match times and manage players. In progress and my not be finished due to my own laziness.


uses a api to do all of the heavy lifting and a discord bots calls the api
gives a lot more freedom for coding and not everything will be in the discord python file


use run.bat to start the api, it will run at localhost, use the link in the console and go to /docs to interact

data structures

Player Data Structures

    - name
    
    - dataAdded
    
    - team
    
    - rank
    
    - age
    


file structure

	/    

		- root
	
		- where all of the code directories will be based off of

	/logsFull.txt  

		- full logs of api

	    - Will have a extra line above text, will be fixed in code

	/main.py  

		- where discord bot code will go

	/api.py     

		- where api code will go
	
	/test.py       

		- were api will be developed for ease of testing
	
		- final code will be copied and pasted to api.py for each release
	
		- might have multiple test.py files for different releases
													 
	/run.bat or run.sh

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

	/servers/{name of server}/logs.txt 

		- full logs of api

 	   	- Will have a extra line above text, will be fixed in code

	/servers/{name of server}/matches/          

		- stores all of the matches information
	
	/servers/{name of server}/matches/{match id number}   

		- stores all the data associated with the match

	/servers/{name of server}/teams/                   

		- stores all of the team folders
	
	/servers/{name of server}/teams/{name of team}/           

		- stores all of the team folders
	
	/servers/{name of server}/teams/{name of team}/players.txt    

		- has the names of all the players on the team
	
	/servers/{name of server}/teams/{name of team}/matches.txt    

		- has the ids of all of the matches associated with the teams

	/servers/{name of server}/players/  

		- stores all of the players information
	
	/servers/{name of server}/players/{player name}.txt   

		- stores all of the information related to each player
	




api commands - still in progress of creating

 	   - if a function is declared as "public" then it can be accessed via api

	   - if a function is declared as "private" then it can be accessed via api

 	   - if a function is declared as "discord accessible" then it can be accessed via discord bot

		- not implemented yet


log commands 

	def logServer(serverName, logStr): 

		- logs to server log file as well as system log file

		- private


	def logSystem(logStr): 

		- logs only to system log file

		- private


information commands

	def getServers(): 

 	   - gets list of servers

 	   - public

	def getTeams(serverName): 

	    - gets list of teams on a server

 	    - public

	def getPlayers(serverName): 

	    - gets list of players on a server

 	    - public

	def getMatches(serverName): 
    
  	  - gets list of matches on a server

          - public

	def getServerPlayerInfo(serverName, playerName): 

 	   - returns player information
    
  	   - returns a dict
	


server commands

	def genServer(user, serverName): 

 	   - Generates a server and file structure

 	   - public

 	   - discord accessible

	def addServerTeams(user, serverName, teamName): 

 	    - adds team to a server

	    - public
	
	    - discord accessible

	def addServerPlayer(user, serverName, playerName): 

 	   - adds player to server with empty data structure



	def editServerPlayerTeam(user, serverName, playerName, team): 

 	   - edits player team
    
  	   - team name is not used to determine players on each team

	def editServerPlayerRank(user, serverName, playerName, rank): 

    - edits player rank

	def editServerPlayerAge(user, serverName, playerName, age): 

  	  - edits player age

	def editServerPlayerComplete(user, serverName, playerName, team, rank, age): 

  	  - edits player team, rank, age

      

    def addTeamPlayer(user, serverName, teamName, playerName): 
    
        - adds a player under a team
        
        - changes player information to the team as well



other commands 

	def genNum(num, list): 

 	   - generates a random number "num" digits that isn't on the inputted list

	def strToDict(string): 

 	   - turns a string into a dict via json

  	   - string dict must have " not '
