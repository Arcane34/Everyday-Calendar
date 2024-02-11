extends VBoxContainer

@onready var monthYear = $ToolBar/MonthYear
@onready var days = $Days


var today = Time.get_date_dict_from_system()

const SECS_PER_DAY: int = 24 * 60 * 60



var monthBrowsing = today.month
var dayBrowsing = today.day
var yearBrowsing = today.year
var firstDayOfMonthBrowsing = Time.get_unix_time_from_datetime_string(str(yearBrowsing) +"-"+ str(monthBrowsing) +"-"+ "01 00:00:00")

var months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
var monthDays = [31,28,31,30,31,30,31,31,30,31,30,31]
var buttonScene = load("res://Scenes/calendar_button.tscn")

var resolvedDays = []

func _ready():
	resolvedDays = LoadsaveData.u_data["Resolution Days"]
	
	
	
	monthYear.text = months[monthBrowsing - 1] + " " + str(yearBrowsing)
	if ((yearBrowsing - 2024) % 4 == 0):
		monthDays[1] = 29
	
	for j in Time.get_datetime_dict_from_unix_time(firstDayOfMonthBrowsing).weekday:
		var button = buttonScene.instantiate()
		button.self_modulate.a = 0.0
		button.disabled = true
		days.add_child(button)
	
	for i in (monthDays[monthBrowsing - 1]):
		var button = buttonScene.instantiate()
		button.text = str(i+1)
		days.add_child(button)
	
	setDates()
	
	

func _process(_delta):
	for k in days.get_children():
		if k.date in resolvedDays:
			k.on = true
		else:
			k.on = false








func setDates():
	for i in days.get_children():
		if !i.disabled:
			i.date = i.text +"-"+ str(monthBrowsing) +"-"+ str(yearBrowsing)
			
func getTodayDateStr():
	return  str(today.day) +"-"+ str(today.month) +"-"+ str(today.year)


func findButtonForDate(curDate):
	for i in days.get_children():
		if i.date == curDate:
			return i
			


func _on_back_pressed():
	for j in Time.get_datetime_dict_from_unix_time(firstDayOfMonthBrowsing).weekday:
		days.remove_child(days.get_child(0))
	
	
	monthBrowsing = (monthBrowsing - 1) 
	if monthBrowsing == 0:
		monthBrowsing = 12
		yearBrowsing -= 1
		
	if ((yearBrowsing - 2024) % 4 == 0):
		monthDays[1] = 29
	else:
		monthDays[1] = 28
	
	if days.get_child_count() >= (monthDays[monthBrowsing - 1]):
		for i in (days.get_child_count() - monthDays[monthBrowsing - 1]):
			days.remove_child(days.get_child(-1))
	else:
		
		for i in (monthDays[monthBrowsing - 1] - days.get_child_count()  ):
			var button = buttonScene.instantiate()
			button.text = str(days.get_child_count()+1)
			days.add_child(button)
	
	firstDayOfMonthBrowsing = Time.get_unix_time_from_datetime_string(str(yearBrowsing) +"-"+ str(monthBrowsing) +"-"+ "01 00:00:00")
	for j in Time.get_datetime_dict_from_unix_time(firstDayOfMonthBrowsing).weekday:
		var button = buttonScene.instantiate()
		button.self_modulate.a = 0.0
		button.disabled = true
		days.add_child(button)
		days.move_child(button,0)
	
		
	
			
	setDates()
	
	monthYear.text = months[monthBrowsing - 1] + " " + str(yearBrowsing)
	

func _on_front_pressed():
	for j in Time.get_datetime_dict_from_unix_time(firstDayOfMonthBrowsing).weekday:
		days.remove_child(days.get_child(0))
	
	
	monthBrowsing = (monthBrowsing + 1) 
	if monthBrowsing == 13:
		monthBrowsing = 1
		yearBrowsing += 1
		
	if ((yearBrowsing - 2024) % 4 == 0):
		monthDays[1] = 29
	else:
		monthDays[1] = 28
	
	if days.get_child_count() >= (monthDays[monthBrowsing - 1]):
		for i in (days.get_child_count() - monthDays[monthBrowsing - 1]):
			days.remove_child(days.get_child(-1))
	else:
		for i in ( monthDays[monthBrowsing - 1] - days.get_child_count() ):
			var button = buttonScene.instantiate()
			button.text = str(days.get_child_count()+1)
			days.add_child(button)
	
	firstDayOfMonthBrowsing = Time.get_unix_time_from_datetime_string(str(yearBrowsing) +"-"+ str(monthBrowsing) +"-"+ "01 00:00:00")
	for j in Time.get_datetime_dict_from_unix_time(firstDayOfMonthBrowsing).weekday:
		var button = buttonScene.instantiate()
		button.self_modulate.a = 0.0
		button.disabled = true
		days.add_child(button)
		days.move_child(button,0)
	
	
			
	setDates()

	monthYear.text = months[monthBrowsing - 1] + " " + str(yearBrowsing)
	
