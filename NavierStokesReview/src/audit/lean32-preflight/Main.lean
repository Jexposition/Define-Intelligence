import Mathlib

example (x y : ℝ) (h : x = y) : y = x := by
  exact h.symm

#check ContDiffOn
#check MeasureTheory.IntegrableOn

