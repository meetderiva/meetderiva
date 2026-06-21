# Customization Guide — GitHub Profile Template

> **Language note**: English is the template's default language. [Spanish guide](CUSTOMIZE.md) is a parallel translation covering the same steps. See [`README.md`](../README.md) for the quick-start checklist.

This guide walks you through customizing your copy of the GitHub profile template.

---

## Prerequisites

- A [GitHub](https://github.com) account
- Git installed locally (optional — the web editor works too)
- A repository named **exactly** after your GitHub username

---

## Required Setup

These steps are required to get your profile working on GitHub.

## Step 1: Use this template (recommended)

The simplest way to get started:

1. Click **Use this template** → **Create a new repository** at the top of the template page.
2. Name the repository **exactly after your GitHub username**.
3. Select **Public**.
4. Click **Create repository from template**.

> ⚠️ The repo name MUST be identical to your GitHub username. Otherwise your README won't show on your profile.

> 👤 **For maintainers**: The repository owner must enable **Template repository** in Settings → General → Template repository for the `Use this template` button to appear.

### Advanced: Fork instead

If you plan to track upstream updates and merge changes later, **Fork** the repository instead of using the template. Note that forked repositories don't appear under your profile automatically — use this path only if you're comfortable with Git merge workflows.

After forking, rename it to match your GitHub username (Settings → Repository name) and check "Copy the main branch only".

---

## Step 2: Replace USERNAME

`USERNAME` is the primary placeholder throughout the template. It appears in:

- GitHub stats URLs
- Repository links in the projects section
- Profile view counter (optional third-party widget — remove the section if not needed)
- Snake animation
- Footer wave capsule

**Recommended**: global find-and-replace.

- **GitHub web**: Open `README.md` → ✏️ edit → `Ctrl+F` / `Cmd+F` → search `USERNAME` → replace with your GitHub username.
- **Local**: `sed -i 's/USERNAME/your-username/g' README.md`

> ✅ After replacement, verify no `USERNAME` remains in visible content.

---

## Step 3: Customize additional placeholders

Three secondary placeholders in `README.md`:

| Placeholder   | Description        | Example                              |
|---------------|--------------------|--------------------------------------|
| `YOUR_NAME`   | Your full name     | `Jane Doe`                           |
| `YOUR_EMAIL`  | Your contact email | `jane@example.com`                   |
| `YOUR_TAGLINE`| A short motto      | `Building things that matter`         |

Replace each with your own information.

---

## Step 4: Profile banner

`README.md` references `assets/banner.png` (1200×300px recommended).

| Option | Action |
|--------|--------|
| **Create your own** | Design a 1200×300 image in Canva, Figma, or GIMP → save as `assets/banner.png` |
| **Keep default** | The template ships with a placeholder banner |
| **Remove banner** | Delete the `<img src="assets/banner.png" ...>` line |

> 💡 If `assets/banner.png` doesn't exist, GitHub shows the `alt` text — not a broken icon.

---

## Step 5: Typing SVG text

Find the `readme-typing-svg.demolab.com` URL in your `README.md`. The `lines=` parameter controls the animation text.

- Use `+` instead of spaces
- Separate lines with `;`
- Emojis need URL-encoding (e.g., `%F0%9F%9A%80`)

**Example**: `lines=Full-Stack+Developer+%F0%9F%9A%80;Open+Source+Enthusiast+%F0%9F%92%A1`

You can also change `font`, `size`, `duration`, and `color`.

---

## Step 6: Social media links

In the `## 🌎 Find Me` section, each badge follows this pattern:

```html
<a href="https://linkedin.com/in/USERNAME" target="_blank" rel="noopener noreferrer">
  <img src="https://img.shields.io/badge/LinkedIn-%230A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn">
</a>
```

To customize:

1. Change `href` to your profile URL
2. Adjust badge label and color (hex after `%23`)
3. Set `logo=` to the icon slug from [simpleicons.org](https://simpleicons.org)
4. **Always** keep `rel="noopener noreferrer"` on external links with `target="_blank"`

Common platforms: `x`, `youtube`, `discord`, `devdotto`, `medium`, `twitch`, `stackoverflow`.

---

## Step 7: Projects section

The template includes two example sections (`Featured Projects` and `Developer Tools`), each with 4 cards.

**Replace a project**: Find an `<a href="https://github.com/USERNAME/example-repo-1">` block and change the repo name.

**Add a row**: Copy a `<tr>` block with two `<td>` cells inside `<table>` and update the repo names.

**Add a new section**: Copy from `## ...` to `</table>`, paste before `## 📈 Profile Views`, then customize.

> ℹ️ If you already did the global `USERNAME` replacement, the URLs are updated automatically.

---

## Step 8: Push and verify

```bash
git add .
git commit -m "Customize profile with my info"
git push origin main
```

After pushing:

1. Visit `https://github.com/your-username` — README renders immediately
2. Check the **Actions** tab — workflows begin running

> ⏱️ README changes are instant.

---

## Optional Automations

These steps enable dynamic content like the snake animation and activity feed. Configure them after your profile is live.

## Step 9: Configure Actions permissions

Workflows need **read and write** permissions to update your profile content.

1. Go to your repository **Settings → Actions → General**
2. Scroll to **Workflow permissions**
3. Select **"Read and write permissions"**
4. Click **Save**

> ✅ Once set, all three workflows use the built-in `GITHUB_TOKEN` — no manual token setup needed.

---

## Step 10: Workflow details

Three preconfigured GitHub Actions workflows activate on push to `main`.

| Workflow | Purpose | Trigger |
|----------|---------|---------|
| `update-activity.yml` | Populates the Recent Activity section | Every hour |
| `generate-snake.yml` | Generates contribution snake SVG | Every hour + on push |
| `check-icons.yml` | Validates external image URLs | On push/PR to `main` |

All use `GITHUB_TOKEN` — no manual token setup needed.

---

## Step 11: Run workflows for the first time

Workflows run automatically on push, but you can trigger them immediately:

1. Go to your repository's **Actions** tab
2. Select a workflow (e.g., `Generate snake animation`)
3. Click **"Run workflow"** → **"Run workflow"**
4. Repeat for each workflow you want to test

Snake SVG appears after ~1 minute. Activity feed populates on the next scheduled run (up to 60 min) or on manual trigger.

---

## Troubleshooting

| Symptom | Likely cause | Fix |
|---------|-------------|-----|
| README not showing on profile | Repo name != username | Rename repo to match your username |
| Stats show "Something went wrong" | `USERNAME` not replaced | Search for `USERNAME` and replace any remaining |
| Snake animation missing | Workflow hasn't run yet | Go to Actions → run `generate-snake.yml` manually |
| Profile counter not showing | Optional widget (komarev.com) unavailable | Remove the `## 📈 Profile Views` section if not needed. To start from an existing count, append `&base=N` to the URL |
| Workflow fails with permission error | Actions permissions not set to read/write | Go to Settings → Actions → General → set "Read and write permissions" |
| Icon check workflow fails | External URL is dead | Check workflow log for the failing URL |

---

## FAQ

**Can I change the theme?** Yes — replace `theme=tokyonight` in stats URLs. Options: `dark`, `radical`, `gruvbox`, `onedark`, `dracula`.

**Can I remove sections?** Yes — delete any section from `README.md`. The template is modular.

**Do I need HTML knowledge?** Minimal. Most changes are text replacements. Advanced customization benefits from basic HTML.

---

## License

This template is distributed under the [MIT License](../LICENSE). See the `LICENSE` file for full terms.

---

*Found an issue or have a suggestion? Open an issue in the template repository.*
