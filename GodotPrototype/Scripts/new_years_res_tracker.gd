extends Control

@onready var pathProg = $Path2D/PathFollow2D
@onready var explosion = $Explosion
@onready var calendar = $PanelContainer/Calendar
@onready var todayResButton = $Button
@onready var backg = $ParallaxBackground

var start = false
var speed = 1
var finished =false
var resolvedDays = []

func _ready():
	resolvedDays = LoadsaveData.u_data["Resolution Days"]
	if calendar.getTodayDateStr() in resolvedDays:
		todayResButton.disabled = true
	


func _process(delta):
	backg.scroll_offset.y += (len(resolvedDays)+ 1)*40*delta
	
	if calendar.getTodayDateStr() in resolvedDays:
		todayResButton.disabled = true
		
		
	if start:
		pathProg.progress_ratio += speed * delta
		if pathProg.progress_ratio > 0.93:
			start = false
			pathProg.visible = false
			explosion.emitting = true
			pathProg.progress_ratio = 0.0
			finished = true
	
	if finished:
		var todayButton = calendar.findButtonForDate(calendar.getTodayDateStr())
		todayButton.on = true
		if !(calendar.getTodayDateStr() in resolvedDays):
			resolvedDays.append(todayButton.date)
			var data = [resolvedDays, LoadsaveData.u_data["Task/Note Days"]]
			LoadsaveData.saveData(data)




func _on_button_pressed():
	if !start and !explosion.emitting:
		start = true
		pathProg.visible = true
		
	
		
		
