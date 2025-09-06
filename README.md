A simple and lightweight LaTeX style for creating high school physics course sheets.

---

## How to use it?

1. Put `physiquecours.sty` inside the `style/` folder.  
2. Organize your chapters inside their own folders (e.g., `chapitre0/`, `chapitre1/`, ...).  
3. In your `.tex` file, load the style with:

```latex
\usepackage{style/physiquecours}
````

4. Use `\startdocument{Physique}` (or `Chimie`, etc.) instead of `\begin{document}`.
5. Compile with `pdflatex` or your favorite LaTeX editor.

---

## Main commands

| Command                        | Description                          | Example                                                         |
| ------------------------------ | ------------------------------------ | --------------------------------------------------------------- |
| `\titre{Title}{Objective}`     | Creates a title with an objective    | `\titre{Chapter 1}{Understanding frames of reference}`          |
| `\definition{...}`             | Box for definitions                  | `\definition{A frame of reference is...}`                       |
| `\formule{...}`                | Box for important formulas           | `\formule{\[\vec{v} = \frac{d\vec{OM}}{dt}\]}`                  |
| `\remarque{...}`               | Box for remarks                      | `\remarque{Be careful with this...}`                            |
| `\attention{...}`              | Red warning box                      | `\attention{Do not confuse speed and acceleration!}`            |
| `\exemple{...}`                | Box for examples                     | `\exemple{An object moving in a straight line...}`              |
| `\illustration{file}{caption}` | Insert a centered image with caption | `\illustration{images/diagram.png}{Frame of reference example}` |
| `\unite{...}`                  | Write units (requires siunitx)       | `\unite{\meter\per\second}`                                     |

---

## Writing a simple course

Minimal `.tex` example:

```latex
\documentclass[12pt,a4paper]{article}
\usepackage{style/physiquecours}

\startdocument{Physique}

\titre{Chapter 0 – Introduction}{Basics and objectives}

\section*{What is Physics?}

Physics is the study of matter, energy, and their interactions.

\definition{
Physics is the natural science that studies matter, its motion, and behavior through space and time.
}

\formule{
\[
F = m \times a
\]
}

\illustration{images/physics_intro.png}{Force acting on an object}

\end{document}
```

---

## Recommended folder structure

```
MyCourse/
├── style/
│   └── physiquecours.sty
├── chapitre0/
│   ├── chapitre0.tex
│   └── images/
│       └── physics_intro.png
```

---

## Need help?

Feel free to ask for a full example project, a ready-to-compile setup, or a more detailed guide!

---

Happy writing!
