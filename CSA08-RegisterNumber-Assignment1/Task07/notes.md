# Task 7 - Notes
* `import milkrate` -> use `milkrate.payout()`; whole module namespace, no name clashes.
* `from milkrate import payout` -> `payout()` directly; shorter, but may shadow other names.
* `import milkrate as mr` -> alias `mr.payout()`; short and still namespaced.
* `if __name__ == "__main__":` is True only when the file is run directly. When imported,
  `__name__` is "milkrate", so the demonstration table is skipped. Without the guard the demo
  table would print every time any script imports the module (unwanted side effects).
* Standard modules: `math` (floor, ceil, isfinite), `decimal` (exact money arithmetic).
* Search order: the importing script's directory/current directory, PYTHONPATH, then the
  standard library and site-packages; the full list is `sys.path`.
* Module vs copy-paste: a module gives ONE place to revise rates (O(1) edits vs O(files));
  copies drift apart. Import cost is paid once: Python caches the module object in
  `sys.modules`, so later imports are a dictionary lookup, O(1).
