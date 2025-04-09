# Alkometer-Vejrbesked
Alkometer + Vejrbesked funktionalitet udviklet primært personligt af mig under min gruppes 1. semester projekt, dog i samråd af min gruppe. Ved brug af MicroPython, MQ3 gas-sensor, ADC, LCD-display samt ESP32. Projektet havde også en masse andre funktionaliteter, som blev udviklet af min gruppe

Funktionalitet:
* 🌦️ Laver API-kald for vejret i København på nuværende tidspunkt og 10 timer frem. Når cyklen modtager en besked fra vores anden ESP via ESP-NOW om at cyklen er aflåset,  viser den på et display om der kommer frostvejr, hedeslag eller regn. Her bedes brugeren om at parkere ansvarligt.
* 🍺 Ved hjælp af en gas-sensor som måler ethanol-indhold via ADC, vil den anmode om en alkometer prøve hvis brugeren forsøger at oplåse sin cykel indenfor specifikke tidsrammer. På baggrund af resultatet af prøven, vil ESP'en sende en besked via ESP-NOW til låse-boksen at cyklen skal forblive låst hvis målingen er for høj, eller låse op for cyklen hvis promillen er under en fastsat værdi. Samtidig vil den afspille en lyd samt vise på display

Projektet i sidste ende - jeg stod for design af 3D-print i CAD-software, samt implementering og optimering af kredsløb (som dog var en fælles indsats af gruppen):
![487757683_1483293399306072_969653230632725275_n](https://github.com/user-attachments/assets/6fe0a5b8-1e7f-4182-b7e5-0f6cc03b4f37)
![487468799_638294185767774_6345072392564367234_n](https://github.com/user-attachments/assets/75e9eca6-7b35-45a8-9bbc-ebf4014d2d67)
![487883858_1580164912647600_4125169835379546696_n](https://github.com/user-attachments/assets/39a63255-aca4-48ae-b8ef-2702f37497f3)
