#!/usr/bin/env python3

import json
from pathlib import Path

OUT = Path(__file__).parent / "themes"

# --- Palette per variante (superfici + testo + accento) ---------------------
VARIANTS = {
    "ceres-ocean": dict(
        label="Ceres -- Ocean",
        bg0="#0b0d14", bg1="#0f111a", bg2="#131622", bg3="#1a1e2f", bg4="#262b46",
        line="#1b1f2e", fg="#b4bad6", mute="#7a81a6", dim="#5a618a",
        accent="#8ab4ff",
    ),
    "ceres-mirage": dict(
        label="Ceres -- Mirage",
        bg0="#181a28", bg1="#212536", bg2="#1c1f2f", bg3="#2a2e45", bg4="#383d5c",
        line="#2b3047", fg="#c2c8e4", mute="#8c94ba", dim="#6a7299",
        accent="#9fb4ff",
    ),
    "ceres-slate": dict(
        label="Ceres -- Slate",
        bg0="#14181b", bg1="#1e2327", bg2="#1a1e21", bg3="#272e33", bg4="#34404a",
        line="#2a3237", fg="#bfcbcf", mute="#7d8f96", dim="#62727a",
        accent="#8fd9b0",
    ),
    # Ispirata a EliverLara/Squared: grigio-blu desaturato, bordi netti, struttura a griglia
    "ceres-squared": dict(
        label="Ceres -- Squared",
        bg0="#1d2027", bg1="#252932", bg2="#20242b", bg3="#2e333d", bg4="#3c424e",
        line="#3a404b", fg="#c5cad4", mute="#8f9aaa", dim="#6e7889",
        accent="#e3b077",
        squared=True,
    ),
}

# --- Colori sintassi condivisi (ispirati al gradiente del logo: menta -> giallo -> corallo)
SYN = dict(
    coral="#f58f86",    # keyword, tag
    mint="#a8e6c0",     # stringhe
    yellow="#ffd88a",   # numeri, costanti, attributi
    blue="#8ab4ff",     # funzioni
    teal="#7fdbe0",     # tipi, classi, regex
    lavender="#b9a7ff", # proprieta', decoratori
    peach="#ffae8a",    # parametri, this/self
    pink="#f2a0c8",     # escape, speciali
    punct="#8a92b8",    # operatori e punteggiatura
)

# Pallino semaforo delle finestre nello screenshot
TRAFFIC = dict(red="#e8707a", yellow="#e5b95c", green="#62c07a")


def a(color, alpha):
    """Aggiunge un canale alpha (0-255) a un colore #rrggbb."""
    return f"{color}{alpha:02x}"


def _workbench(p):
    acc = p["accent"]
    return {
        # base
        "focusBorder": a(acc, 0x66),
        "foreground": p["fg"],
        "descriptionForeground": p["mute"],
        "errorForeground": TRAFFIC["red"],
        "icon.foreground": p["mute"],
        "widget.shadow": a("#000000", 0x55),
        "selection.background": a(acc, 0x55),
        "textLink.foreground": acc,
        "textLink.activeForeground": SYN["teal"],
        "textCodeBlock.background": p["bg0"],
        "textBlockQuote.background": p["bg0"],
        "textBlockQuote.border": p["bg4"],
        "textSeparator.foreground": p["line"],
        "sash.hoverBorder": acc,
        # bottoni e input
        "button.background": acc,
        "button.foreground": p["bg0"],
        "button.hoverBackground": SYN["teal"],
        "button.secondaryBackground": p["bg3"],
        "button.secondaryForeground": p["fg"],
        "button.secondaryHoverBackground": p["bg4"],
        "input.background": p["bg0"],
        "input.foreground": p["fg"],
        "input.border": p["line"],
        "input.placeholderForeground": p["dim"],
        "inputOption.activeBorder": acc,
        "inputOption.activeBackground": a(acc, 0x33),
        "inputValidation.errorBackground": a(TRAFFIC["red"], 0x22),
        "inputValidation.errorBorder": TRAFFIC["red"],
        "inputValidation.warningBackground": a(TRAFFIC["yellow"], 0x22),
        "inputValidation.warningBorder": TRAFFIC["yellow"],
        "inputValidation.infoBackground": a(acc, 0x22),
        "inputValidation.infoBorder": acc,
        "dropdown.background": p["bg0"],
        "dropdown.foreground": p["fg"],
        "dropdown.border": p["line"],
        "checkbox.background": p["bg0"],
        "checkbox.border": p["bg4"],
        "badge.background": acc,
        "badge.foreground": p["bg0"],
        "progressBar.background": acc,
        "scrollbar.shadow": "#00000000",
        "scrollbarSlider.background": a(p["bg4"], 0x66),
        "scrollbarSlider.hoverBackground": a(p["bg4"], 0xaa),
        "scrollbarSlider.activeBackground": a(p["mute"], 0x66),
        # liste e alberi (sidebar, quick pick, ecc.)
        "list.activeSelectionBackground": p["bg3"],
        "list.activeSelectionForeground": p["fg"],
        "list.inactiveSelectionBackground": p["bg3"],
        "list.inactiveSelectionForeground": p["fg"],
        "list.hoverBackground": a(p["bg3"], 0xaa),
        "list.hoverForeground": p["fg"],
        "list.focusBackground": p["bg3"],
        "list.focusOutline": "#00000000",
        "list.highlightForeground": acc,
        "list.errorForeground": TRAFFIC["red"],
        "list.warningForeground": TRAFFIC["yellow"],
        "list.dropBackground": a(acc, 0x22),
        "tree.indentGuidesStroke": p["bg4"],
        # barra del titolo
        "titleBar.activeBackground": p["bg0"],
        "titleBar.activeForeground": p["mute"],
        "titleBar.inactiveBackground": p["bg0"],
        "titleBar.inactiveForeground": p["dim"],
        "titleBar.border": p["bg0"],
        # menu
        "menubar.selectionBackground": p["bg3"],
        "menubar.selectionForeground": p["fg"],
        "menu.background": p["bg2"],
        "menu.foreground": p["fg"],
        "menu.selectionBackground": p["bg3"],
        "menu.selectionForeground": p["fg"],
        "menu.separatorBackground": p["line"],
        # activity bar: icone monocromatiche, indicatore a pillola
        "activityBar.background": p["bg0"],
        "activityBar.foreground": p["fg"],
        "activityBar.inactiveForeground": p["dim"],
        "activityBar.border": p["bg0"],
        "activityBar.activeBorder": acc,
        "activityBar.activeBackground": a(p["bg3"], 0x99),
        "activityBarBadge.background": acc,
        "activityBarBadge.foreground": p["bg0"],
        # sidebar
        "sideBar.background": p["bg2"],
        "sideBar.foreground": p["mute"],
        "sideBar.border": p["bg2"],
        "sideBarTitle.foreground": p["fg"],
        "sideBarSectionHeader.background": p["bg2"],
        "sideBarSectionHeader.foreground": p["mute"],
        "sideBarSectionHeader.border": p["line"],
        # tab
        "editorGroupHeader.tabsBackground": p["bg0"],
        "editorGroupHeader.noTabsBackground": p["bg1"],
        "editorGroupHeader.tabsBorder": p["bg0"],
        "editorGroup.border": p["bg0"],
        "editorGroup.dropBackground": a(acc, 0x22),
        "tab.activeBackground": p["bg1"],
        "tab.activeForeground": p["fg"],
        "tab.activeBorderTop": acc,
        "tab.inactiveBackground": p["bg0"],
        "tab.inactiveForeground": p["mute"],
        "tab.hoverBackground": p["bg2"],
        "tab.unfocusedActiveBackground": p["bg1"],
        "tab.unfocusedActiveForeground": p["mute"],
        "tab.unfocusedInactiveBackground": p["bg0"],
        "tab.border": p["bg0"],
        "tab.lastPinnedBorder": p["bg4"],
        # editor
        "editor.background": p["bg1"],
        "editor.foreground": p["fg"],
        "editorLineNumber.foreground": p["dim"],
        "editorLineNumber.activeForeground": p["fg"],
        "editorCursor.foreground": acc,
        "editor.selectionBackground": a(acc, 0x33),
        "editor.inactiveSelectionBackground": a(acc, 0x1a),
        "editor.selectionHighlightBackground": a(acc, 0x1f),
        "editor.wordHighlightBackground": a(acc, 0x1f),
        "editor.wordHighlightStrongBackground": a(SYN["lavender"], 0x2a),
        "editor.findMatchBackground": a(TRAFFIC["yellow"], 0x55),
        "editor.findMatchHighlightBackground": a(TRAFFIC["yellow"], 0x26),
        "editor.findRangeHighlightBackground": a(p["bg4"], 0x66),
        "editor.hoverHighlightBackground": a(acc, 0x1f),
        "editor.lineHighlightBackground": a(p["bg3"], 0x77),
        "editor.lineHighlightBorder": "#00000000",
        "editor.rangeHighlightBackground": a(p["bg3"], 0x77),
        "editor.foldBackground": a(p["bg3"], 0x66),
        "editorWhitespace.foreground": a(p["dim"], 0x66),
        "editorIndentGuide.background1": a(p["bg4"], 0x77),
        "editorIndentGuide.activeBackground1": p["dim"],
        "editorRuler.foreground": p["line"],
        "editorLink.activeForeground": acc,
        "editorCodeLens.foreground": p["dim"],
        "editorInlayHint.foreground": p["mute"],
        "editorInlayHint.background": a(p["bg3"], 0xaa),
        "editorGutter.background": p["bg1"],
        "editorGutter.modifiedBackground": TRAFFIC["yellow"],
        "editorGutter.addedBackground": TRAFFIC["green"],
        "editorGutter.deletedBackground": TRAFFIC["red"],
        "editorOverviewRuler.border": "#00000000",
        "editorOverviewRuler.errorForeground": TRAFFIC["red"],
        "editorOverviewRuler.warningForeground": TRAFFIC["yellow"],
        "editorOverviewRuler.infoForeground": acc,
        # bracket colorizer: gradiente del logo
        "editorBracketHighlight.foreground1": TRAFFIC["yellow"],
        "editorBracketHighlight.foreground2": SYN["coral"],
        "editorBracketHighlight.foreground3": SYN["mint"],
        "editorBracketHighlight.foreground4": SYN["blue"],
        "editorBracketHighlight.foreground5": SYN["lavender"],
        "editorBracketHighlight.foreground6": SYN["teal"],
        "editorBracketHighlight.unexpectedBracket.foreground": TRAFFIC["red"],
        "editorBracketMatch.background": a(acc, 0x2a),
        "editorBracketMatch.border": a(acc, 0x88),
        # errori e warning
        "editorError.foreground": TRAFFIC["red"],
        "editorWarning.foreground": TRAFFIC["yellow"],
        "editorInfo.foreground": acc,
        "editorHint.foreground": SYN["mint"],
        # widget (suggerimenti, find, hover)
        "editorWidget.background": p["bg2"],
        "editorWidget.border": p["line"],
        "editorSuggestWidget.background": p["bg2"],
        "editorSuggestWidget.border": p["line"],
        "editorSuggestWidget.selectedBackground": p["bg3"],
        "editorSuggestWidget.highlightForeground": acc,
        "editorHoverWidget.background": p["bg2"],
        "editorHoverWidget.border": p["line"],
        "peekView.border": acc,
        "peekViewEditor.background": p["bg2"],
        "peekViewResult.background": p["bg0"],
        "peekViewTitle.background": p["bg0"],
        "peekViewTitleLabel.foreground": p["fg"],
        "peekViewResult.selectionBackground": p["bg3"],
        "peekViewEditor.matchHighlightBackground": a(TRAFFIC["yellow"], 0x44),
        # diff
        "diffEditor.insertedTextBackground": a(TRAFFIC["green"], 0x1f),
        "diffEditor.removedTextBackground": a(TRAFFIC["red"], 0x22),
        "diffEditor.insertedLineBackground": a(TRAFFIC["green"], 0x14),
        "diffEditor.removedLineBackground": a(TRAFFIC["red"], 0x16),
        # breadcrumb
        "breadcrumb.foreground": p["dim"],
        "breadcrumb.focusForeground": p["fg"],
        "breadcrumb.activeSelectionForeground": acc,
        "breadcrumbPicker.background": p["bg2"],
        # pannello e terminale
        "panel.background": p["bg1"],
        "panel.border": p["line"],
        "panelTitle.activeForeground": p["fg"],
        "panelTitle.inactiveForeground": p["mute"],
        "panelTitle.activeBorder": acc,
        "panelSectionHeader.background": p["bg2"],
        "terminal.background": p["bg1"],
        "terminal.foreground": p["fg"],
        "terminal.selectionBackground": a(acc, 0x33),
        "terminalCursor.foreground": acc,
        "terminal.ansiBlack": p["bg4"],
        "terminal.ansiRed": TRAFFIC["red"],
        "terminal.ansiGreen": TRAFFIC["green"],
        "terminal.ansiYellow": TRAFFIC["yellow"],
        "terminal.ansiBlue": SYN["blue"],
        "terminal.ansiMagenta": SYN["lavender"],
        "terminal.ansiCyan": SYN["teal"],
        "terminal.ansiWhite": p["fg"],
        "terminal.ansiBrightBlack": p["dim"],
        "terminal.ansiBrightRed": SYN["coral"],
        "terminal.ansiBrightGreen": SYN["mint"],
        "terminal.ansiBrightYellow": SYN["yellow"],
        "terminal.ansiBrightBlue": "#a9c8ff",
        "terminal.ansiBrightMagenta": SYN["pink"],
        "terminal.ansiBrightCyan": "#a5ecef",
        "terminal.ansiBrightWhite": "#e6e9f5",
        # barra di stato: si fonde con la barra del titolo
        "statusBar.background": p["bg0"],
        "statusBar.foreground": p["mute"],
        "statusBar.border": p["bg0"],
        "statusBar.noFolderBackground": p["bg0"],
        "statusBar.debuggingBackground": TRAFFIC["red"],
        "statusBar.debuggingForeground": p["bg0"],
        "statusBarItem.hoverBackground": p["bg3"],
        "statusBarItem.remoteBackground": acc,
        "statusBarItem.remoteForeground": p["bg0"],
        "statusBarItem.prominentBackground": p["bg3"],
        # notifiche e quick input
        "notifications.background": p["bg2"],
        "notifications.foreground": p["fg"],
        "notifications.border": p["line"],
        "notificationCenterHeader.background": p["bg0"],
        "notificationLink.foreground": acc,
        "quickInput.background": p["bg2"],
        "quickInput.foreground": p["fg"],
        "quickInputList.focusBackground": p["bg3"],
        "quickInputTitle.background": p["bg0"],
        "pickerGroup.foreground": acc,
        "pickerGroup.border": p["line"],
        # git
        "gitDecoration.modifiedResourceForeground": TRAFFIC["yellow"],
        "gitDecoration.addedResourceForeground": TRAFFIC["green"],
        "gitDecoration.untrackedResourceForeground": SYN["mint"],
        "gitDecoration.deletedResourceForeground": TRAFFIC["red"],
        "gitDecoration.ignoredResourceForeground": p["dim"],
        "gitDecoration.conflictingResourceForeground": SYN["peach"],
        # minimap
        "minimap.background": p["bg1"],
        "minimap.selectionHighlight": a(acc, 0x66),
        "minimap.findMatchHighlight": a(TRAFFIC["yellow"], 0x88),
        "minimapSlider.background": a(p["bg4"], 0x44),
        "minimapSlider.hoverBackground": a(p["bg4"], 0x66),
        "minimapSlider.activeBackground": a(p["bg4"], 0x88),
        # debug
        "debugToolBar.background": p["bg2"],
        "debugIcon.breakpointForeground": TRAFFIC["red"],
        "editor.stackFrameHighlightBackground": a(TRAFFIC["yellow"], 0x22),
        "editor.focusedStackFrameHighlightBackground": a(TRAFFIC["green"], 0x22),
    }


def workbench(p):
    c = _workbench(p)
    if p.get("squared"):
        ln = p["line"]
        # griglia: ogni area e' separata da un filo di 1px, niente fusione tra le barre
        c.update({
            "titleBar.border": ln, "activityBar.border": ln, "sideBar.border": ln,
            "statusBar.border": ln, "panel.border": ln, "editorGroup.border": ln,
            "editorGroupHeader.tabsBorder": ln, "tab.border": ln,
            "tab.activeBorder": p["bg1"], "tab.activeBorderTop": p["accent"],
            "tab.unfocusedActiveBorderTop": p["dim"],
            "sideBarSectionHeader.border": ln, "menu.border": ln,
            "list.focusOutline": a(p["accent"], 0x66),
            "list.activeSelectionBackground": p["bg4"],
            "list.inactiveSelectionBackground": p["bg3"],
            "input.border": p["bg4"], "dropdown.border": p["bg4"],
            "button.border": p["bg4"], "quickInput.border": ln,
            "activityBar.activeBackground": "#00000000",
            "editorWidget.border": p["bg4"], "editorSuggestWidget.border": p["bg4"],
            "editorHoverWidget.border": p["bg4"], "notifications.border": p["bg4"],
            "widget.shadow": "#00000000",
            "editor.lineHighlightBorder": a(p["bg4"], 0x66),
            "editor.lineHighlightBackground": "#00000000",
            "editorGroupHeader.noTabsBackground": p["bg1"],
        })
    return c


def tokens():
    s = SYN
    rules = [
        ("Commenti", ["comment", "punctuation.definition.comment"], "mute_italic"),
        ("Stringhe", ["string", "string.quoted", "punctuation.definition.string"], s["mint"]),
        ("Escape e speciali", ["constant.character.escape", "string.regexp", "constant.other.placeholder"], s["pink"]),
        ("Numeri e costanti", ["constant.numeric", "constant.language", "constant.character", "support.constant"], s["yellow"]),
        ("Keyword", ["keyword", "keyword.control", "storage", "storage.type", "storage.modifier"], s["coral"]),
        ("Operatori", ["keyword.operator", "punctuation.separator", "punctuation.terminator"], s["punct"]),
        ("Punteggiatura", ["punctuation", "meta.brace"], s["punct"]),
        ("Funzioni", ["entity.name.function", "support.function", "meta.function-call"], s["blue"]),
        ("Tipi e classi", ["entity.name.type", "entity.name.class", "support.type", "support.class", "entity.other.inherited-class"], s["teal"]),
        ("Parametri", ["variable.parameter", "meta.parameter"], s["peach"]),
        ("this / self", ["variable.language"], "peach_italic"),
        ("Proprieta'", ["variable.other.property", "variable.other.object.property", "support.type.property-name", "meta.object-literal.key"], s["lavender"]),
        ("Decoratori e annotazioni", ["meta.decorator", "entity.name.function.decorator", "storage.type.annotation", "meta.annotation"], s["lavender"]),
        ("Tag HTML/JSX", ["entity.name.tag", "punctuation.definition.tag"], s["coral"]),
        ("Attributi", ["entity.other.attribute-name"], "yellow_italic"),
        ("CSS selettori classe/id", ["entity.other.attribute-name.class.css", "entity.other.attribute-name.id.css", "entity.name.tag.css"], s["yellow"]),
        ("CSS proprieta'", ["support.type.property-name.css", "meta.property-name.css"], s["lavender"]),
        ("CSS valori e unita'", ["keyword.other.unit", "support.constant.property-value.css", "constant.other.color"], s["teal"]),
        ("CSS variabili", ["variable.css", "variable.argument.css", "support.type.custom-property.name"], s["peach"]),
        ("JSON chiavi", ["support.type.property-name.json"], s["lavender"]),
        ("Markdown titoli", ["markup.heading", "entity.name.section"], "blue_bold"),
        ("Markdown grassetto", ["markup.bold"], "yellow_bold"),
        ("Markdown corsivo", ["markup.italic"], "coral_italic"),
        ("Markdown codice", ["markup.inline.raw", "markup.fenced_code"], s["mint"]),
        ("Markdown link", ["markup.underline.link", "string.other.link"], s["teal"]),
        ("Diff inserito", ["markup.inserted"], TRAFFIC["green"]),
        ("Diff rimosso", ["markup.deleted"], TRAFFIC["red"]),
        ("Diff modificato", ["markup.changed"], TRAFFIC["yellow"]),
        ("Invalid", ["invalid", "invalid.illegal"], TRAFFIC["red"]),
    ]
    return rules


def token_colors(p):
    out = []
    for name, scopes, spec in tokens():
        setting = {}
        if spec == "mute_italic":
            setting = {"foreground": p["mute"], "fontStyle": "italic"}
        elif spec.endswith("_italic") or spec.endswith("_bold"):
            col, style = spec.split("_")
            setting = {"foreground": {**SYN, **TRAFFIC}[col], "fontStyle": style}
        else:
            setting = {"foreground": spec}
        out.append({"name": name, "scope": scopes, "settings": setting})
    return out


def build(slug, p):
    theme = {
        "name": p["label"],
        "type": "dark",
        "semanticHighlighting": True,
        "colors": workbench(p),
        "tokenColors": token_colors(p),
        "semanticTokenColors": {
            "property": SYN["lavender"],
            "parameter": SYN["peach"],
            "enumMember": SYN["yellow"],
            "*.defaultLibrary": {"foreground": SYN["blue"]},
            "variable.defaultLibrary": SYN["peach"],
        },
    }
    (OUT / f"{slug}-color-theme.json").write_text(
        json.dumps(theme, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    for slug, pal in VARIANTS.items():
        build(slug, pal)
        print("scritto", slug)
