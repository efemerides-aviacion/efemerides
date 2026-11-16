# Excepciones documentadas a la norma de grados y tratamientos (D1-a/D2-a)

Registro de los cinco casos en que una regla de capitalización de grados, tratamientos o cargos (D1-a/D2-a) exige conservar la forma existente en el texto —cuatro aceptados en la tanda de armonización del 3 de septiembre de 2026 y uno incorporado el 16 de noviembre de 2026 tras la enmienda presidencial de D1-a—. En ellos la forma registrada es correcta y el validador la omite con un aviso en lugar de marcarla como falta o desvío. Cada entrada indica el archivo donde aparece, el fragmento literal respetado y el motivo de la excepción.

- **«Presidente Aviador»** — `1911-11-30-primer-presidente-en-vuelo.md`. Trato de «Presidente» seguido de «Aviador» con mayúscula: es el apodo histórico entrecomillado, no un cargo en prosa, por lo que conserva su forma establecida. *(Nota del 16-11-2026: tras retirar `Presidente` de `CIVIL_RE`, ya no activa la regla de cargos civiles; se conserva como registro histórico de la tanda del 03-09-2026.)*
- **«Presidente Rivadavia»** — `1899-08-15-nacimiento-carola-lorenzini-primera-instructora-vuelo-suramerica.md`. No es un tratamiento dirigido a una persona: es parte del nombre propio del aeródromo de Morón, y los topónimos se escriben como los dicta su uso.
- **Etiqueta «Ciudad CCS» y su encabezado** — `1920-04-17-fundacion-escuela-aviacion-militar-venezuela.md`. El fragmento pertenece a la transcripción literal de una referencia citada (pie de fuente «Ciudad CCS»); las citas textuales se respetan tal como las publicó la fuente.
- **«general Jo…» en el caso de la corbeta Caldas** — `1987-08-18-crisis-corbeta-caldas-venezuela-colombia.md`. La secuencia corresponde al cargo civil «secretario general» de la OEA antepuesto a un nombre; según la propia norma D1-a, los cargos civiles se escriben en minúscula, así que la minúscula es la forma correcta y no una falta.
- **«presidente Hans» (Hans Thau, IFATCA)** — `1961-10-20-fundacion-ifatca-controladores-aereos.md`. Designa al presidente de la asociación civil alemana de controladores aéreos, no a un jefe de Estado; conforme a la enmienda presidencial de D1-a (16-11-2026), la minúscula es obligatoria y la comprobación `[AVISO] 16` del validador la omite con esta nota.

## Uso de este registro

Este documento es la versión para lectores humanos; vive en `docs/` junto al Manual de Estilo. La versión legible por máquina es `tools/efemerides-rangos-excepciones.txt`, en formato `archivo|fragmento|motivo`, y se mantiene versionada junto a `tools/efemerides-linter.sh` para que las excepciones sobrevivan al cambio de sesión y puedan recuperarse con el repositorio.

Toda incorporación, modificación o supresión de una excepción debe aplicarse simultáneamente en este registro humano y en el fichero legible por máquina. Si una revisión futura de los rectores cambia la norma, ambos registros deberán contrastarse antes de modificar o reclasificar alguno de los fragmentos registrados.

---
*Actualizado: 2026-11-16 — se añade la quinta excepción (`1961-10-20`, «presidente Hans») tras la enmienda presidencial de D1-a y se anota la condición histórica de las dos entradas previas sobre `Presidente`.*
