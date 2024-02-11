extends Button

var on = false
var date = ""
var chosen = false

func _process(_delta):
	if on:
		self.modulate.b = 0.0
		self.modulate.r = 0.0
	else:
		self.modulate.b = 1.0
		self.modulate.r = 1.0


func _on_pressed():
	chosen = true
