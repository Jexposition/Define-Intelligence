import NavierStokes.R3.Theorem
import Euler.EulerSingularity
import Euler.Solution

open Lean Elab Command

namespace NavierStokesReview.Audit

private def projectName (name : Name) : Bool :=
  let text := name.toString
  text.startsWith "NavierStokes" ||
    text.startsWith "Euler" ||
    text.startsWith "ComparatorChallenges" ||
    text.startsWith "NavierStokesReview"

private def infoReferences (info : ConstantInfo) : Array Name :=
  let typeRefs := info.type.getUsedConstants
  match info.value? true with
  | some value => typeRefs ++ value.getUsedConstants
  | none => typeRefs

private def jsonNames (names : Array Name) : Json :=
  Json.arr (names.map (fun name => Json.str name.toString))

private def dedupNames (names : Array Name) : Array Name :=
  names.foldl (init := #[]) fun acc name =>
    if acc.contains name then acc else acc.push name

private def jsonNode (name : Name) (info : ConstantInfo) : Json :=
  let refs := infoReferences info
  Json.mkObj [
    ("name", Json.str name.toString),
    ("type", Json.str (toString info.type)),
    ("usesSorryAx", Json.bool (refs.any (· == ``sorryAx))),
    ("uses", jsonNames (refs.filter projectName))
  ]

elab "exportReviewEnvironmentClosure " output:str : command => do
  let output := output.getString
  let env ← getEnv
  let roots : Array Name := #[
    ``NavierStokesR3.theorem_1_1,
    ``NavierStokesR3.theorem_1_1_with_initial_rest,
    ``NavierStokesR3.theorem_1_1_with_dissipation,
    ``NavierStokes.ActualCandidateAssembly.selected_witness,
    ``NavierStokes.Comparator.navier_stokes_breakdown_R3,
    ``NavierStokes.Comparator.navier_stokes_breakdown_periodic,
    ``Euler.euler_breakdown_R3,
    ``Euler.exists_compact_smooth_euler_singularity,
    ``EulerPacketInduction.exists_compact_smooth_euler_singularity
  ]
  let mut queue : Array Name := roots
  let mut cursor := 0
  let mut seen : NameSet := {}
  let mut nodes : Array Json := #[]
  let mut edges : Array Json := #[]
  while cursor < queue.size do
    let current := queue[cursor]!
    cursor := cursor + 1
    if !seen.contains current then
      seen := seen.insert current
      match env.find? current with
      | none =>
          logWarning m!"Environment declaration not found: {current}"
      | some info =>
          let refs := dedupNames (infoReferences info |>.filter projectName)
          nodes := nodes.push (jsonNode current info)
          for target in refs do
            edges := edges.push <| Json.mkObj [
              ("from", Json.str current.toString),
              ("to", Json.str target.toString)
            ]
            if !seen.contains target then
              queue := queue.push target
  let payload := Json.mkObj [
    ("schema", Json.str "navier-stokes-review-lean-environment-closure/v2"),
    ("roots", jsonNames roots),
    ("nodes", Json.arr nodes),
    ("edges", Json.arr edges)
  ]
  liftIO <| IO.FS.writeFile output (Json.compress payload ++ "\n")
  logInfo m!"Exported {roots.size} roots, {nodes.size} project declarations, and {edges.size} edges to {output}"

end NavierStokesReview.Audit

exportReviewEnvironmentClosure "NavierStokesReview/evidence/lean_environment_closure_all_public_roots_2026-09-28.json"
