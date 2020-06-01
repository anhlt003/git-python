# Example application code for the python architecture book

## Chapters

Each chapter has its own branch which contains all the commits for that chapter,
so it has the state that corresponds to the _end_ of that chapter.  If you want
to try and code along with a chapter, you'll want to check out the branch for the
previous chapter.

https://github.com/python-leap/code/branches/all


## Exercises

Branches for the exercises follow the convention `{chatper_name}_exercise`, eg 
https://github.com/python-leap/code/tree/chapter_03_service_layer_exercise


## Requirements

* docker with docker-compose
* for chapters 1 and 2, and optionally for the rest: a local python3.7 virtualenv


## Building the containers

_(this is only required from chapter 3 onwards)_

```sh
make build
make up
# or
make all # builds, brings containers up, runs tests
```

## Running the tests

```sh
make test
# or, to run individual test types
make unit
make integration
make e2e
# or, if you have a local virtualenv
make up
pytest tests/unit
pytest tests/integration
pytest tests/e2e


## Makefile

There are more useful commands in the makefile, have a look and try them out.
#1	Initial account		https://stackoverflow.com/questions/46877667/how-to-push-a-new-initial-project-to-github-using-vs-code																								
	git config --global user.name "Your Name"																																			
	git config --global user.email youremail@domain.com																																																																						
#2	Commit route																																
	git init		                                                           																// start tracking current directory																	
	git add -A																		// add all files in current directory to staging area, making them available for commit																	
	git commit -m "commit message"        																		 // commit your changes																	
	git remote add origin "git-setting-browser"																		 // add remote repository URL which contains the required details																	
	git pull origin master                             																		 // always pull from remote before pushing																	
	git push -u origin master																		 // publish changes to your remote repository																	
																																				
	git remote -v  																		// show version of link 																	
	git remote set-url origin "git - new -browser"																		// set new origin 																	
																																				
																																				
	refer: 																																			
	git pull origin master --allow-unrelated-histories																																			
																																				
	git clone https://github.com/cosmicpython/code.git																		// clone some link / checkout to current work space																	
	cd code																																			
	git checkout chapter_02_repository																		// check out to out branches																	
	# or to code along, checkout the previous chapter:																																			
	git checkout chapter_01_domain_model																																			
