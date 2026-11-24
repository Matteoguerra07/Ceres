# Ceres per VS Code


Ceres: tema scuro ispirato ai temi GTK [Juno](https://github.com/EliverLara/Juno) e [Squared](https://github.com/EliverLara/Squared) di EliverLara. Quattro varianti, tre dalle finestre di Juno e una da Squared:

| Variante | Editor | Carattere |
|---|---|---|
| **Ceres -- Ocean** | `#0f111a` | blu notte profondo, il piu' scuro |
| **Ceres -- Mirage** | `#212536` | blu-viola piu' morbido e leggibile |
| **Ceres -- Slate** | `#1e2327` | grigio-verde, accento menta |
| **Ceres -- Squared** | `#252932` | ispirata a [Squared](https://github.com/EliverLara/Squared): grigio-blu desaturato, accento ambra, bordi netti |

## Scelte di design

- **Superfici piatte a gradini**: titlebar, activity bar e status bar condividono lo stesso colore (`bg0`), sidebar ed editor salgono di un gradino. Niente bordi pesanti, come nelle finestre GTK.
- **Accenti dal logo**: sintassi in menta, giallo e corallo, i colori del gradiente del logo Juno. Le parentesi colorate seguono lo stesso ordine.
- **Semaforo**: rosso, giallo e verde dei pallini delle finestre sono usati per git, errori e debug.
- **Squared**: Squared e' un tema GTK con angoli squadrati e palette riposante, ma non pubblica i colori. La variante ne traduce il carattere: fili da 1px tra ogni area (griglia), niente ombre, selezioni piene, toni desaturati. Colori e ambra d'accento sono una scelta di questo tema, non valori copiati.
- **Contrasto**: testo e token superano 4.5:1, i numeri di riga 3:1 (verificato con `check.py`).

## Sviluppo

```bash
python3 build.py   # rigenera themes/*.json dalle palette
python3 check.py   # valida i JSON e controlla i contrasti WCAG
npx @vscode/vsce package
```

Per cambiare un colore modifica `VARIANTS` o `SYN` in `build.py` e rigenera.

## Installazione locale

```bash
code --install-extension ceres-vscode-0.3.1.vsix
```

Poi `Ctrl+K Ctrl+T` e scegli una variante Ceres.
