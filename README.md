# Afsluttende projekt for 1.semester som IT-Teknolog
Alkometer + Vejrbesked funktionalitet blev udviklet primært personligt af mig under min gruppes 1. semester projekt, dog i samråd af min gruppe. Ved brug af MicroPython, MQ3 gas-sensor, ADC, GPS, I2C, LCD-display samt ESP32. Projektet havde også en masse andre funktionaliteter, som blev udviklet af min gruppe - som f.eks. at den kunne detecte om cyklen befandt sig i en high-risk zone. Samtidig havde vi opsat en server, hvor via MQTT blev sendt data til et dashboard som så visualiserede dataen.

Funktionalitet:
* 🌦️ Laver API-kald for vejret i København på nuværende tidspunkt og 10 timer frem. Når cyklen modtager en besked fra vores anden ESP via ESP-NOW om at cyklen er aflåset,  viser den på et display om der kommer frostvejr, hedeslag eller regn. Her bedes brugeren om at parkere ansvarligt.
* 🍺 Ved hjælp af en gas-sensor som måler ethanol-indhold via ADC, vil den anmode om en alkometer prøve hvis brugeren forsøger at oplåse sin cykel indenfor specifikke tidsrammer. På baggrund af resultatet af prøven, vil ESP'en sende en besked via ESP-NOW til låse-boksen at cyklen skal forblive låst hvis målingen er for høj, eller låse op for cyklen hvis promillen er under en fastsat værdi. Samtidig vil den afspille en lyd samt vise på display

# ENGLISH
The breathalyzer + weather notification functionality was developed primarily by me during my group’s 1st-semester project, although in consultation with my group. The project used MicroPython, an MQ3 gas sensor, ADC, GPS, I2C, LCD display, and ESP32. The project also included many other functionalities developed by my group-for example, detecting whether the bike was in a high-risk zone. Additionally, we set up a server where data was sent via MQTT to a dashboard that visualized the information.

Functionality:

🌦️ Makes API calls for the weather in Copenhagen at the current time and 10 hours ahead. When the bike receives a message from our other ESP via ESP-NOW that it is locked, it shows on a display whether frost, heatstroke, or rain is expected. The user is thereby prompted to park responsibly.

🍺 Using a gas sensor that measures ethanol content via ADC, it requests a breathalyzer test if the user attempts to unlock their bike within specific time frames. Based on the test result, the ESP sends a message via ESP-NOW to the lock box to either keep the bike locked if the alcohol level is too high or unlock the bike if the blood alcohol is below a set threshold. At the same time, it plays a sound and displays information on the screen.

![487757683_1483293399306072_969653230632725275_n](https://github.com/user-attachments/assets/6fe0a5b8-1e7f-4182-b7e5-0f6cc03b4f37)
![487468799_638294185767774_6345072392564367234_n](https://github.com/user-attachments/assets/75e9eca6-7b35-45a8-9bbc-ebf4014d2d67)
![487883858_1580164912647600_4125169835379546696_n](https://github.com/user-attachments/assets/39a63255-aca4-48ae-b8ef-2702f37497f3)


