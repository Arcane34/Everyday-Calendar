extends Node

const SAVE_FILE = "user://save_file.dat"
var u_data = {"Resolution Days": [],
"Task/Note Days": []}

func _ready():
	loadData()

func loadData():
	if not FileAccess.file_exists(SAVE_FILE):
		saveData([[],[]])
	
	var file = FileAccess.open(SAVE_FILE, FileAccess.READ)
	u_data = file.get_var()
			
	if not u_data.is_empty():
		print(u_data)
	
	file.close()
	
# save data function that saves the data in the variable into the save file
func saveData(data):
	var file = FileAccess.open(SAVE_FILE, FileAccess.WRITE)
	u_data = {"Resolution Days": data[0],
		"Task/Note Days": data[1]}
	file.store_var(u_data)
	file.close()
