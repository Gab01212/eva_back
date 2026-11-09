# eva_back
## Nombre de la Organización o Plataforma: RedSalud Vital
## Modelo de Negocio / Giro: Centro de atención médica ambulatoria y prestaciones clínicas
##  Integrantes del Equipo: [Gabriel Urra - 21944558-k]
## Entidad de Contexto / Agrupación (ORM): EspecialidadMedica
## Entidad Principal Gestionable (ORM): PrestacionMedica
##  Propósito de la Sesión (request.session): Canasta de Exámenes: Pre-agendamiento temporal de prestaciones con cálculo dinámico de copago según previsión.

## 🤖 Bitácora de Prompts de Inteligencia Artificial (Criterio 2.1.4)

### Caso 1: Arquitectura ORM y Protección de Relaciones
* **Prompt Utilizado:** "Actúa como experto en Django. Necesito estructurar un modelo de Centro Médico donde una Especialidad tenga múltiples Prestaciones. Exijo que si se intenta borrar una especialidad con prestaciones activas, Django lo impida por seguridad mediante ORM, y además agregar un validador numérico para evitar aranceles negativos."
* **Respuesta Técnica de la IA:** Sugirió el uso de `on_delete=models.PROTECT` y la importación de `MinValueValidator` junto con los decoradores en `clean_()`.
* **Adaptación Aplicada:** Se integró directamente en `models.py` para los campos `arancel_base` y la relación `ForeignKey` de `PrestacionMedica`.

### Caso 2: Optimización de Consultas con `select_related`
* **Prompt Utilizado:** "Tengo una vista de catálogo público en Django que lista todas las prestaciones y muestra su especialidad asociada. ¿Cómo evito el problema de consultas N+1 al renderizar las tarjetas Bootstrap?"
* **Respuesta Técnica de la IA:** Recomendó el uso de `.select_related('especialidad')` directamente en el queryset de la vista `catalogo_prestaciones`.
* **Adaptación Aplicada:** Se aplicó en `views.py` para mejorar drásticamente el rendimiento de lectura del catálogo público.

### Caso 3: Manejo de Carrito / Canasta Transitoria en Sesión
* **Prompt Utilizado:** "Muéstrame cómo estructurar una lógica basada puramente en `request.session` en Django para acumular servicios clínicos con cantidades, subtotal y un botón para vaciar la sesión sin utilizar base de datos."
* **Respuesta Técnica de la IA:** Proveyó la estructura de diccionario anidado dentro de `request.session['canasta']` iterando llaves por ID de producto.
* **Adaptación Aplicada:** Se adaptó para calcular el subtotal, aplicar una simulación de bonificación por previsión de salud y vaciar la sesión de manera segura tras confirmar el pre-agendamiento.