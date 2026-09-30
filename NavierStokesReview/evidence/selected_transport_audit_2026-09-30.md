# Hardened selected-endpoint transport audit

This report separates source declaration triage from Lean-environment evidence.
A co-occurrence is not a transport proof. No absence result is promoted to an impossibility theorem.

## Audit contract

A declaration is a transport candidate only when the same declaration binds selected-field terms and moment terms, and also contains an equality/transport conclusion. A `manual_transport_candidate` is a positive theorem/lemma/example whose declaration body also binds the selected expression and transformation terms. Negative, compatibility, countermodel, and conditional-gate declarations are separated before this category. All candidates remain review targets until compiled and manually checked.

- Source declarations indexed: **31472**
- Joint source candidates: **0**
- Full manual candidates: **0**
- Joint candidates by origin: **{}**
- Manual candidates by origin: **{}**
- Environment closure supplied: **False**
- Environment status: **not_supplied**
- Missing environment roots: **none**
- Environment declarations with endpoint/moment/transform terms in their type: **0**

## Source candidates

| Origin | Category | File | Lines | Declaration | Field terms | Moment terms | Transform terms |
|---|---|---|---:|---|---|---|---|

## Interpretation boundary

`manual_transport_candidate` means only that a declaration deserves direct Lean review. It does not prove that the equality is the paper's equality, that its domain is the selected whole-space field, or that its premises are inhabited. A conditional `False` theorem is not an endpoint contradiction until every hypothesis is derived on the selected branch. `conditional_or_obstruction_candidate` includes useful adversarial probes, but never counts as a selected-field impossibility theorem by itself.

The report therefore cannot by itself justify `FORMALLY REFUTED`, `False`, `Delta m != 0`, or `zero percent formalised`. Those labels require a compiled zero-sorry theorem or a complete source-backed proof with all concrete premises.
