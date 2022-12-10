# fifteen-puzzle
Repository contains implementation of exemplary fifteen-puzzle solving techniques

![Tests](https://github.com/odpaleniek1337/radio-generator/actions/workflows/tests.yml/badge.svg)


## Prerequisites
Implemented using `Python 3.8.10`

1. Clone repository
2. Create venv `python -m venv {VENV_NAME}` and activate it - `{VENV_NAME}\Scripts\activate`
3. Install fifteen-puzzle as package - while in repo directory `pip install -e .` or `python -m pip install -e .`
4. To run locally

Usage

> main.py [(-b/--bfs | -d/--dfs | -i/--idfs) {LRUD, LRDU, ...} | (-f/--bf | -a/--astar) {1,2}] 
> 
> [-e/--display] 
> 
> [-h/--help] 
>
> [-n/--input_file <INPUT_FILE>] 
> 
> [-o/--output_file <OUTPUT_FILE>]

Example invokes - file paths depending on os
    
`python .\src\fifteen_puzzle\main.py -n input1.sav --bfs DRUL --display`

`python src\fifteen_puzzle\main.py < tests\prepared_boards\input8.15sav > output.15sav --dfs LRUD`

Example output

`10, LDRUDURDLU`

`5, URUUL`

To run tests

- Install tox `pip install tox` or `python -m pip install tox`
- Run tox `python -m tox`


## Implemented algorithms
- Breadth First Search
- Depth First Search
- Iterative Deepening Depth First Search
- Greedy Best First Search
- A*


## Tests
- Tested with the use of `pytest` on `ubuntu-20.04` and `windows-latest`
- Checked linting with the use of `flake8`


## Additional information
- Heuristic algorithms were optimized by adding hashes of previously visited nodes, so if a new node would be exactly the same it won't be added as a state to check.

- Brute-force algorithms have limitation of max_depth of newly created node equal to 20