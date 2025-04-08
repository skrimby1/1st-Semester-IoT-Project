# Alkometer-Vejrbesked
Alkometer + Vejrbesked funktionalitet udviklet personligt af mig under min gruppes 1. semester projekt, ved brug af MicroPython, MQ3 gas-sensor, ADC, LCD-display samt ESP32

Funktionalitet:
* 🌦️ Laver API-kald for vejret i København på nuværende tidspunkt og 10 timer frem. Når cyklen modtager en besked fra vores anden ESP via ESP-NOW om at cyklen er aflåset,  viser den på et display om der kommer frostvejr, hedeslag eller regn. Her bedes brugeren om at parkere ansvarligt.
* 🍺 Ved hjælp af en gas-sensor som måler ethanol-indhold via ADC, vil den anmode om en alkometer prøve hvis brugeren forsøger at oplåse sin cykel indenfor specifikke tidsrammer. På baggrund af resultatet af prøven, vil cyklen forblive låst hvis målingen er for høj, eller låse op for cyklen promillen er under en fastsat værdi.
