# Staff the constrained step

Twenty-four kits are prepared. Twenty pass inspection. Two dozen borrowers have a reservation. A manager estimates that one release signer can authorize 14 cases in the remaining time. How many successful handoffs can this shift promise? The answer is a bound, not a commitment.

You will model stages in a constrained queue, specify which counts are capacities and which are observed outcomes, and decide what to change when a day stops looking normal.

## Calculate the ceiling

During one window, suppose each handoff requires a distinct prepared kit that has passed inspection, one authorization, and one counter slot. Demand means eligible confirmed requests. For the first calculation assume all 20 passing kits and their matching requests are available in time, there is no ready stock carried in, and the numerical capacities have no other hidden dependencies. Then

```text
handoff ceiling = min(confirmed demand, kits that pass inspection,
                      authorization slots, counter slots)
```

The upper bound in the changed window is min(24, 20, 14, 22) = 14. Add six preparations and keep the inspection and release numbers fixed. Now there are 30 prepared, still 20 passed, still 14 authorizations and at most 14 handoffs. Assuming the team attains that ceiling and each authorization is used, the prepared-but-uninspected or failed count rises from four to ten and six passed units await release. The work in process grew. Throughput did not.

Real order matters. If the first inspections come in five minutes before close, 22 nominal counter slots may be irrelevant. If a particular kit cannot serve a particular reservation, the minimum can overstate completion. Use dated state logs and distinguish planned capacity from measured count.

## Run an abnormal week

Suppose a qualified second release owner adds four slots. With all other quantities unchanged, the new ceiling is 18. If an inspection failure leaves only 12 passing kits, the added slots do not raise the ceiling above 12. If four previously passed kits were safely carried into the window and remain eligible, they count as supply after rechecking status, not as this Saturday's preparations. They cannot bypass the release queue.

Write a checkpoint before noon. List the number prepared, passed, authorized, handed off and held, along with an estimate of remaining staffed slots. Compare the constraints against the time left. Choose one action: redeploy a trained release owner, call for authorized inspection coverage, inform borrowers promptly of an unavailable window, or hold the release pending evidence. Never move unqualified staff into a safety role.

## Try it

Given demand 24, 20 passing kits, 14 authorizations and a temporary counter capacity of nine, where is the binding stage? How many more handoffs could an extra release signer alone produce?

**Check.** The ceiling is nine. Capacity at the counter binds; the signer alone adds zero to the ceiling. First check whether the nine appointment slots correspond to actual arrival times. The [offline checker](../checks/README.md) is a small arithmetic model, not a staffing forecast.
