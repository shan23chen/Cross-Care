## Todo
- Co-occurrences
	- Update paths for co-occurrence run now moved folders
- Logits tweaking
	- I think we should trial setting system prompt for True / False instead of a/b/c/d or 1/2 - should be no tokenization issues fot True/False
	- should we set max_length to full prompt +1 to constrain output in t/f setting?
	- Run all 
- propagation results
	- join logits notebook
		- Convert to .py script
		- needs to account for langauage, hf vs hf_tf vs api and the american context
		- Keep all separate for now
		- Save combined dfs appropriately
	- Adjust the logit notebooks to account for added vars 
	- Add comparision notebook across the new vars 
- app
	- Update web app paths now moved folders
- Repo
	- Overall and sub READMEs 
		- add details on folders
		- add bash runs to readme
	- Sort docker container etc