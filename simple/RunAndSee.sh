# wip 
# lux-ai-2021 command not recognized

# lux-ai-2021 main.py main.py --out=replay.json
# main picks agent.py

# npx lux-ai-vis replay.json
# lux-ai-vis replay.json

function pause(){
   read -p "$*"
}

timestamp=$(date +%s)
replay_file_name= "$timestamp.json"
echo "$replay_file_name"
pause 'Press [Enter] key to continue...'

run_game_command= "lux-ai-2021 main.py main.py --out=$replay_file_name"
eval run_game_command
pause 'Press [Enter] key to continue...'

see_game_command= "lux-ai-vis $replay_file_name"
eval see_game_command
pause 'Press [Enter] key to continue...'
