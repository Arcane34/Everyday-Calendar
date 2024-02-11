extends Control



func _on_new_year_res_tracker_pressed():
	get_tree().change_scene_to_file("res://Scenes/new_years_res_tracker.tscn")


func _on_quit_pressed():
	get_tree().quit()
