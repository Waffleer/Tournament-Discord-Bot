# Tournament-Discord-Bot
This is a discord bot intended for use for MNCS tournaments to get match times and manage players. In progress and my not be finished due to my own laziness.


uses a api to do all of the heavy lifting and a discord bots calls the api
gives a lot more freedom for coding and not everything will be in the discord python file


use run.bat to start the api, it will run at localhost, use the link in the console and go to /docs to interact

bot join url : https://discord.com/api/oauth2/authorize?client_id=1032121033186091031&permissions=268487760&scope=bot

data structures

# Player Data Structures

    - name
    
    - dataAdded
    
    - team
    
    - rank
    
    - age
    


# file structure

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
	




# api commands - still in progress of creating

 	   - if a function is declared as "public" then it can be accessed via api

	   - if a function is declared as "private" then it can be accessed via api

 	   - if a function is declared as "discord accessible" then it can be accessed via discord bot

		- not implemented yet


# log commands 

	def logServer(serverName, logStr): 

		- logs to server log file as well as system log file

		- private


	def logSystem(logStr): 

		- logs only to system log file

		- private


# information commands

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

		  - used for debug

	def getServerPlayerInfo(serverName, playerName): 

 	   - returns player information
    
  	   - returns a dict

    def getTeamMatches(serverName, teamName): 
    
        - returns the dictionaries for all of the matches associated with a team
	
	def getTeamRoster(serverName, teamName): 
	
		- returns all of the player's data for a team

# server commands

	def genServer(user, serverName): 

 	   - Generates a server and file structure

 	   - public

 	   - discord accessible

	def addServerTeam(user, serverName, teamName): 

 	    - adds team to a server

	    - public
	
	    - discord accessible

	def addServerPlayer(user, serverName, playerName): 

 	   - adds player to server with empty data structure

       - must have "#" in playerName or other function will break




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
        
        - changes player information to the team

    def removeTeamPlayer(user, serverName, teamName, playerName): 
    
        - removes a player under a team
        
        - changes player information to the "" team





    def addMatch(user, serverName, date, time, team1, team2): 
    
        - Adds match object to the matches folder
        
        - then adds the matches to the related teams
        
        - date should be in a dd/mm/year format
        
        - time should be in a hour:day format in military time

    def removeMatch(user, serverName, matchTag): 
    
        - Removes a match object to the matches folder
    
        - then removes the matches in the related teams




# other commands 

	def genNum(num, list): 

 	   - generates a random number "num" digits that isn't on the inputted list

	def strToDict(string): 

 	   - turns a string into a dict via json

  	   - string dict must have " not '

# To Do:
	- add a record system for wins and losses

	- adds team roles to players on a team

	- add failsafes for every method

	- filter players not on a team

	- get server logs

	- add rules for team names and shit, no parenthesis, one word (no spaces), no banned characters

	- Documentation

	- change api response for add and remove match to be string instead of list for date and time

	- return match information command

		- need to check if necessary

	- make matches have data slots for bo3 or bo5 to record results

	- change league {role} via bot

		- role is from player data not discord roles

		- makes it so that any find by role doesn't break

	- delete tournament or have a check when creating 
	
	- deal with reactions, would add a level of professionalism
	
	- add status to player data object, (active, inactive, kicked)

	- add try catch error codes for discord commands if no parameters are passed though

	- work on !help function

	- pin !adminHelp to adminChannel so that it doesn't need to be spammed


# Things to do next

	- add to config file

		- if you want tournament channels visable to non tournament members

		- add timezone

	- get tournaments

	- add discord username to player data structure

		- store with #

			- change last ")" or 5th to last charater to a # when storing and pulling from database

	- decide what commands can be run outside the adminchannel
	
	- Need to make discord outputs more user friendly

## License
[MIT](https://choosealicense.com/licenses/mit/)
