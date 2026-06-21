# Guía de Personalización — GitHub Profile Template

> Esta guía te explica paso a paso cómo tomar esta plantilla y adaptarla a tu perfil de GitHub.

---

## 📋 Tabla de Contenidos

1. [Requisitos previos](#requisitos-previos)
2. [Configuración Requerida](#configuración-requerida)
3. [Paso 1: Use this template (recomendado)](#paso-1-use-this-template-recomendado)
4. [Paso 2: Reemplazar USERNAME](#paso-2-reemplazar-username)
5. [Paso 3: Personalizar placeholders adicionales](#paso-3-personalizar-placeholders-adicionales)
6. [Paso 4: Banner de perfil](#paso-4-banner-de-perfil)
7. [Paso 5: Texto del typing SVG](#paso-5-texto-del-typing-svg)
8. [Paso 6: Enlaces a redes sociales](#paso-6-enlaces-a-redes-sociales)
9. [Paso 7: Sección de proyectos](#paso-7-sección-de-proyectos)
10. [Paso 8: Push y verificación](#paso-8-push-y-verificación)
11. [Automatizaciones Opcionales](#automatizaciones-opcionales)
12. [Paso 9: Configurar permisos de Actions](#paso-9-configurar-permisos-de-actions)
13. [Paso 10: Detalles de los workflows](#paso-10-detalles-de-los-workflows)
14. [Paso 11: Ejecutar workflows por primera vez](#paso-11-ejecutar-workflows-por-primera-vez)
15. [Solución de problemas](#solución-de-problemas)
16. [Preguntas frecuentes](#preguntas-frecuentes)
17. [Referencias](#referencias)

---

## Requisitos previos

- Una cuenta de [GitHub](https://github.com)
- Git instalado en tu computadora (opcional, puedes usar la interfaz web de GitHub)
- Un repositorio especial cuyo nombre **debe coincidir exactamente** con tu nombre de usuario de GitHub

---

## Configuración Requerida

Estos pasos son necesarios para que tu perfil funcione en GitHub.

## Paso 1: Use this template (recomendado)

La forma más simple de empezar:

1. Haz clic en **Use this template** → **Create a new repository** en la parte superior de la página del template.
2. Nombra el repositorio **exactamente igual a tu nombre de usuario de GitHub**.
3. Selecciona **Public**.
4. Haz clic en **Create repository from template**.

> ⚠️ **IMPORTANTE**: El nombre del repositorio debe ser **idéntico** a tu nombre de usuario de GitHub. Sin esto, el README no aparecerá en tu perfil.

> 👤 **Para mantenedores**: El dueño del repositorio debe habilitar **Template repository** en Settings → General → Template repository para que aparezca el botón `Use this template`.

### Avanzado: Fork como alternativa

Si planeas seguir las actualizaciones del repositorio original y fusionar cambios más adelante, puedes hacer un **Fork** en lugar de usar el template. Ten en cuenta que los forks no aparecen automáticamente en tu perfil — usa esta ruta solo si te sientes cómodo con flujos de merge de Git.

Después de hacer el fork, renómbralo para que coincida con tu nombre de usuario de GitHub (Settings → Repository name) y marca "Copy the main branch only".

---

## Paso 2: Reemplazar USERNAME

La plantilla usa la palabra clave `USERNAME` como marcador de posición para tu nombre de usuario de GitHub. Este marcador aparece en:

- URLs de estadísticas de GitHub
- Enlaces a repositorios en la sección de proyectos
- Contador de visitas al perfil
- Animación de la serpiente (snake)
- Footer (wave capsule)

### Método recomendado: buscar y reemplazar global

**En la interfaz web de GitHub**:
1. Abre tu repositorio.
2. Haz clic en `README.md`.
3. Haz clic en el ícono de lápiz (✏️) para editar.
4. Presiona `Ctrl+F` (o `Cmd+F` en Mac).
5. Busca `USERNAME` y reemplázalo por **tu nombre de usuario de GitHub**.
6. Repite hasta que no queden ocurrencias de `USERNAME`.

**En tu computadora (local)**:
```bash
# Abre README.md en tu editor favorito y usa buscar y reemplazar global
# VS Code: Ctrl+Shift+H → buscar "USERNAME" → reemplazar con "tu-usuario"
# O usa sed:
sed -i 's/USERNAME/tu-usuario/g' README.md
```

> ✅ **Verificación**: Después del reemplazo global, busca `USERNAME` en el archivo. No debería quedar ninguno.

---

## Paso 3: Personalizar placeholders adicionales

Además de `USERNAME`, hay tres placeholders secundarios que debes reemplazar:

| Placeholder | Descripción | Ejemplo |
|-------------|-------------|---------|
| `YOUR_NAME` | Tu nombre completo | `María García` |
| `YOUR_EMAIL` | Tu correo de contacto | `maria@ejemplo.com` |
| `YOUR_TAGLINE` | Tu frase o lema personal | `Building the future, one commit at a time` |

Búscalos en el `README.md` y reemplázalos con tu información.

---

## Paso 4: Banner de perfil

El `README.md` referencia un banner en `assets/banner.png`.

**Opción A — Crear tu propio banner**:
1. Diseña una imagen de **1200×300 píxeles** con tu nombre, logo o frase.
2. Herramientas recomendadas: Canva, Figma, Photoshop, o GIMP.
3. Guarda el archivo como `assets/banner.png` en tu repositorio.
4. Haz commit y push.

**Opción B — Usar la imagen por defecto**:
El template incluye un banner de relleno en `assets/banner.png`. Puedes mantenerlo mientras diseñas el tuyo.

**Opción C — No usar banner**:
Si no quieres banner, simplemente elimina la línea:
```html
<img src="assets/banner.png" alt="..." width="100%"/>
```
O reemplázala por tu propio contenido.

> 💡 **Tip**: Si el archivo `assets/banner.png` no existe, GitHub muestra el texto `alt` en su lugar, no un ícono roto.

---

## Paso 5: Texto del typing SVG

El typing SVG es la animación que escribe texto línea por línea. Para personalizarlo:

1. Busca la línea que contiene `readme-typing-svg.demolab.com` en tu `README.md`.
2. Localiza el parámetro `lines=` en la URL.
3. Cada línea está separada por `;` y los espacios se representan como `+`.
4. Cambia el texto por tus propias frases.

**Ejemplo**:
```
lines=Full-Stack+Developer+%F0%9F%9A%80;Open+Source+Enthusiast+%F0%9F%92%A1
```

Para codificar tus líneas:
- Usa `+` en lugar de espacios.
- Usa `%F0%9F%9A%80` para emojis (puedes buscar "emoji URL encoder" en Google).
- Separa cada línea con `;`.

También puedes cambiar el `font`, `size`, `duration`, y `color` (formato hexadecimal con opacidad: `6BE68EA0` = color + alpha).

---

## Paso 6: Enlaces a redes sociales

Encuentra la sección `## 🌎 Find Me`. Cada badge tiene este formato:

```html
<a href="https://linkedin.com/in/USERNAME" target="_blank" rel="noopener noreferrer">
  <img src="https://img.shields.io/badge/LinkedIn-%230A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn">
</a>
```

Para personalizar:
1. Cambia `href` por la URL de tu perfil.
2. Cambia el texto después de `/badge/` para personalizar la etiqueta.
3. Cambia el color hex (`%230A66C2`).
4. Cambia `logo=` por el slug del ícono desde [simpleicons.org](https://simpleicons.org).

**Para agregar más redes**, copia todo el bloque `<a>...</a>` y modifícalo. Ejemplos de plataformas comunes:

- **X/Twitter**: `logo=x` (color `%23000000`)
- **YouTube**: `logo=youtube` (color `%23ED0000`)
- **Dev.to**: `logo=devdotto` (color `%230A0A0A`)
- **Medium**: `logo=medium` (color `%2312100E`)
- **Twitch**: `logo=twitch` (color `%239146FF`)
- **Stack Overflow**: `logo=stackoverflow` (color `%23F58025`)
- **Codeforces**: `logo=codeforces` (color `%23456392`)

---

## Paso 7: Sección de proyectos

El template incluye **dos secciones de ejemplo**: `Featured Projects` y `Developer Tools`, cada una con 4 tarjetas (2 filas × 2 columnas).

### Para reemplazar un proyecto existente:
1. Localiza un bloque como este:
   ```html
   <a href="https://github.com/USERNAME/example-repo-1">
     <img src="https://github-readme-stats.vercel.app/api/pin/?username=USERNAME&repo=example-repo-1&theme=tokyonight" alt="Example Repo 1" />
   </a>
   ```
2. Cambia `example-repo-1` por el nombre real de tu repositorio.
3. Actualiza el texto `alt`.
4. Si reemplazaste globalmente `USERNAME`, esta URL también se actualizó.

### Para agregar más filas:
1. Copia este bloque dentro del `<table>`:
   ```html
   <tr>
     <td align="center">
       <a href="https://github.com/USERNAME/tu-repo">
         <img src="https://github-readme-stats.vercel.app/api/pin/?username=USERNAME&repo=tu-repo&theme=tokyonight" alt="Tu Repo" />
       </a>
     </td>
     <td align="center">
       <a href="https://github.com/USERNAME/otro-repo">
         <img src="https://github-readme-stats.vercel.app/api/pin/?username=USERNAME&repo=otro-repo&theme=tokyonight" alt="Otro Repo" />
       </a>
     </td>
   </tr>
   ```
2. Pega el bloque antes de `</table>`.
3. Reemplaza los nombres de repositorio.

### Para agregar una sección completamente nueva:
1. Busca el comentario `<!-- PROJECTS: Developer Tools -->`.
2. Copia todo desde `## ...` hasta `</table>`.
3. Pégalo antes de la sección `## 📈 Profile Views`.
4. Cambia el título, la nota, y las tarjetas.

---

## Paso 8: Push y verificación

1. **Haz commit de tus cambios**:
   ```bash
   git add .
   git commit -m "Personalizar perfil con mis datos"
   git push origin main
   ```

2. **Revisa tu perfil**: Ve a `https://github.com/{tu-usuario}` y verifica que todo se vea bien.

3. **Verifica los workflows**: Ve a la pestaña Actions — los workflows deberían comenzar a ejecutarse automáticamente.

> ⏱️ Los cambios en el README son inmediatos.

---

## Automatizaciones Opcionales

Estos pasos activan contenido dinámico como la animación de la serpiente y el feed de actividad. Configúralos después de tener tu perfil en línea.

## Paso 9: Configurar permisos de Actions

Los workflows necesitan permisos de **lectura y escritura** para actualizar el contenido de tu perfil.

1. Ve a **Settings → Actions → General** de tu repositorio.
2. Desplázate hasta **Workflow permissions**.
3. Selecciona **"Read and write permissions"**.
4. Haz clic en **Save**.

> ✅ Una vez configurado, los tres workflows usan el `GITHUB_TOKEN` incorporado — no necesitas crear ningún token manualmente.

---

## Paso 10: Detalles de los workflows

El template incluye tres workflows de GitHub Actions preconfigurados.

### `update-activity.yml` — Actividad reciente
- Actualiza automáticamente la sección `Recent Activity` de tu README.
- Se ejecuta cada 60 minutos y manualmente desde la interfaz de Actions.
- Usa `GITHUB_TOKEN` — no requiere configuración adicional.

### `generate-snake.yml` — Animación de serpiente
- Genera un SVG con tu cuadrícula de contribuciones.
- Se ejecuta cada 60 minutos, al hacer push a `main`, o manualmente.
- Usa `GITHUB_TOKEN` — no requiere configuración adicional.
- La imagen se renderiza automáticamente en el footer del README.

### `check-icons.yml` — Validación de íconos
- Verifica que todas las URLs de imágenes externas en tu README sean accesibles.
- Se ejecuta al hacer push o PR contra `main`, o manualmente.
- Si algún ícono está roto, el workflow falla y te muestra cuál es.

Todos usan `GITHUB_TOKEN` — no requieren configuración manual de tokens.

---

## Paso 11: Ejecutar workflows por primera vez

Los workflows se activan automáticamente al hacer push, pero puedes ejecutarlos de inmediato:

1. Ve a la pestaña **Actions** de tu repositorio.
2. Selecciona un workflow (por ejemplo, `Generate snake animation`).
3. Haz clic en **"Run workflow"** → **"Run workflow"**.
4. Repite para cada workflow que quieras probar.

La animación de la serpiente aparece después de ~1 minuto. El feed de actividad se llena en la próxima ejecución programada (hasta 60 min) o al ejecutarlo manualmente.

---

## Solución de problemas

### El README no aparece en mi perfil
- **Causa**: El repositorio no está nombrado exactamente como tu usuario.
- **Solución**: Ve a Settings → Repository name y cámbialo para que coincida con tu nombre de usuario de GitHub.

### La animación de la serpiente no se muestra
- **Causa 1**: El workflow `generate-snake.yml` aún no se ha ejecutado.
- **Solución**: Ve a Actions → Generate snake animation → "Run workflow" → "Run workflow".
- **Causa 2**: La rama `output` no existe.
- **Solución**: El workflow la crea automáticamente en su primera ejecución. Ejecútalo manualmente.

### Las tarjetas de estadísticas muestran "Something went wrong"
- **Causa**: `USERNAME` no fue reemplazado correctamente.
- **Solución**: Busca `USERNAME` en tu README. Si queda algún marcador sin reemplazar, cámbialo por tu usuario.

### El contador de visitas no funciona
- **Causa**: El contador de visitas usa un widget externo (`komarev.com`) que puede no estar disponible temporalmente.
- **Solución**: Verifica que `USERNAME` fue reemplazado en la URL. El contador es opcional — puedes eliminar la sección `## 📈 Profile Views` si no lo necesitas. Si quieres partir de un número existente, agrega `&base=N` a la URL (ejemplo: `&base=100`).

### El workflow falla con error de permisos
- **Causa**: `GITHUB_TOKEN` no tiene los permisos necesarios.
- **Solución**: Ve a Settings → Actions → General → "Workflow permissions" y selecciona "Read and write permissions".

### "check-icons.yml" falla
- **Causa**: Alguna URL de imagen externa ya no está disponible.
- **Solución**: Abre el log del workflow para ver qué URL falló y actualízala por una alternativa.

---

## Preguntas frecuentes

### ¿Puedo cambiar el tema (tokyonight)?
Sí. En las URLs de `github-readme-stats`, cambia `theme=tokyonight` por otro tema. Los temas disponibles incluyen: `dark`, `radical`, `merko`, `gruvbox`, `onedark`, `dracula`, etc. [Lista completa de temas](https://github.com/anuraghazra/github-readme-stats/blob/master/themes/README.md).

### ¿Puedo eliminar secciones que no me interesan?
Sí. Simplemente borra las secciones que no quieras del README.md. El template está diseñado para ser modular.

### ¿Puedo agregar más tecnologías a la tabla?
Sí. Copia el patrón de un ícono existente y cambia el nombre del ícono en simpleicons.org. Asegúrate de mantener el formato: `https://cdn.simpleicons.org/ICONO/white`.

### ¿El template funciona con GitHub Enterprise?
Sí, pero los workflows pueden requerir ajustes menores (como cambiar `GITHUB_TOKEN` por un PAT si tu instancia no soporta `GITHUB_TOKEN` con permisos de escritura).

### ¿Necesito conocimientos de HTML?
Mínimos. La mayoría de las personalizaciones son reemplazar texto. Para cambios avanzados (agregar secciones, cambiar el diseño), se recomienda conocimiento básico de HTML y Markdown.

### ¿Puedo dar crédito de otra forma?
Si modificas significativamente el template, puedes cambiar el texto de atribución a "Inspired by EduardoProfe666's profile" o eliminarlo si lo prefieres. Agradecemos mantener la atribución original.

---

## 📚 Referencias

- [github-readme-stats](https://github.com/anuraghazra/github-readme-stats) — Tarjetas de estadísticas
- [github-profile-trophy](https://github.com/ryo-ma/github-profile-trophy) — Trofeos de perfil (widget externo opcional; puede no estar disponible o requerir auto-hosting)
- [github-profile-summary-cards](https://github.com/vn7n24fzkq/github-profile-summary-cards) — Tarjetas de resumen
- [readme-typing-svg](https://github.com/DenverCoder1/readme-typing-svg) — Animación de escritura
- [simple-icons](https://simpleicons.org) — Íconos de tecnologías
- [shields.io](https://shields.io) — Badges para enlaces
- [capsule-render](https://github.com/kyechan99/capsule-render) — Wave footer
- [platane/snk](https://github.com/platane/snk) — Generador de snake animation
- [github-activity-readme](https://github.com/jamesgeorge007/github-activity-readme) — Actividad reciente

---

## Licencia

Esta plantilla se distribuye bajo la [Licencia MIT](../LICENSE). Consulta el archivo `LICENSE` para los términos completos.

---

<sub>¿Encontraste un error o tienes una sugerencia? Abre un issue en el repositorio del template.</sub>
