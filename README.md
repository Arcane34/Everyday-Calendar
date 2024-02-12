# Everyday-Calendar
A visual representation of the Everyday calendar made by Simone Giertz to track the progress of new year's resolutions throughout the year.

## Version 2

Seeing as my previous version was rudimentary and was only able to handle a single year's worth of data, I realized I needed to make the UI more user friendly and adaptable. For the second 
attempt at implementing an everyday calendar tracker, I used Pygame again, but with the aim of making a more traditional looking calendar interface and allowing the user to choose a day
from it to then add tasks, notes and more to.

But, I wanted to keep the colour changing from the previous version as the motivation for continuing to stay true to your resolution.

This is the UI created as a result of these aims:
![](https://github.com/Arcane34/Everyday-Calendar/blob/main/pygameCalendarPrev.gif)

Upon getting this far into the UI, I realized there was a flaw in this implementation in comparison to the previous implementation, this being there was a large number of buttons on screen
and their sizes had been increased to meet the desired expectations I had, this overwhelmed the CPU as the event handling and drawing for each button was not efficient in Pygame and would 
not improve regardless of further optimizations without causing great changes in the UI.

This is when I decided to discontinue this version of this project.



## Version 1

It follows the same principle as the original idea where you essentially press a button to activate the light of a specific day in the year to show you have followed the resolutions for that particular day.

However, as it is made via code, instead of implementing every button as a basic light system, I wanted the button to cycle through an array of colors seamlessly creating an aesthetically pleasing pattern across
the board if the user has ensured they follow their resolutions on multiple days consecutively. This is done to ensure the action of pressing the button is fun, pleasing and satisfying to the user, giving them a 
reward for their effort.


Here is a preview of the usage of the project:
![](https://github.com/Arcane34/Everyday-Calendar/blob/main/calendarUsage.gif)



And here is a preview of what a completed calendar would look like:
![](https://github.com/Arcane34/Everyday-Calendar/blob/main/completedCalendar.gif)