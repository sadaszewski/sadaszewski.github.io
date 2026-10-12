PEP 638 playground - CPython 3.14.2 with syntactic macros, built as Pyodide 314.0.7

Run:    python3 serve.py        then open http://localhost:8638/
        (any static web server works; the page cannot be opened from file://)

index.html        the playground (editable macro module + program, output,
                  expansion and parsed tree)
console.html      Pyodide's stock REPL on this build; needs internet access for
                  its terminal widget. Macros imported with from! stay available
                  on later lines.
pyodide.mjs, pyodide.asm.mjs, pyodide.asm.wasm, python_stdlib.zip,
pyodide-lock.json, micropip-*.whl   the Pyodide distribution itself; use it like
                  any Pyodide build:  loadPyodide({indexURL: "<this folder>/"})
